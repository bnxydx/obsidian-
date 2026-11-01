# -*- coding: utf-8 -*-
import json, re

DATA_2015_2014 = []

def add_items(year, section, subcategory, raw_lines):
    for line in raw_lines.strip().split('\n'):
        line = line.strip()
        if not line or line.startswith('【') or line.startswith('第') or line.startswith('Text'):
            continue
        
        match = re.search(r'[\u4e00-\u9fa5（［]', line)
        if match:
            idx = match.start()
            eng_part = line[:idx].strip()
            cn_part = line[idx:].strip()
            
            pos_match = re.search(r'\b(n|v|a|ad|prep|conj|pl)\.?\s*$', eng_part)
            pos = ""
            if pos_match:
                pos = pos_match.group(0).strip('., ')
                eng_word = eng_part[:pos_match.start()].strip()
            else:
                m2 = re.search(r'^(.*?)\s+([a-z]{1,4}[\.,])\s*(.*)$', eng_part)
                if m2:
                    eng_word = m2.group(1).strip()
                    pos = m2.group(2).strip('., ')
                    if m2.group(3).strip():
                        cn_part = m2.group(3).strip() + " " + cn_part
                else:
                    eng_word = eng_part
            
            DATA_2015_2014.append({
                "year": year,
                "section": section,
                "category": subcategory,
                "word": eng_word,
                "pos": pos,
                "trans": cn_part
            })
        else:
            DATA_2015_2014.append({
                "year": year,
                "section": section,
                "category": subcategory,
                "word": line,
                "pos": "",
                "trans": ""
            })

# 2015 完形填空
raw_2015_cloze = """
contemporary a. 当代的
prospect n. 景象，情形
virtually ad. 几乎
unbearable a. 难以忍受的
cling v. 紧紧抓住
interact v. 相互交流
executive coach 高级培训师
rejection n. 拒绝
advance n. （表示愿意友好的）主动姿态
disruptive a. 破坏性的，制造混乱的
inherently a. 固有的，内在的
acquaintance n. 相识
blanket n. 毯子
perceive v. 察觉，认识到
rip off 扯掉，撕掉
band-aid n. 创可贴，绷带
tuck v. 把…塞入
commuter n. 通勤者
unthinkable a. 难以想象的
embarrassed a. 尴尬的
"""
add_items(2015, "完形填空", "核心词汇与搭配", raw_2015_cloze)

# 2015 Text 1
raw_2015_t1 = """
stressed a. 紧张焦虑的，感到有压力的
cortisol n. 皮质醇
marker n. 标记
contradict v. 与…矛盾，反驳，否定
nonparents n. 无子女者
household a. 家庭的；日常的
blurring n. 模糊
gender n. 性别
draw v. （从某来源）得到，取，获取
bargain n. 协议，协定
life-sustaining a. 维持生命的
division n. 分配
clinically ad. 不偏不倚地
methodically ad. 有条不紊地
inadequate a. 不充分的，不适当的
removal n. 移动，搬动
apparently ad. 显然地；似乎
infinite a. 无限的，无穷的，极多的
motivate v. 使有动机，激发…的积极性
contrary to 与…相反，违反
be supposed to be 应该是，被认为是
hold true for 适用于，对…有效
kick back 放松下来；回踢，反弹
leave the office 收工
home front 家庭后方
lag behind 落后，拖欠
make adjustments 作出调整以适应
pretty much 几乎，差不多是
put in 投入
lay out 安排，布置，展示
talk into 说服
"""
add_items(2015, "传统阅读 Text 1", "核心词汇与搭配", raw_2015_t1)

# 2015 Text 2
raw_2015_t2 = """
lag v. 落后（于）
dropout n. 退学，辍学；退学者
paradox n. 自相矛盾的情形，悖论
recruit v. 招收
forthcoming a. 即将到来的
optimistic a. 乐观的
outline v. 概述，勾勒
potential a. 可能的
finding n. 调查发现
recipients n. 接受者
grant n. 助学金，拨款
thesis n. 论点，论题
modest a. 较小的
intervention n. 干预
cite v. 引用
navigate v. 理解，应对
seldom ad. 很少，几乎不
college degree 大学学位
lag sb 落后于某人
a range of 一系列
social class 社会阶层
a potential solution to 解决某一问题的可能方案
next-to-no-cost 接近零成本的，几乎无成本的
financial need 经济需求
a big impact 巨大影响
be lacking in 缺乏…
practical knowledge 实用知识
deal with 处理
struggle to 挣扎于…
middle-class culture 中产阶级文化
take advantage of 利用…
"""
add_items(2015, "传统阅读 Text 2", "核心词汇与搭配", raw_2015_t2)

# 2015 Text 3
raw_2015_t3 = """
lingua franca 通用语、交际语
right-brained a. 右脑的，感性的
spin v. 快速旋转
parachute v. 空降、空投
era n. 时代、年代
male-dominated a. 男性占主导地位的
explicitly ad. 清楚地
infuse v. 把…注入；灌输
allegiance n. （对组织、信仰的）忠诚，拥护
importation n. 引进、输入
terminology n. 学科术语；专门用语
amid prep. 在…中间，在…当中
prompt v. 促进、激起
buzzword n. 某一领域内的时髦用语
office speak 办公语言
linguist n. 语言学家
nonsense n. 无稽之谈、胡说、荒谬的想法
point out 指出
by coincidence 巧合、偶然
a big deal 非常重要的事
be associated with 和…有关联
non-profit organization 非营利性组织
keep sb. motivated 使某人受到激励
personal fulfillment 个人成就、自我实现
in its own right 凭借自身的能力
set boundaries between 在两者之间设置界限
devote yourself to 奉献/投身于某事
buy into it 买账、认可
figure out 弄清楚
"""
add_items(2015, "传统阅读 Text 3", "核心词汇与搭配", raw_2015_t3)

# 2015 Text 4
raw_2015_t4 = """
the Labor Department 劳工部
decent a. 相当好的，不错的
largely ad. 很大程度上
overlook v. 忽略，忽视
voluntarily ad. 自愿地
distinction n. 区别，差别
evidence n. 证据，迹象
recession n. 衰退，不景气
survey n. 调查，研究
reference n. 参考，参照
issue n. 问题，话题
insurance n. 保险
previously ad. 先前的
cover v. 投保，承保
along with 伴随，随同…一起
unemployment rate 失业率
for now 目前看来
at a decent pace 以相当不错的速度
still have a long way to go 还有很长的路要走
full employment 充分就业
jobs picture 就业图景
a big jump in …的突增
voluntarily working part-time 自愿从事兼职工作
the connection to 与…的联系
it's worth doing 值得做某事
make ends meet 收支相抵，维持生计
an increase in …的增加
general direction 总体趋势，大方向
have no choice 别无选择
serious health conditions 有严重健康问题
allow to 允许…成为可能
either... or 或者…或者…
feel the need to 感到…的迫切需要
"""
add_items(2015, "传统阅读 Text 4", "核心词汇与搭配", raw_2015_t4)

# 2015 新题型
raw_2015_new = """
grieve v. 为…而悲伤，感到伤心
inopportune a. 不合时宜的，不是时候的
mourn v. 悲哀，痛惜，忧伤
signal v. 发出…信号，表明
inner a. 内心的，思想的
barrier n. 障碍物，屏障
luxuriant a. 丰富的，过多的
poison v. 败坏，污染，阻碍
mindset n. 心态，思想倾向
design v. 决意，意欲
pause v. 暂停，停顿
isolated a. 孤立的，孤独的
companionship n. 友谊，交情，陪伴
objectivity n. 客观，客观性
external a. 外部的，外界的
devalue v. 降低…的价值，贬低
a bed of roses 轻松安逸的生活
hold down 压制，抑制
press forward 奋力向前，努力前进
along the way 沿途，一路上
weigh down 使负重担
keep the eyes open 睁大眼睛，保持留心
catch up 把…缠住，陷入…
dearest and nearest 最亲密的，最亲近的
circle of friends 朋友圈，交友圈
good humor 高兴，好心情
be incapable of 无能力的，不会的
"""
add_items(2015, "新题型", "核心词汇与搭配", raw_2015_new)

# 2015 翻译与写作
raw_2015_trans_write = """
route n. 路，道路（尤指公路）
perceive v. 发觉，感知
well-travelled a. 经常旅行的；频繁经过的
underestimate v. 低估
allocate v. 分配，派定，配给
assume v. 假定，臆断；承担
know like the back of one's hand 对…了如指掌
twist and turn 迂回曲折
think back 回想
organize v. 组织
cooperation ability 合作能力
practical skills 实践技能
facilitate learning 促进学习
cultivate ability 培养能力
including but not limited to 包括但不限于
business-starting competition 创业大赛
daily affairs 日常事务
ideal candidate 理想人选
relevant experience 相关经验
health n. 健康
coach n. 教练
arrange accommodation 安排食宿
athlete n. 运动员
lodgment n. 住宿
keep in order 维持秩序
spring festival 春节
spending n. 花费、开支
interpersonal communication 人际交往
fulfillment n. 幸福感
extraordinary a. 超凡的
handsome a. 大量的
blindly ad. 盲目地
intention n. 意图
squander v. 挥霍
transient a. 短暂的
rationally ad. 理性地
respective proportions 各自的比例
account for 占
family reunion 家庭团聚
invest on 投资
go to extremes 走向极端
pursue pride 追求面子
heavy economic burden 沉重的经济负担
education spending 教育开支
remedial class 辅导班
tuition n. 学费
training class 培训班
"""
add_items(2015, "翻译与写作", "核心词汇与表达", raw_2015_trans_write)

# 2014 完形填空
raw_2014_cloze = """
overweight a. 体重超常的，超重的
condition n. 健康状况，健康
develop v. 患（某种疾病）
deficiency n. 缺乏，不足；缺乏症
the elderly n. 老年人，上岁数的人
obesity n. 肥胖，过度肥胖
mass n. （物体的）质量
divide v. 除，除以
square n. （某数值的）平方
moderately ad. 适度地，不过分地
numerical a. 数字的，以数字表示的
fit a. 健康的，健壮的
collegiate a. 学院的，学院学生的
conversely ad. 相反地，以相反的方式
frame n. （人或动物的）身体，体形
disgrace n. 耻辱，丢脸的事；出丑
stereotype n. 陈词滥调，刻板印象
prospect n. 前景，可能性
harbor v. 心怀，怀有（某想法等）
tease v. 取笑，嘲弄，招惹
build n. （人体的）体形，体格
negative a. 否定的，消极的
stimulate v. 刺激，促进
ban v. 明令禁止
facility n. （供特定用途的）场所
institute v. 建立，制定（习俗、规则等）
initiative n. 新倡议、行动、方案
launch v. 推出，使开始
campaign n. 运动（有计划的一系列活动）
"""
add_items(2014, "完形填空", "核心词汇与搭配", raw_2014_cloze)

# 2014 Text 1
raw_2014_t1 = """
widow n. 寡妇；孀妇
emerge v. 开始被认知
tin-roofed a. 铁皮房顶的
undivided a. 未分开的；完整的
lottery n. 彩票
jackpot n. 头奖；最高奖
fortune n. 财富
yield v. 产生；生产
lasting a. 持久的
fulfillment n. 满足感
academic n. 高校老师；科研人员
rewarding a. 有益的；值得的
counterintuitive a. 违反直觉的
fantasy n. 幻想；白日梦
vision n. 想象；幻想
fancy a. 昂贵的；精致的
extravagant a. 奢侈的
commute n. 通勤；上下班路程
whopping a. 巨大的；很大的
sparingly ad. 节俭地；慎用地；爱惜地
privileged a. 荣幸的，幸运的
scarcity n. 不足；缺乏
mandate v. 批准；授权
incentive n. 激励
emerge from 从…走出来；摆脱…
the biggest in history 史上最大
new-found fortune 新到手财富
could do worse than 不妨试试…
an array of 一系列
wear off fairly quickly 很快消失殆尽
creep in 悄然而至
it is far better to do 做…则要好许多
be packed with 挤满；塞满
wage slave 薪奴，靠工资吃饭的人
bang for your buck 努力值得；钱花得合算
be better off 过得更好
restrict the availability of 限制对…的获取
an object of obsession 令人痴迷之物
a privileged lot 特权群体；幸运群体
come away 离开时留下（印象）
"""
add_items(2014, "传统阅读 Text 1", "核心词汇与搭配", raw_2014_t1)

# 2014 Text 2
raw_2014_t2 = """
empirical a. 以实验（或经验）为依据的
deep-seated a. 深层的；根深蒂固的
employ v. 使用，采用
self-enhancing a. 自我提升、自我加强的
psychologist n. 心理学家
amass v. 聚集（尤指大量）
illusory a. 错觉的；虚假的
superiority n. 优越感
rose-tint v. 染了玫瑰色，精饰、美化
defensive a. 自卫的；戒备的
stereotype n. （不合理的）刻板印象
boost v. 促进；增加；增强
esteem n. 尊重；尊敬
stalk v. 高视阔步地走
oversee v. 监督；监管
self-enhancement n. 自我强化、自我拔高
identify v. 确定；识别，辨认出
lineup n. 阵容；一组
deliberation n. 考虑；熟思
flattering a. 使人显得更漂亮的；讨好的
genuinely ad. 真诚地；诚实地
doctor v. 篡改，伪造
profound a. 深刻的；极大的；严重的
delusion n. 错觉；谬见；妄想
depressed a. 沮丧的；压抑的
viscerally ad. 发自肺腑地
wit n. 风趣
intellect n. 智力，非凡的才智
profile n. 印象，形象
portray v. 描绘
idealise v. 把…理想化
feel good about oneself 自我感觉良好
oceans of 海量的，极大量的
above-average effect 高于平均效应
rate as 把…评估为…
get on well with others 与他人相处融洽
hot stuff 奇才；非凡的人物
visual recognition 面部识别
conscious deliberation 刻意的深思熟虑
make up for 弥补
correspond with 符合，一致
think well of 赞赏；对…有好感
make sense 有意义；讲得通
the cream of …的精华部分
"""
add_items(2014, "传统阅读 Text 2", "核心词汇与搭配", raw_2014_t2)

# 2014 Text 3
raw_2014_t3 = """
acutely ad. 剧烈地，强烈地
fragile a. 不牢固的，脆弱的
recovery n. 复苏；恢复
outmoded v. 使…过时；使…不流行
insatiable a. 贪得无厌的；不知足的
foresee v. 预见；预知
performance n. 性能；绩效；表现状况
immune a. 免疫的
scary a. 可怕的；提心吊胆的
vulnerable a. 易受攻击的；有弱点的
scripted a. 脚本化的；照书面稿念的
standardized a. 标准的；标准化的
initiative n. 主动权；首创精神
reinvent v. 彻底改造
formula n. 方案，方法
conduct v. 执行；实施
notion n. 概念；见解
unexpected a. 意外的，想不到的
predictable a. 可预见的
note v. 指出；特别提到
reframe v. 重新组织
augment v. 增加；增大
innovate v. 改变；改革；创新
institution n. 制度，风俗习惯
man versus machine 人机矛盾
economic downturn 经济下滑
boom and bust cycle 繁荣与萧条循环
eat up 吃光，吞噬
restructure economy 重构经济
hail from 来自
individual initiative 个人主动性
perform much better at 更擅长
exercise one's imagination 运用想象力
"""
add_items(2014, "传统阅读 Text 3", "核心词汇与搭配", raw_2014_t3)

# 2014 Text 4
raw_2014_t4 = """
infrastructure n. 基础设施
broadband n. 宽带
housing n. 住宅，住房
seldom ad. 很少，不常
shoulder v. 肩负，承担
shove v. 挤；撞；猛推
inevitable a. 必然的，不可避免地
charged v. 命令，吩咐
nevertheless conj. 然而，不过
affordable a. 负担得起的
desperate a. 危急的，严峻的
comprehensive a. 综合的，全部的，详尽的
review n. 审核；审查
rectify v. 改正，纠正
prejudice n. 偏见
address v. 设法解决；处理；应付
urgent a. 紧急的；急迫的
indication n. 迹象
hint v. 暗示；示意
introduce v. 引进，推行，实施
flexibility n. 灵活性；弹性
cap n. 最高限额
authorities n. 当局，官方
lift v. 提高
registered a. 注册的，登记在册的
revenue n. 国家的收入；岁入
grant n. 拨款
expire v. 期满；终止
retain v. 保持，保留
coalition n. 联合；联盟
commitment n. 承诺
long-term a. 长期的
pressing a. 迫切的
shoulder the blame 承担过失
real value 真实价值
multibillion-pound infrastructure 数十亿磅基础设施
waiting list 候补名单
spending review 开支审查
take some steps 采取一些措施
address urgent housing need 解决紧迫住房需求
registered provider 注册供应者
be down to sb 是某人的责任
"""
add_items(2014, "传统阅读 Text 4", "核心词汇与搭配", raw_2014_t4)

# 2014 新题型
raw_2014_new = """
confines n. 范围，界限，边界
studio n. 工作室
gallery n. 画廊，陈列室，展览馆
substance n. 物质
medium n. （文艺创作中使用的）材料，形式
typify v. 代表；作为…的典型
scale v. 按比例绘制、制作
quirky a. 古怪的
counterpart n. 对应的人或物
sole a. 唯一的，单独的，仅有的
embodiment n. 体现，具体化
obscure a. 费解的，难以理解的
set the tone for 奠定基调
purplish a. 略带紫色的
lay out 展示，安排，布置
rarefied a. 高妙精深的；曲高和寡的
comprise v. 包含，包括，由…组成
brick-strewn a. 堆满砖头的
embrace v. 囊括，涉及
commonplaceness n. 普通平凡
characterise v. 是…的特征
feature v. 起重要作用
stroller n. 散步者；流浪者
unwittingly ad. 不知不觉地；不知情地
assault v. 攻击；袭击
gravitate v. 被吸引到，受吸引而转向
permeate v. 渗透，弥漫
escapism n. 逃避现实，逃避主义
the likes of 像这样的人或事
readily ad. 轻而易举地，快捷地
still shot 固定镜头
evoke v. 引起，唤起
make sth. pay 受益，赢利，得到回报
epic a. 史诗般的，漫长而艰难的
modestly ad. 谨慎地；适当地
impose on 利用，施加影响于
landscape-orientated a. 以风景为中心展开的
conceptual a. 概念上的
gallery-bound a. 适合在画廊展出的
"""
add_items(2014, "新题型", "核心词汇与搭配", raw_2014_new)

# 2014 翻译与写作
raw_2014_trans_write = """
define v. 定义，使明确，规定
optimism n. 乐观；乐观主义
perpetually ad. 永恒地，持久地
cheerfulness n. 高兴；快活
psychologist n. 心理学家，心理学者
recommend v. 推荐，介绍；劝告，建议
make the best of 充分利用；尽力而为
grant v. 授予，同意，准予，允许
permission n. 允许，许可
reconstruction n. 再现，重现
perspective n. 角度，观点，想法
involve v. 包含，需要，涉及到
acknowledge v. 承认（属实）
scheme n. 计划，方案，体系，体制
roommate n. 室友
living habit 生活习惯
observe living rules 遵守生活规范
overseas study 留学
arrive at understanding 对…有基本了解
gorgeous a. 极好的
humble a. 简单的、粗陋的
tidy and clean 整洁干净
tolerance n. 容忍
dish preparation 准备饭菜
have balanced diet 平衡饮食
love sports 热爱运动
have timely relaxation 及时休息
stay up late 熬夜
omit breakfast 不吃早饭
lack exercises 缺乏锻炼
be addicted to Internet 沉迷网络
design work schedule 制定工作计划
peer edit 互相审核
new perspective 崭新视角
bar graph 柱状图
urban population 城市人口
rural population 农村人口
demographic change 人口变化
moderate a. 温和的、不剧烈的
considerably ad. 可观地
narrow v. 缩小
urbanization n. 城市化
transform v. 变化
flock v. 涌向
integration n. 融合
population distribution 人口分布
dramatic shift 巨大变化
skyscraper n. 摩天大楼
mobile urban resident 城市流动人口
rural migrant 农村移民
social tension 社会冲突
desktop n. 桌面
mobile n. 移动端
advertising revenue 广告收入
"""
add_items(2014, "翻译与写作", "核心词汇与表达", raw_2014_trans_write)

with open(r'f:\obsidiannote\obsidian-\408\数据结构\考研英语二核心词背诵\data_generators\data_2015_2014.json', 'w', encoding='utf-8') as f:
    json.dump(DATA_2015_2014, f, ensure_ascii=False, indent=2)

print('Generated 2015 & 2014 items count:', len(DATA_2015_2014))
