/**
 * 考研英语二核心词 (2010-2026) 背诵应用核心交互脚本
 */

(function () {
  'use strict';

  // 全局数据源
  let allWords = [];
  
  // 运行状态
  let currentSession = {
    year: 'all',
    section: 'all',
    shuffle: true,
    autoSpeak: true,
    queue: [],              // 待背诵单词列表（动态队列）
    rememberedIds: new Set(), // 本轮已经真正记住的词 ID
    historyCount: 0,        // 本轮已经翻阅/判定的总词次数
    currentWord: null,      // 当前正在背诵的词
    cardState: 'question',  // 'question' (只看单词) | 'answer' (展示释义)
    lastChoice: null,       // 'remember' | 'forgot'
    currentGroup: [],       // 当前每 10 个一组的记录
    groupIndex: 1,          // 当前第几组
    startTime: null,
    totalToLearn: 0         // 当前选择范围的总独立单词数
  };

  // DOM 元素引用
  const dom = {
    // 筛选区
    yearSelect: document.getElementById('yearSelect'),
    sectionSelect: document.getElementById('sectionSelect'),
    filterCountBadge: document.getElementById('filterCountBadge'),
    orderShuffle: document.getElementById('orderShuffle'),
    orderSequence: document.getElementById('orderSequence'),
    labelShuffle: document.getElementById('labelShuffle'),
    labelSequence: document.getElementById('labelSequence'),
    orderModeHint: document.getElementById('orderModeHint'),
    autoSpeakCheck: document.getElementById('autoSpeakCheck'),
    startBtn: document.getElementById('startBtn'),
    filterCard: document.getElementById('filterCard'),
    
    // 背诵区
    recitationView: document.getElementById('recitationView'),
    statusTotal: document.getElementById('statusTotal'),
    statusRemembered: document.getElementById('statusRemembered'),
    statusRemaining: document.getElementById('statusRemaining'),
    statusGroup: document.getElementById('statusGroup'),
    progressBar: document.getElementById('progressBar'),
    
    // 卡片
    flashcard: document.getElementById('flashcard'),
    tagYear: document.getElementById('tagYear'),
    tagSection: document.getElementById('tagSection'),
    tagOrderMode: document.getElementById('tagOrderMode'),
    wordTitle: document.getElementById('wordTitle'),
    speakBtn: document.getElementById('speakBtn'),
    answerPanel: document.getElementById('answerPanel'),
    answerPos: document.getElementById('answerPos'),
    answerTrans: document.getElementById('answerTrans'),
    answerExtra: document.getElementById('answerExtra'),
    
    // 按钮区
    actionsQuestion: document.getElementById('actionsQuestion'),
    actionsAnswerRemember: document.getElementById('actionsAnswerRemember'),
    actionsAnswerForgot: document.getElementById('actionsAnswerForgot'),
    
    btnRemember: document.getElementById('btnRemember'),
    btnForgot: document.getElementById('btnForgot'),
    btnMistake: document.getElementById('btnMistake'),
    btnNextCorrect: document.getElementById('btnNextCorrect'),
    btnNextReview: document.getElementById('btnNextReview'),
    
    // 10词阶段小结 Modal
    summaryModal: document.getElementById('summaryModal'),
    summaryGroupBadge: document.getElementById('summaryGroupBadge'),
    summaryTableBody: document.getElementById('summaryTableBody'),
    summaryContinueBtn: document.getElementById('summaryContinueBtn'),
    
    // 结算完成卡片
    celebrateView: document.getElementById('celebrateView'),
    cStatTotal: document.getElementById('cStatTotal'),
    cStatAccuracy: document.getElementById('cStatAccuracy'),
    cStatTime: document.getElementById('cStatTime'),
    btnRestartSession: document.getElementById('btnRestartSession'),
    btnChangeFilter: document.getElementById('btnChangeFilter'),
    
    // 词汇库浏览弹窗
    browseModal: document.getElementById('browseModal'),
    browseSearch: document.getElementById('browseSearch'),
    browseTableBody: document.getElementById('browseTableBody'),
    browseCount: document.getElementById('browseCount'),
    btnOpenBrowse: document.getElementById('btnOpenBrowse'),
    btnCloseBrowse: document.getElementById('btnCloseBrowse'),
    
    // 主题切换
    themeToggleBtn: document.getElementById('themeToggleBtn')
  };

  // 初始化应用程序
  function init() {
    if (window.KNOW_WORDS_DATA && Array.isArray(window.KNOW_WORDS_DATA)) {
      allWords = window.KNOW_WORDS_DATA;
    } else {
      console.warn("未直接读取到 KNOW_WORDS_DATA，尝试从同名 JSON 加载...");
      fetch('words_data.json')
        .then(res => res.json())
        .then(data => {
          allWords = data;
          populateSelectors();
          updateFilterStats();
        })
        .catch(err => {
          console.error("加载单词数据失败:", err);
          alert("单词数据加载失败，请确保与 words_data.js 同目录。");
        });
      return;
    }

    populateSelectors();
    updateFilterStats();
    setupEventListeners();
    setupTheme();
  }

  // 填充年份和篇章下拉框
  function populateSelectors() {
    // 年份列表: 2021 ~ 2010 降序
    const years = Array.from(new Set(allWords.map(w => w.year))).sort((a, b) => b - a);
    dom.yearSelect.innerHTML = '<option value="all">全部真题年份 (2010-2026)</option>';
    years.forEach(y => {
      const opt = document.createElement('option');
      opt.value = y;
      opt.textContent = `${y} 年`;
      dom.yearSelect.appendChild(opt);
    });

    // 题型篇章列表
    updateSectionOptions();
  }

  // 根据选中的年份更新篇章选项
  function updateSectionOptions() {
    const selectedYear = dom.yearSelect.value;
    let filtered = allWords;
    if (selectedYear !== 'all') {
      filtered = allWords.filter(w => w.year === parseInt(selectedYear));
    }
    
    // 常用固定标准顺序排序
    const standardOrder = [
      '完形填空',
      '传统阅读 Text 1',
      '传统阅读 Text 2',
      '传统阅读 Text 3',
      '传统阅读 Text 4',
      '新题型',
      '翻译与写作'
    ];

    const currentSections = Array.from(new Set(filtered.map(w => w.section)));
    currentSections.sort((a, b) => {
      let idxA = standardOrder.indexOf(a);
      let idxB = standardOrder.indexOf(b);
      if (idxA === -1) idxA = 99;
      if (idxB === -1) idxB = 99;
      return idxA - idxB;
    });

    const prevVal = dom.sectionSelect.value;
    dom.sectionSelect.innerHTML = '<option value="all">全部篇章 / 题型</option>';
    currentSections.forEach(sec => {
      const opt = document.createElement('option');
      opt.value = sec;
      const count = filtered.filter(w => w.section === sec).length;
      opt.textContent = `${sec} (${count}词)`;
      dom.sectionSelect.appendChild(opt);
    });

    // 如果之前选的依然存在，保留选项
    if (currentSections.includes(prevVal)) {
      dom.sectionSelect.value = prevVal;
    } else {
      dom.sectionSelect.value = 'all';
    }
  }

  // 计算当前筛选条件下的单词数量
  function updateFilterStats() {
    const list = getFilteredWords();
    dom.filterCountBadge.textContent = `${list.length} 个单词`;
  }

  // 获取当前筛选条件对应的单词数组
  function getFilteredWords() {
    const y = dom.yearSelect.value;
    const s = dom.sectionSelect.value;
    return allWords.filter(w => {
      const matchYear = (y === 'all') || (w.year === parseInt(y));
      const matchSection = (s === 'all') || (w.section === s);
      return matchYear && matchSection;
    });
  }

  // 绑定事件
  function setupEventListeners() {
    dom.yearSelect.addEventListener('change', () => {
      updateSectionOptions();
      updateFilterStats();
    });

    dom.sectionSelect.addEventListener('change', () => {
      updateFilterStats();
    });

    dom.startBtn.addEventListener('click', startRecitation);

    // 出词顺序切换 (乱序/顺序)
    const orderRadios = document.querySelectorAll('input[name="orderMode"]');
    orderRadios.forEach(radio => {
      radio.addEventListener('change', () => {
        const isShuffle = dom.orderShuffle ? dom.orderShuffle.checked : true;
        if (dom.labelShuffle) dom.labelShuffle.classList.toggle('active', isShuffle);
        if (dom.labelSequence) dom.labelSequence.classList.toggle('active', !isShuffle);
        if (dom.orderModeHint) {
          dom.orderModeHint.innerHTML = isShuffle
            ? '当前模式: <strong style="color:var(--primary)">🔀 随机乱序背诵</strong> (打乱顺序测试记忆)'
            : '当前模式: <strong style="color:var(--success)">🔢 真题顺序背诵</strong> (按试卷原出现次序逐个记忆)';
        }
      });
    });

    // 背诵按钮事件
    dom.btnRemember.addEventListener('click', () => handleFirstChoice('remember'));
    dom.btnForgot.addEventListener('click', () => handleFirstChoice('forgot'));
    
    // 答案二度确认
    dom.btnMistake.addEventListener('click', handleMistake);
    dom.btnNextCorrect.addEventListener('click', handleConfirmRemembered);
    dom.btnNextReview.addEventListener('click', handleNextReview);

    // 小结弹窗继续
    dom.summaryContinueBtn.addEventListener('click', closeSummaryAndContinue);

    // 发音
    dom.speakBtn.addEventListener('click', () => speakWord(currentSession.currentWord?.word));
    dom.wordTitle.addEventListener('click', () => speakWord(currentSession.currentWord?.word));

    // 结算按钮
    dom.btnRestartSession.addEventListener('click', startRecitation);
    dom.btnChangeFilter.addEventListener('click', () => {
      dom.celebrateView.classList.add('hidden');
      dom.recitationView.classList.add('hidden');
      dom.filterCard.classList.remove('hidden');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // 词库总览
    dom.btnOpenBrowse.addEventListener('click', openBrowseModal);
    dom.btnCloseBrowse.addEventListener('click', () => dom.browseModal.classList.add('hidden'));
    dom.browseSearch.addEventListener('input', renderBrowseList);

    // 键盘快捷键监听
    window.addEventListener('keydown', handleGlobalKeydown);
  }

  // 开始背诵一轮
  function startRecitation() {
    const targetWords = getFilteredWords();
    if (targetWords.length === 0) {
      alert("当前筛选条件下没有单词，请重新选择！");
      return;
    }

    const isShuffle = dom.orderShuffle ? dom.orderShuffle.checked : false;
    let queue = [...targetWords];
    if (isShuffle) {
      shuffleArray(queue);
    }

    currentSession = {
      year: dom.yearSelect.value,
      section: dom.sectionSelect.value,
      shuffle: isShuffle,
      autoSpeak: dom.autoSpeakCheck ? dom.autoSpeakCheck.checked : true,
      queue: queue,
      rememberedIds: new Set(),
      historyCount: 0,
      currentWord: null,
      cardState: 'question',
      lastChoice: null,
      currentGroup: [],
      groupIndex: 1,
      startTime: Date.now(),
      totalToLearn: queue.length
    };

    // 切换界面
    dom.filterCard.classList.add('hidden');
    dom.celebrateView.classList.add('hidden');
    dom.recitationView.classList.remove('hidden');

    showNextWord();
  }

  // 呈现下一个单词
  function showNextWord() {
    // 检查队列是否已空
    if (currentSession.queue.length === 0) {
      // 队列空了，代表本轮所有单词都已经真正掌握了！
      finishSession();
      return;
    }

    // 从队列首部取出单词
    currentSession.currentWord = currentSession.queue.shift();
    currentSession.cardState = 'question';
    currentSession.lastChoice = null;

    updateStatusBar();
    renderCardQuestion();

    if (currentSession.autoSpeak) {
      speakWord(currentSession.currentWord.word);
    }
  }

  // 渲染卡片为提问态（只展示英文）
  function renderCardQuestion() {
    const w = currentSession.currentWord;
    dom.tagYear.textContent = `${w.year} 年`;
    dom.tagSection.textContent = w.section;
    if (dom.tagOrderMode) {
      if (currentSession.shuffle) {
        dom.tagOrderMode.textContent = '🔀 乱序模式';
        dom.tagOrderMode.classList.remove('sequence-mode');
      } else {
        dom.tagOrderMode.textContent = '🔢 顺序模式';
        dom.tagOrderMode.classList.add('sequence-mode');
      }
    }
    dom.wordTitle.textContent = w.word;

    // 隐藏释义
    dom.answerPanel.classList.add('hidden');

    // 显示记得/不记得按钮
    dom.actionsQuestion.classList.remove('hidden');
    dom.actionsAnswerRemember.classList.add('hidden');
    dom.actionsAnswerForgot.classList.add('hidden');
  }

  // 用户点击初始选择：'remember' (记得) 或 'forgot' (不记得)
  function handleFirstChoice(choice) {
    if (currentSession.cardState !== 'question') return;

    currentSession.cardState = 'answer';
    currentSession.lastChoice = choice;

    // 展开答案
    showAnswerPanel();

    // 切换操作按钮
    dom.actionsQuestion.classList.add('hidden');
    if (choice === 'remember') {
      dom.actionsAnswerRemember.classList.remove('hidden');
      dom.actionsAnswerForgot.classList.add('hidden');
    } else {
      dom.actionsAnswerRemember.classList.add('hidden');
      dom.actionsAnswerForgot.classList.remove('hidden');
    }
  }

  // 展示详细释义面板
  function showAnswerPanel() {
    const w = currentSession.currentWord;
    dom.answerPos.textContent = w.pos || '释义';
    dom.answerTrans.textContent = w.trans;
    
    let extraText = `题型归类: ${w.section} · ${w.category || '核心词'}`;
    dom.answerExtra.textContent = extraText;
    
    dom.answerPanel.classList.remove('hidden');
  }

  // 确认“确实记住了” -> 本轮不再出现
  function handleConfirmRemembered() {
    const w = currentSession.currentWord;
    currentSession.rememberedIds.add(w.id);
    recordWordResult(w, true);
    checkGroupAndProceed();
  }

  // 考生发现自己“记错了” -> 放回待背诵队列
  function handleMistake() {
    const w = currentSession.currentWord;
    // 放回队列末尾
    currentSession.queue.push(w);
    recordWordResult(w, false);
    checkGroupAndProceed();
  }

  // “没记住” -> 放回待背诵队列
  function handleNextReview() {
    const w = currentSession.currentWord;
    // 放回队列末尾
    currentSession.queue.push(w);
    recordWordResult(w, false);
    checkGroupAndProceed();
  }

  // 记录单词到当前每10个一组的列表中
  function recordWordResult(wordObj, isRemembered) {
    currentSession.historyCount++;
    currentSession.currentGroup.push({
      id: wordObj.id,
      word: wordObj.word,
      pos: wordObj.pos,
      trans: wordObj.trans,
      year: wordObj.year,
      section: wordObj.section,
      remembered: isRemembered
    });
  }

  // 检查是否达到每 10 个一组或本轮结束
  function checkGroupAndProceed() {
    // 每 10 个为一组弹窗总结
    if (currentSession.currentGroup.length === 10) {
      showGroupSummaryModal();
      return;
    }

    // 如果队列已经全部背完并且当前组也有单词
    if (currentSession.queue.length === 0 && currentSession.currentGroup.length > 0) {
      showGroupSummaryModal(true); // 最后一组可能不足10个
      return;
    }

    showNextWord();
  }

  // 弹出阶段小结 Modal（每十个单词一组总结）
  function showGroupSummaryModal(isLastGroup = false) {
    dom.summaryGroupBadge.textContent = isLastGroup 
      ? `第 ${currentSession.groupIndex} 组 (本轮收尾 · 共 ${currentSession.currentGroup.length} 词)`
      : `第 ${currentSession.groupIndex} 组完成 (10 词回顾)`;
    
    dom.summaryTableBody.innerHTML = '';

    currentSession.currentGroup.forEach((item, idx) => {
      const tr = document.createElement('tr');
      
      const statusBadge = item.remembered
        ? '<span class="status-tag remembered">已记住</span>'
        : '<span class="status-tag repeat">待复习</span>';

      tr.innerHTML = `
        <td class="col-idx">${idx + 1}</td>
        <td class="col-word">
          <div class="col-word-voice">
            <span>${escapeHtml(item.word)}</span>
            <button class="mini-speak-btn" data-word="${escapeHtml(item.word)}" title="朗读">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                <path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>
              </svg>
            </button>
          </div>
        </td>
        <td class="col-trans">
          <strong style="color:var(--primary); font-size:0.85rem; margin-right:4px;">${escapeHtml(item.pos || '')}</strong>
          ${escapeHtml(item.trans)}
        </td>
        <td class="col-status">${statusBadge}</td>
      `;

      dom.summaryTableBody.appendChild(tr);
    });

    // 绑定小发音按钮
    dom.summaryTableBody.querySelectorAll('.mini-speak-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        speakWord(btn.getAttribute('data-word'));
      });
    });

    dom.summaryModal.classList.remove('hidden');
    dom.summaryContinueBtn.focus();
  }

  // 关闭小结弹窗并继续
  function closeSummaryAndContinue() {
    dom.summaryModal.classList.add('hidden');
    currentSession.currentGroup = [];
    currentSession.groupIndex++;

    if (currentSession.queue.length === 0) {
      finishSession();
    } else {
      showNextWord();
    }
  }

  // 更新顶部状态看板和进度条
  function updateStatusBar() {
    const total = currentSession.totalToLearn;
    const remembered = currentSession.rememberedIds.size;
    const remaining = total - remembered;
    const percent = Math.min(100, Math.round((remembered / total) * 100));

    dom.statusTotal.textContent = total;
    dom.statusRemembered.textContent = remembered;
    dom.statusRemaining.textContent = remaining;
    dom.statusGroup.textContent = `第 ${currentSession.groupIndex} 组 (${currentSession.currentGroup.length}/10)`;
    dom.progressBar.style.width = `${percent}%`;
  }

  // 完成背诵
  function finishSession() {
    dom.recitationView.classList.add('hidden');
    dom.summaryModal.classList.add('hidden');
    dom.celebrateView.classList.remove('hidden');

    const durationSec = Math.round((Date.now() - currentSession.startTime) / 1000);
    const mins = Math.floor(durationSec / 60);
    const secs = durationSec % 60;
    const timeStr = mins > 0 ? `${mins}分${secs}秒` : `${secs}秒`;

    const total = currentSession.totalToLearn;
    const history = currentSession.historyCount;
    const accuracy = history > 0 ? Math.round((total / history) * 100) : 100;

    dom.cStatTotal.textContent = total;
    dom.cStatAccuracy.textContent = `${accuracy}%`;
    dom.cStatTime.textContent = timeStr;
  }

  // 词库总览检索弹窗
  function openBrowseModal() {
    dom.browseModal.classList.remove('hidden');
    dom.browseSearch.value = '';
    renderBrowseList();
    dom.browseSearch.focus();
  }

  function renderBrowseList() {
    const query = dom.browseSearch.value.trim().toLowerCase();
    let list = allWords;
    if (query) {
      list = allWords.filter(w => 
        w.word.toLowerCase().includes(query) || 
        w.trans.includes(query) ||
        String(w.year).includes(query) ||
        w.section.includes(query)
      );
    }

    dom.browseCount.textContent = `共搜索到 ${list.length} 个单词 (总库 ${allWords.length} 词)`;
    dom.browseTableBody.innerHTML = '';

    // 最多一次渲染 150 条以保证极度丝滑
    const displayList = list.slice(0, 150);
    displayList.forEach((item, idx) => {
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td class="col-idx">${idx + 1}</td>
        <td class="col-word">
          <div class="col-word-voice">
            <span>${escapeHtml(item.word)}</span>
            <button class="mini-speak-btn" data-word="${escapeHtml(item.word)}" title="朗读">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                <path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>
              </svg>
            </button>
          </div>
        </td>
        <td class="col-trans">
          <span style="display:inline-block; font-size:0.75rem; background:var(--bg-subtle); padding:1px 6px; border-radius:4px; margin-right:6px; color:var(--text-muted)">${item.year} ${item.section}</span>
          <strong style="color:var(--primary); font-size:0.85rem; margin-right:4px;">${escapeHtml(item.pos || '')}</strong>
          ${escapeHtml(item.trans)}
        </td>
      `;
      dom.browseTableBody.appendChild(tr);
    });

    dom.browseTableBody.querySelectorAll('.mini-speak-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        speakWord(btn.getAttribute('data-word'));
      });
    });
  }

  // 键盘快捷键响应
  function handleGlobalKeydown(e) {
    // 如果在搜索框输入，不劫持键盘按键
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') {
      if (e.key === 'Escape') {
        dom.browseModal.classList.add('hidden');
      }
      return;
    }

    // 小结弹窗打开时
    if (!dom.summaryModal.classList.contains('hidden')) {
      if (e.key === 'Enter' || e.key === ' ' || e.key === 'Escape') {
        e.preventDefault();
        closeSummaryAndContinue();
      }
      return;
    }

    // 浏览词库弹窗打开时
    if (!dom.browseModal.classList.contains('hidden')) {
      if (e.key === 'Escape') {
        dom.browseModal.classList.add('hidden');
      }
      return;
    }

    // 背诵界面活跃中
    if (!dom.recitationView.classList.contains('hidden')) {
      // 发音快捷键: V 或 P
      if (e.key === 'v' || e.key === 'V' || e.key === 'p' || e.key === 'P') {
        e.preventDefault();
        speakWord(currentSession.currentWord?.word);
        return;
      }

      // 阶段 1: 提问态 (未看答案)
      if (currentSession.cardState === 'question') {
        // 按 1 / J / 左箭头 -> 记得
        if (e.key === '1' || e.key === 'j' || e.key === 'J' || e.key === 'ArrowLeft') {
          e.preventDefault();
          handleFirstChoice('remember');
        }
        // 按 2 / K / 右箭头 -> 不记得
        else if (e.key === '2' || e.key === 'k' || e.key === 'K' || e.key === 'ArrowRight' || e.key === ' ') {
          e.preventDefault();
          handleFirstChoice('forgot');
        }
      }
      // 阶段 2: 答案展示态
      else if (currentSession.cardState === 'answer') {
        if (currentSession.lastChoice === 'remember') {
          // 记得后的选项:
          // 按 1 / 空格 / 回车 -> 确实记住了 (下一个)
          if (e.key === '1' || e.key === ' ' || e.key === 'Enter' || e.key === 'j' || e.key === 'J' || e.key === 'ArrowRight') {
            e.preventDefault();
            handleConfirmRemembered();
          }
          // 按 2 / 3 / Backspace / K -> 记错了！
          else if (e.key === '2' || e.key === '3' || e.key === 'Backspace' || e.key === 'k' || e.key === 'K' || e.key === 'ArrowLeft') {
            e.preventDefault();
            handleMistake();
          }
        } else {
          // 之前点了不记得:
          // 任何确认键继续 (空格, 回车, 1, 2)
          if (e.key === ' ' || e.key === 'Enter' || e.key === '1' || e.key === '2' || e.key === 'j' || e.key === 'k' || e.key === 'ArrowRight') {
            e.preventDefault();
            handleNextReview();
          }
        }
      }
    }
  }

  // 语音合成发音
  function speakWord(text) {
    if (!text || !('speechSynthesis' in window)) return;
    try {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = 'en-US';
      utterance.rate = 0.95;
      window.speechSynthesis.speak(utterance);
    } catch (e) {
      console.warn('SpeechSynthesis error:', e);
    }
  }

  // 数组洗牌算法
  function shuffleArray(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  // HTML 转义防 XSS
  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // 深浅色主题切换
  function setupTheme() {
    const savedTheme = localStorage.getItem('know_english_theme') || 'light';
    setTheme(savedTheme);

    dom.themeToggleBtn.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme') || 'light';
      const nextTheme = current === 'dark' ? 'light' : 'dark';
      setTheme(nextTheme);
    });
  }

  function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('know_english_theme', theme);
    dom.themeToggleBtn.innerHTML = theme === 'dark'
      ? `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>`
      : `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>`;
  }

  // 页面加载完成后启动
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
