# -*- coding: utf-8 -*-
import json, os

base_dir = r"f:\obsidiannote\obsidian-\408\数据结构\考研英语二核心词背诵"
json_path = os.path.join(base_dir, "words_data.json")

with open(json_path, "r", encoding="utf-8") as f:
    words_data = json.load(f)

words_json_str = json.dumps(words_data, ensure_ascii=False)

html_template = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="theme-color" content="#4f46e5">
  <title>考研英语二核心词 (2010-2026) 移动端随身背</title>
  <style>
    :root {{
      --primary: #4f46e5;
      --primary-active: #3730a3;
      --primary-light: #e0e7ff;
      --success: #10b981;
      --success-active: #047857;
      --success-light: #d1fae5;
      --danger: #ef4444;
      --danger-active: #b91c1c;
      --danger-light: #fee2e2;
      --warning: #f59e0b;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --safe-bottom: max(16px, env(safe-area-inset-bottom));
    }}

    [data-theme="dark"] {{
      --primary: #6366f1;
      --primary-light: #1e1b4b;
      --bg: #090d16;
      --card-bg: #131b2e;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --border: #1e293b;
      --success-light: #064e3b;
      --danger-light: #7f1d1d;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
      user-select: none;
    }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Roboto, "PingFang SC", "Hiragino Sans GB", sans-serif;
      background: var(--bg);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      touch-action: manipulation;
    }}

    /* 顶部导航与状态条 */
    .app-header {{
      background: var(--card-bg);
      border-bottom: 1px solid var(--border);
      padding: 12px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 40;
    }}

    .app-brand {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .brand-pill {{
      background: var(--primary);
      color: white;
      font-weight: 800;
      font-size: 0.85rem;
      padding: 2px 8px;
      border-radius: 6px;
    }}

    .brand-name {{
      font-weight: 700;
      font-size: 1rem;
    }}

    .header-btns {{
      display: flex;
      gap: 8px;
    }}

    .h-btn {{
      background: none;
      border: 1px solid var(--border);
      color: var(--text-muted);
      width: 36px;
      height: 36px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }}

    /* 容器 */
    .container {{
      flex: 1;
      display: flex;
      flex-direction: column;
      padding: 14px 16px var(--safe-bottom);
      max-width: 540px;
      width: 100%;
      margin: 0 auto;
    }}

    /* 筛选与设置面板 */
    .setup-card {{
      background: var(--card-bg);
      border-radius: 16px;
      padding: 20px 16px;
      border: 1px solid var(--border);
      box-shadow: 0 4px 12px rgba(0,0,0,0.04);
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .form-item {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .form-label {{
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .form-select {{
      width: 100%;
      padding: 12px 14px;
      border-radius: 12px;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text-main);
      font-size: 0.95rem;
      font-weight: 500;
      outline: none;
      -webkit-appearance: none;
      appearance: none;
      background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2364748b' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
      background-repeat: no-repeat;
      background-position: right 12px center;
      background-size: 16px;
    }}

    .options-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 6px 0;
    }}

    .switch-label {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.9rem;
      color: var(--text-main);
    }}

    .switch-label input {{
      width: 18px;
      height: 18px;
      accent-color: var(--primary);
    }}

    .m-order-toggle {{
      display: flex;
      background: var(--bg);
      padding: 4px;
      border-radius: 12px;
      border: 1px solid var(--border);
      gap: 6px;
      margin-top: 4px;
    }}

    .m-order-btn {{
      flex: 1;
      text-align: center;
      padding: 9px 6px;
      border-radius: 9px;
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .m-order-btn input {{
      display: none;
    }}

    .m-order-btn.active {{
      background: var(--card-bg);
      color: var(--primary);
      box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }}

    .badge-order {{
      background: var(--primary-light);
      color: var(--primary);
      padding: 2px 7px;
      border-radius: 4px;
    }}

    .badge-order.seq {{
      background: var(--success-light);
      color: var(--success);
    }}

    .btn-big-start {{
      background: var(--primary);
      color: white;
      border: none;
      border-radius: 14px;
      padding: 16px;
      font-size: 1.05rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 4px 14px rgba(79, 70, 229, 0.35);
      cursor: pointer;
      margin-top: 6px;
    }}

    .btn-big-start:active {{
      background: var(--primary-active);
      transform: scale(0.98);
    }}

    /* 背诵主视图 */
    .recite-view {{
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    /* 顶部进度指标条 */
    .pill-status {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: var(--card-bg);
      border-radius: 12px;
      padding: 10px 14px;
      border: 1px solid var(--border);
      font-size: 0.85rem;
      font-weight: 600;
    }}

    .pill-group-tag {{
      background: var(--primary-light);
      color: var(--primary);
      padding: 2px 8px;
      border-radius: 6px;
      font-size: 0.78rem;
    }}

    .progress-bar-wrap {{
      width: 100%;
      height: 6px;
      background: var(--border);
      border-radius: 10px;
      overflow: hidden;
    }}

    .progress-bar-inner {{
      height: 100%;
      background: var(--primary);
      width: 0%;
      transition: width 0.25s ease;
    }}

    /* 单词大卡片 */
    .word-card {{
      background: var(--card-bg);
      border-radius: 20px;
      border: 1px solid var(--border);
      box-shadow: 0 6px 20px rgba(0,0,0,0.06);
      padding: 28px 18px 22px;
      flex: 1;
      min-height: 280px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      position: relative;
      cursor: pointer;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}

    .word-card:active {{
      transform: scale(0.995);
    }}

    .card-meta-tags {{
      position: absolute;
      top: 14px;
      left: 16px;
      display: flex;
      gap: 6px;
      font-size: 0.72rem;
      font-weight: 700;
    }}

    .badge-year {{
      background: var(--primary-light);
      color: var(--primary);
      padding: 2px 7px;
      border-radius: 4px;
    }}

    .badge-section {{
      background: var(--border);
      color: var(--text-muted);
      padding: 2px 7px;
      border-radius: 4px;
    }}

    .word-text {{
      font-size: 2.3rem;
      font-weight: 800;
      color: var(--text-main);
      margin-bottom: 12px;
      line-height: 1.2;
      word-break: break-word;
    }}

    .speak-circle-btn {{
      background: var(--primary-light);
      color: var(--primary);
      border: none;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }}

    .speak-circle-btn:active {{
      background: var(--primary);
      color: white;
      transform: scale(1.1);
    }}

    /* 答案展开框 */
    .answer-box {{
      width: 100%;
      background: var(--bg);
      border-radius: 12px;
      padding: 16px;
      margin-top: 18px;
      text-align: left;
      border-left: 4px solid var(--primary);
      animation: slideUp 0.2s ease-out;
    }}

    @keyframes slideUp {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .pos-pill {{
      display: inline-block;
      background: var(--primary);
      color: white;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
      margin-right: 6px;
    }}

    .trans-text {{
      font-size: 1.1rem;
      font-weight: 600;
      line-height: 1.45;
    }}

    .trans-sub {{
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-top: 6px;
    }}

    /* 底部操作区域 (适合双手/单手大拇指快速点击) */
    .bottom-actions {{
      display: flex;
      gap: 12px;
      margin-top: auto;
      padding-top: 6px;
    }}

    .touch-btn {{
      flex: 1;
      height: 56px;
      border-radius: 14px;
      border: none;
      font-size: 1.1rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      cursor: pointer;
      box-shadow: 0 3px 8px rgba(0,0,0,0.1);
      transition: transform 0.1s ease;
    }}

    .touch-btn:active {{
      transform: scale(0.96);
    }}

    .btn-f-forgot {{
      background: var(--danger);
      color: white;
    }}
    .btn-f-forgot:active {{
      background: var(--danger-active);
    }}

    .btn-f-remember {{
      background: var(--success);
      color: white;
    }}
    .btn-f-remember:active {{
      background: var(--success-active);
    }}

    .btn-f-mistake {{
      background: #e11d48;
      color: white;
    }}

    .btn-f-next {{
      background: var(--primary);
      color: white;
    }}
    .btn-f-next:active {{
      background: var(--primary-active);
    }}

    /* 10 词回顾抽屉 / Modal */
    .m-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.6);
      backdrop-filter: blur(4px);
      z-index: 100;
      display: flex;
      align-items: flex-end;
    }}

    .m-sheet {{
      background: var(--card-bg);
      width: 100%;
      border-radius: 20px 20px 0 0;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      padding-bottom: var(--safe-bottom);
      animation: sheetUp 0.25s cubic-bezier(0.32, 1, 0.23, 1);
    }}

    @keyframes sheetUp {{
      from {{ transform: translateY(100%); }}
      to {{ transform: translateY(0); }}
    }}

    .sheet-header {{
      padding: 16px 20px;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .sheet-title {{
      font-size: 1.1rem;
      font-weight: 800;
    }}

    .sheet-list {{
      overflow-y: auto;
      padding: 10px 16px;
      flex: 1;
    }}

    .summary-item {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 0;
      border-bottom: 1px solid var(--border);
    }}

    .sum-word {{
      font-weight: 700;
      font-size: 1.05rem;
    }}

    .sum-trans {{
      font-size: 0.88rem;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    .badge-status {{
      font-size: 0.72rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
    }}
    .badge-ok {{ background: var(--success-light); color: #047857; }}
    .badge-no {{ background: var(--danger-light); color: #b91c1c; }}

    .sheet-footer {{
      padding: 12px 16px 6px;
    }}

    /* 结算卡片 */
    .celebrate-box {{
      background: var(--card-bg);
      border-radius: 20px;
      border: 1px solid var(--border);
      padding: 36px 20px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 16px;
    }}

    .c-emoji {{
      font-size: 3.2rem;
      animation: bounce 0.8s infinite alternate;
    }}

    @keyframes bounce {{
      from {{ transform: translateY(0); }}
      to {{ transform: translateY(-8px); }}
    }}

    /* 检索抽屉 */
    .search-input {{
      width: 100%;
      padding: 10px 14px;
      border-radius: 10px;
      border: 1px solid var(--border);
      background: var(--bg);
      color: var(--text-main);
      font-size: 0.95rem;
      outline: none;
      margin-bottom: 10px;
    }}

    .hidden {{
      display: none !important;
    }}
  </style>
</head>
<body>
  <header class="app-header">
    <div class="app-brand">
      <span class="brand-pill">手机版</span>
      <span class="brand-name">英语二核心词随身背</span>
    </div>
    <div class="header-btns">
      <a href="index.html" class="h-btn" title="电脑桌面版" style="text-decoration:none; width:auto; padding:0 8px; font-size:0.75rem; font-weight:600;">💻 电脑版</a>
      <button id="mSearchBtn" class="h-btn" title="查词">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
      </button>
      <button id="mThemeBtn" class="h-btn" title="深浅色">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
      </button>
    </div>
  </header>

  <main class="container">
    <!-- 1. 设置与开始界面 -->
    <div id="mSetupCard" class="setup-card">
      <div style="font-size:1.15rem; font-weight:800; display:flex; justify-content:space-between; align-items:center;">
        <span>🎯 选择背诵内容</span>
        <span id="mCountBadge" style="font-size:0.8rem; background:var(--primary-light); color:var(--primary); padding:3px 8px; border-radius:12px;">4385 词</span>
      </div>

      <div class="form-item">
        <label class="form-label">真题年份</label>
        <select id="mYearSelect" class="form-select"></select>
      </div>

      <div class="form-item">
        <label class="form-label">题型 / 篇章</label>
        <select id="mSectionSelect" class="form-select"></select>
      </div>

      <div class="form-item">
        <label class="form-label">出词顺序</label>
        <div class="m-order-toggle">
          <label class="m-order-btn active" id="mLabelShuffle">
            <input type="radio" name="mOrderMode" id="mOrderShuffle" value="shuffle" checked>
            <span>🔀 乱序背诵</span>
          </label>
          <label class="m-order-btn" id="mLabelSequence">
            <input type="radio" name="mOrderMode" id="mOrderSequence" value="sequence">
            <span>🔢 顺序背诵</span>
          </label>
        </div>
      </div>

      <div class="options-row">
        <label class="switch-label">
          <input type="checkbox" id="mAutoSpeakCheck" checked>
          <span>自动真人发音</span>
        </label>
      </div>

      <button id="mStartBtn" class="btn-big-start">
        <span>开始背诵</span>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
      </button>
    </div>

    <!-- 2. 背诵主界面 (默认隐藏) -->
    <div id="mReciteView" class="recite-view hidden">
      <!-- 进度信息 -->
      <div class="pill-status">
        <span class="pill-group-tag" id="mGroupBadge">第 1 组 (0/10)</span>
        <div>已记 <span id="mNumRemembered" style="color:var(--success)">0</span> / 剩 <span id="mNumRemaining" style="color:var(--danger)">0</span></div>
      </div>
      <div class="progress-bar-wrap">
        <div id="mProgressBar" class="progress-bar-inner"></div>
      </div>

      <!-- 单词主卡片 (点击任意处翻开答案) -->
      <div id="mWordCard" class="word-card">
        <div class="card-meta-tags">
          <span id="mTagYear" class="badge-year">2026 年</span>
          <span id="mTagSection" class="badge-section">传统阅读 Text 1</span>
          <span id="mTagOrderMode" class="badge-order">🔀 乱序</span>
        </div>

        <div id="mWordTitle" class="word-text">word</div>

        <div>
          <button id="mSpeakBtn" class="speak-circle-btn" title="朗读">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
          </button>
        </div>

        <!-- 详细释义面板 -->
        <div id="mAnswerBox" class="answer-box hidden">
          <div>
            <span id="mAnswerPos" class="pos-pill">n.</span>
            <span id="mAnswerTrans" class="trans-text">释义</span>
          </div>
          <div id="mAnswerSub" class="trans-sub">考点归类</div>
        </div>
      </div>

      <!-- 底部大拇指触控按键区 -->
      <!-- 阶段 1: 提问态 -->
      <div id="mActionsQuestion" class="bottom-actions">
        <button id="mBtnForgot" class="touch-btn btn-f-forgot">
          <span>✕ 不记得</span>
        </button>
        <button id="mBtnRemember" class="touch-btn btn-f-remember">
          <span>✓ 记得</span>
        </button>
      </div>

      <!-- 阶段 2: 选了记得后的二次确认 -->
      <div id="mActionsAnswerRemember" class="bottom-actions hidden">
        <button id="mBtnMistake" class="touch-btn btn-f-mistake">
          <span>记错了 (放回重背)</span>
        </button>
        <button id="mBtnConfirmOk" class="touch-btn btn-f-remember">
          <span>确实记住了 ➔</span>
        </button>
      </div>

      <!-- 阶段 2: 选了不记得后的继续 -->
      <div id="mActionsAnswerForgot" class="bottom-actions hidden">
        <button id="mBtnNextReview" class="touch-btn btn-f-next">
          <span>没记住 (放回队列) ➔</span>
        </button>
      </div>
    </div>

    <!-- 3. 本轮通关结算卡片 (默认隐藏) -->
    <div id="mCelebrateView" class="celebrate-box hidden">
      <div class="c-emoji">🎉</div>
      <h2 style="font-size:1.4rem; font-weight:800;">背完啦！全部搞定！</h2>
      <p style="color:var(--text-muted); font-size:0.95rem;">本轮所选的全部真题核心词汇已彻底掌握！</p>
      
      <div style="display:flex; justify-content:space-around; width:100%; margin:10px 0;">
        <div>
          <div id="mCStatTotal" style="font-size:1.6rem; font-weight:800; color:var(--primary)">0</div>
          <div style="font-size:0.75rem; color:var(--text-muted)">掌握词数</div>
        </div>
        <div>
          <div id="mCStatAccuracy" style="font-size:1.6rem; font-weight:800; color:var(--success)">100%</div>
          <div style="font-size:0.75rem; color:var(--text-muted)">一次记忆率</div>
        </div>
        <div>
          <div id="mCStatTime" style="font-size:1.6rem; font-weight:800; color:var(--warning)">0s</div>
          <div style="font-size:0.75rem; color:var(--text-muted)">总用时</div>
        </div>
      </div>

      <div style="display:flex; gap:10px; width:100%; margin-top:10px;">
        <button id="mBtnRestart" class="touch-btn btn-f-next" style="font-size:0.95rem;">再来一轮</button>
        <button id="mBtnBackSetup" class="touch-btn" style="background:var(--border); color:var(--text-main); font-size:0.95rem;">重选篇章</button>
      </div>
    </div>
  </main>

  <!-- 4. 每十个一组阶段小结 底部抽屉 Modal -->
  <div id="mSummaryModal" class="m-overlay hidden">
    <div class="m-sheet">
      <div class="sheet-header">
        <div class="sheet-title" id="mSummaryTitle">📝 第 1 组完成 (10 词回顾)</div>
      </div>
      <div class="sheet-list" id="mSummaryList">
        <!-- 动态生成 10 个词 -->
      </div>
      <div class="sheet-footer">
        <button id="mSummaryContinueBtn" class="btn-big-start" style="width:100%; margin:0;">继续背诵下一组 ➔</button>
      </div>
    </div>
  </div>

  <!-- 5. 快速查词抽屉 Modal -->
  <div id="mSearchModal" class="m-overlay hidden">
    <div class="m-sheet" style="max-height:90vh;">
      <div class="sheet-header">
        <span class="sheet-title">📖 4385 真题词库检索</span>
        <button id="mCloseSearchBtn" style="border:none; background:none; font-size:1.2rem; color:var(--text-muted);">✕</button>
      </div>
      <div style="padding:12px 16px 0;">
        <input type="text" id="mSearchInput" class="search-input" placeholder="输入英文、中文或年份检索...">
      </div>
      <div class="sheet-list" id="mSearchList">
        <!-- 动态填充 -->
      </div>
    </div>
  </div>

  <!-- 内嵌完整 4385 词库数据与移动端逻辑 -->
  <script>
    const ALL_WORDS = {words_json_str};

    (function() {{
      let queue = [];
      let rememberedSet = new Set();
      let currentWord = null;
      let cardState = 'question'; // 'question' | 'answer'
      let lastChoice = null;
      let currentGroup = [];
      let groupIndex = 1;
      let totalToLearn = 0;
      let historyCount = 0;
      let startTime = null;

      // DOM
      const dom = {{
        yearSelect: document.getElementById('mYearSelect'),
        sectionSelect: document.getElementById('mSectionSelect'),
        countBadge: document.getElementById('mCountBadge'),
        orderShuffle: document.getElementById('mOrderShuffle'),
        orderSequence: document.getElementById('mOrderSequence'),
        labelShuffle: document.getElementById('mLabelShuffle'),
        labelSequence: document.getElementById('mLabelSequence'),
        autoSpeakCheck: document.getElementById('mAutoSpeakCheck'),
        startBtn: document.getElementById('mStartBtn'),
        setupCard: document.getElementById('mSetupCard'),
        reciteView: document.getElementById('mReciteView'),
        celebrateView: document.getElementById('mCelebrateView'),
        groupBadge: document.getElementById('mGroupBadge'),
        numRemembered: document.getElementById('mNumRemembered'),
        numRemaining: document.getElementById('mNumRemaining'),
        progressBar: document.getElementById('mProgressBar'),
        wordCard: document.getElementById('mWordCard'),
        tagYear: document.getElementById('mTagYear'),
        tagSection: document.getElementById('mTagSection'),
        tagOrderMode: document.getElementById('mTagOrderMode'),
        wordTitle: document.getElementById('mWordTitle'),
        speakBtn: document.getElementById('mSpeakBtn'),
        answerBox: document.getElementById('mAnswerBox'),
        answerPos: document.getElementById('mAnswerPos'),
        answerTrans: document.getElementById('mAnswerTrans'),
        answerSub: document.getElementById('mAnswerSub'),
        actionsQuestion: document.getElementById('mActionsQuestion'),
        actionsAnswerRemember: document.getElementById('mActionsAnswerRemember'),
        actionsAnswerForgot: document.getElementById('mActionsAnswerForgot'),
        btnRemember: document.getElementById('mBtnRemember'),
        btnForgot: document.getElementById('mBtnForgot'),
        btnMistake: document.getElementById('mBtnMistake'),
        btnConfirmOk: document.getElementById('mBtnConfirmOk'),
        btnNextReview: document.getElementById('mBtnNextReview'),
        summaryModal: document.getElementById('mSummaryModal'),
        summaryTitle: document.getElementById('mSummaryTitle'),
        summaryList: document.getElementById('mSummaryList'),
        summaryContinueBtn: document.getElementById('mSummaryContinueBtn'),
        cStatTotal: document.getElementById('mCStatTotal'),
        cStatAccuracy: document.getElementById('mCStatAccuracy'),
        cStatTime: document.getElementById('mCStatTime'),
        btnRestart: document.getElementById('mBtnRestart'),
        btnBackSetup: document.getElementById('mBtnBackSetup'),
        searchModal: document.getElementById('mSearchModal'),
        searchInput: document.getElementById('mSearchInput'),
        searchList: document.getElementById('mSearchList'),
        searchBtn: document.getElementById('mSearchBtn'),
        closeSearchBtn: document.getElementById('mCloseSearchBtn'),
        themeBtn: document.getElementById('mThemeBtn')
      }};

      function init() {{
        populateSelectors();
        updateCount();
        bindEvents();
        initTheme();
      }}

      function populateSelectors() {{
        const years = Array.from(new Set(ALL_WORDS.map(w => w.year))).sort((a,b) => b-a);
        dom.yearSelect.innerHTML = '<option value="all">全部年份 (2010-2026)</option>';
        years.forEach(y => {{
          const opt = document.createElement('option');
          opt.value = y;
          opt.textContent = `${{y}} 年`;
          dom.yearSelect.appendChild(opt);
        }});
        updateSectionOptions();
      }}

      function updateSectionOptions() {{
        const selectedYear = dom.yearSelect.value;
        let list = ALL_WORDS;
        if (selectedYear !== 'all') {{
          list = ALL_WORDS.filter(w => w.year === parseInt(selectedYear));
        }}
        const sections = Array.from(new Set(list.map(w => w.section)));
        const standardOrder = ['完形填空', '传统阅读 Text 1', '传统阅读 Text 2', '传统阅读 Text 3', '传统阅读 Text 4', '新题型', '翻译与写作'];
        sections.sort((a, b) => (standardOrder.indexOf(a) === -1 ? 99 : standardOrder.indexOf(a)) - (standardOrder.indexOf(b) === -1 ? 99 : standardOrder.indexOf(b)));
        
        dom.sectionSelect.innerHTML = '<option value="all">全部篇章 / 题型</option>';
        sections.forEach(sec => {{
          const opt = document.createElement('option');
          opt.value = sec;
          const count = list.filter(w => w.section === sec).length;
          opt.textContent = `${{sec}} (${{count}}词)`;
          dom.sectionSelect.appendChild(opt);
        }});
      }}

      function getFilteredList() {{
        const y = dom.yearSelect.value;
        const s = dom.sectionSelect.value;
        return ALL_WORDS.filter(w => {{
          const matchYear = (y === 'all') || (w.year === parseInt(y));
          const matchSec = (s === 'all') || (w.section === s);
          return matchYear && matchSec;
        }});
      }}

      function updateCount() {{
        const count = getFilteredList().length;
        dom.countBadge.textContent = `${{count}} 词`;
      }}

      function bindEvents() {{
        dom.yearSelect.addEventListener('change', () => {{
          updateSectionOptions();
          updateCount();
        }});
        dom.sectionSelect.addEventListener('change', updateCount);

        dom.startBtn.addEventListener('click', startRecitation);

        // 顺序/乱序切换
        const orderRadios = document.querySelectorAll('input[name="mOrderMode"]');
        orderRadios.forEach(radio => {{
          radio.addEventListener('change', () => {{
            const isShuffle = dom.orderShuffle ? dom.orderShuffle.checked : true;
            if (dom.labelShuffle) dom.labelShuffle.classList.toggle('active', isShuffle);
            if (dom.labelSequence) dom.labelSequence.classList.toggle('active', !isShuffle);
          }});
        }});

        // 卡片点击翻转
        dom.wordCard.addEventListener('click', (e) => {{
          if (e.target.closest('#mSpeakBtn')) return;
          if (cardState === 'question') {{
            handleFirstChoice('remember');
          }}
        }});

        dom.btnRemember.addEventListener('click', () => handleFirstChoice('remember'));
        dom.btnForgot.addEventListener('click', () => handleFirstChoice('forgot'));

        dom.btnConfirmOk.addEventListener('click', handleConfirmOk);
        dom.btnMistake.addEventListener('click', handleMistake);
        dom.btnNextReview.addEventListener('click', handleNextReview);

        dom.summaryContinueBtn.addEventListener('click', continueFromSummary);

        dom.speakBtn.addEventListener('click', (e) => {{
          e.stopPropagation();
          speak(currentWord?.word);
        }});

        dom.btnRestart.addEventListener('click', startRecitation);
        dom.btnBackSetup.addEventListener('click', () => {{
          dom.celebrateView.classList.add('hidden');
          dom.reciteView.classList.add('hidden');
          dom.setupCard.classList.remove('hidden');
        }});

        // 检索
        dom.searchBtn.addEventListener('click', () => {{
          dom.searchModal.classList.remove('hidden');
          dom.searchInput.value = '';
          renderSearchList();
          dom.searchInput.focus();
        }});
        dom.closeSearchBtn.addEventListener('click', () => dom.searchModal.classList.add('hidden'));
        dom.searchInput.addEventListener('input', renderSearchList);

        // 主题
        dom.themeBtn.addEventListener('click', toggleTheme);
      }}

      function startRecitation() {{
        const list = getFilteredList();
        if (list.length === 0) return alert('当前没有匹配词汇');

        const isShuffle = dom.orderShuffle ? dom.orderShuffle.checked : false;
        queue = [...list];
        if (isShuffle) {{
          for (let i = queue.length - 1; i > 0; i--) {{
            const j = Math.floor(Math.random() * (i + 1));
            [queue[i], queue[j]] = [queue[j], queue[i]];
          }}
        }}

        rememberedSet = new Set();
        currentGroup = [];
        groupIndex = 1;
        totalToLearn = queue.length;
        historyCount = 0;
        startTime = Date.now();

        dom.setupCard.classList.add('hidden');
        dom.celebrateView.classList.add('hidden');
        dom.reciteView.classList.remove('hidden');

        showNextWord();
      }}

      function showNextWord() {{
        if (queue.length === 0) {{
          finishSession();
          return;
        }}

        currentWord = queue.shift();
        cardState = 'question';
        lastChoice = null;

        updateProgress();

        dom.tagYear.textContent = `${{currentWord.year}} 年`;
        dom.tagSection.textContent = currentWord.section;
        if (dom.tagOrderMode) {{
          const isShuffle = dom.orderShuffle ? dom.orderShuffle.checked : false;
          dom.tagOrderMode.textContent = isShuffle ? '🔀 乱序' : '🔢 顺序';
          dom.tagOrderMode.classList.toggle('seq', !isShuffle);
        }}
        dom.wordTitle.textContent = currentWord.word;

        dom.answerBox.classList.add('hidden');
        dom.actionsQuestion.classList.remove('hidden');
        dom.actionsAnswerRemember.classList.add('hidden');
        dom.actionsAnswerForgot.classList.add('hidden');

        if (dom.autoSpeakCheck.checked) {{
          speak(currentWord.word);
        }}
      }}

      function handleFirstChoice(choice) {{
        if (cardState !== 'question') return;
        cardState = 'answer';
        lastChoice = choice;

        vibrate(15);

        // 展开答案
        dom.answerPos.textContent = currentWord.pos || '释义';
        dom.answerTrans.textContent = currentWord.trans;
        dom.answerSub.textContent = `${{currentWord.section}} · ${{currentWord.category || '核心真题词'}}`;
        dom.answerBox.classList.remove('hidden');

        dom.actionsQuestion.classList.add('hidden');
        if (choice === 'remember') {{
          dom.actionsAnswerRemember.classList.remove('hidden');
          dom.actionsAnswerForgot.classList.add('hidden');
        }} else {{
          dom.actionsAnswerRemember.classList.add('hidden');
          dom.actionsAnswerForgot.classList.remove('hidden');
        }}
      }}

      function handleConfirmOk() {{
        vibrate(15);
        rememberedSet.add(currentWord.id);
        recordResult(true);
        checkGroupOrNext();
      }}

      function handleMistake() {{
        vibrate(40);
        queue.push(currentWord);
        recordResult(false);
        checkGroupOrNext();
      }}

      function handleNextReview() {{
        vibrate(20);
        queue.push(currentWord);
        recordResult(false);
        checkGroupOrNext();
      }}

      function recordResult(ok) {{
        historyCount++;
        currentGroup.push({{
          id: currentWord.id,
          word: currentWord.word,
          pos: currentWord.pos,
          trans: currentWord.trans,
          ok: ok
        }});
      }}

      function checkGroupOrNext() {{
        if (currentGroup.length === 10) {{
          showSummarySheet();
          return;
        }}
        if (queue.length === 0 && currentGroup.length > 0) {{
          showSummarySheet(true);
          return;
        }}
        showNextWord();
      }}

      function showSummarySheet(isEnd = false) {{
        dom.summaryTitle.textContent = isEnd
          ? `📝 第 ${{groupIndex}} 组 (本轮收尾回顾 · ${{currentGroup.length}}词)`
          : `📝 第 ${{groupIndex}} 组完成 (10 词回顾)`;

        dom.summaryList.innerHTML = '';
        currentGroup.forEach((it, idx) => {{
          const div = document.createElement('div');
          div.className = 'summary-item';
          div.innerHTML = `
            <div>
              <div class="sum-word">${{it.word}}</div>
              <div class="sum-trans"><strong style="color:var(--primary);">${{it.pos || ''}}</strong> ${{it.trans}}</div>
            </div>
            <div class="badge-status ${{it.ok ? 'badge-ok' : 'badge-no'}}">
              ${{it.ok ? '已记住' : '待复习'}}
            </div>
          `;
          dom.summaryList.appendChild(div);
        }});

        dom.summaryModal.classList.remove('hidden');
      }}

      function continueFromSummary() {{
        dom.summaryModal.classList.add('hidden');
        currentGroup = [];
        groupIndex++;
        if (queue.length === 0) {{
          finishSession();
        }} else {{
          showNextWord();
        }}
      }}

      function updateProgress() {{
        const rem = rememberedSet.size;
        const total = totalToLearn;
        const remaining = total - rem;
        const pct = Math.min(100, Math.round((rem / total) * 100));

        dom.numRemembered.textContent = rem;
        dom.numRemaining.textContent = remaining;
        dom.groupBadge.textContent = `第 ${{groupIndex}} 组 (${{currentGroup.length}}/10)`;
        dom.progressBar.style.width = `${{pct}}%`;
      }}

      function finishSession() {{
        vibrate([30, 60, 30]);
        dom.reciteView.classList.add('hidden');
        dom.summaryModal.classList.add('hidden');
        dom.celebrateView.classList.remove('hidden');

        const dur = Math.round((Date.now() - startTime) / 1000);
        const m = Math.floor(dur / 60);
        const s = dur % 60;
        dom.cStatTotal.textContent = totalToLearn;
        dom.cStatAccuracy.textContent = `${{Math.round((totalToLearn / Math.max(1, historyCount)) * 100)}}%`;
        dom.cStatTime.textContent = m > 0 ? `${{m}}分${{s}}秒` : `${{s}}秒`;
      }}

      function speak(text) {{
        if (!text || !('speechSynthesis' in window)) return;
        try {{
          window.speechSynthesis.cancel();
          const u = new SpeechSynthesisUtterance(text);
          u.lang = 'en-US';
          u.rate = 0.95;
          window.speechSynthesis.speak(u);
        }} catch (e) {{}}
      }}

      function vibrate(pattern) {{
        if ('vibrate' in navigator) {{
          try {{ navigator.vibrate(pattern); }} catch (e) {{}}
        }}
      }}

      function renderSearchList() {{
        const q = dom.searchInput.value.trim().toLowerCase();
        let list = ALL_WORDS;
        if (q) {{
          list = ALL_WORDS.filter(w => w.word.toLowerCase().includes(q) || w.trans.includes(q) || String(w.year).includes(q));
        }}
        dom.searchList.innerHTML = '';
        list.slice(0, 100).forEach(w => {{
          const div = document.createElement('div');
          div.className = 'summary-item';
          div.innerHTML = `
            <div>
              <div class="sum-word">${{w.word}}</div>
              <div class="sum-trans"><span style="font-size:0.75rem; background:var(--border); padding:1px 5px; border-radius:4px; margin-right:4px;">${{w.year}} ${{w.section}}</span> <strong style="color:var(--primary);">${{w.pos || ''}}</strong> ${{w.trans}}</div>
            </div>
            <button class="h-btn" style="width:32px; height:32px; border-radius:50%;" onclick="window.speechSynthesis && window.speechSynthesis.speak(new SpeechSynthesisUtterance('${{w.word}}'))">🔊</button>
          `;
          dom.searchList.appendChild(div);
        }});
      }}

      function initTheme() {{
        const t = localStorage.getItem('know_mobile_theme') || 'light';
        document.documentElement.setAttribute('data-theme', t);
      }}

      function toggleTheme() {{
        const curr = document.documentElement.getAttribute('data-theme') || 'light';
        const next = curr === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('know_mobile_theme', next);
      }}

      init();
    }})();
  </script>
</body>
</html>'''

mobile_html_path = os.path.join(base_dir, "mobile.html")
with open(mobile_html_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Generated mobile.html successfully! Size: {os.path.getsize(mobile_html_path)} bytes")
