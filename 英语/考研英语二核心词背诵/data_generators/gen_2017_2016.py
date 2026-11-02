# -*- coding: utf-8 -*-
import json, re

DATA_2017_2016 = []

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
            
            DATA_2017_2016.append({
                "year": year,
                "section": section,
                "category": subcategory,
                "word": eng_word,
                "pos": pos,
                "trans": cn_part
            })
        else:
            DATA_2017_2016.append({
                "year": year,
                "section": section,
                "category": subcategory,
                "word": line,
                "pos": "",
                "trans": ""
            })

# 2017 完形填空
raw_2017_cloze = """
speculate v. 推测
capital n. 资本
the masses 普通百姓
struggle v. 奋斗；挣扎
impoverished a. 穷困的
wasteland n. 荒地，不毛之地
mutually exclusive 互相排斥
purposelessness n. 无目的
Gallup poll 盖洛普民意调查
mortality n. 死亡人数
agonizing a. 痛苦难忍的
dullness n. 沉闷，无聊
follow from 是…的必然结果
unease n. 不安
vision n. 憧憬，想象
design v. 设计
end n. 目的
strikingly ad. 显著地，引人注目地
circumstance n. 情形
overblow v. 夸张，过分渲染
degrading a. 丧失体面的
leisure time 空闲时间
relatively ad. 相对地，比较地
counterbalance v. 使平衡，抵消
intellectual a. 智力的
hobby n. 业余爱好
passion n. 强烈的爱好，热爱
"""
add_items(2017, "完形填空", "核心词汇与搭配", raw_2017_cloze)

# 2017 Text 1
raw_2017_t1 = """
inspire v. 激发，引起
event n. 体育比赛，体育活动
staff v. 为…配备工作人员，在…工作
time n. 所用的时间，成绩
pledge v. 发誓，保证
legacy n. 遗产
lever v. （用杠杆）撬动
couch n. 沙发
fit a. 健壮的，强健的
obesity n. 肥胖症
retrospection n. 回想，反思
ethos n. 精神特质，理念
shine v. 干得出色，出类拔萃
bidder n. 投标人
dual a. 双重的
intimidating a. 令人胆怯的
grassroots n. 基层民众，草根
successive a. 连续的
decline v. 拒绝
wordy a. 冗长的，啰嗦的
worthy a. 有价值的，值得尊敬的
set off 出发，启程
range from... to... 包括从…到…
in the run-up to 重要事件的前夕
as to 关于
fail to do 未能完成某事
time trial 计时赛
puffed-out a. 气喘吁吁的
first-timer n. 初次做某事者
Olympic bidder 奥运申办者
stress on A over B 强调A胜过B
get involved in 参与，卷入
common goods 公共产品，公共资源
make sure 确保
preside over 主持，掌管…
at least 至少，起码
"""
add_items(2017, "传统阅读 Text 1", "核心词汇与搭配", raw_2017_t1)

# 2017 Text 2
raw_2017_t2 = """
screen n. 屏幕（指代数字产品）
maximal a. 最大的，最高的
engagement n. 参与度
disengage v. 脱离，不再感兴趣
bleed-over n. 渗透，渗开
tablet n. 平板电脑
exercise n. 活动，任务
verbal a. 文字的，言语的
interaction n. 交流；相互作用
tension n. 紧张关系，紧张状况
bid n. 努力，企图，争取
blank a. 没表情的，不感兴趣的
unresponsive a. 反应迟钝的
disconcerting a. 使人不安的
distressed a. 痛苦的，悲伤的，苦恼的
exquisitely ad. 精致地，近乎完美地
present a. 在场的，存在的
sensitive a. 体恤的，善解人意的
oppressive a. 压制的，令人焦虑的
fantasized a. 想象的，幻想的
available a. 有空的，有暇的
attentive a. 专心的，留意的
be designed to 为…而设计，目的是…
suck in 把某人卷入，吸引某人
be wired to do 天生，自然就会
be absorbed in 全神贯注于…，专注于…
put on a... expression 做出/装出某一表情
capture one's attention 吸引某人的注意力
be born out of 因…而产生
expose sb. to sth 使某人接触/体验某事物
get a lot out of 从…中获益良多
get sth. out of the way 把某事处理完
"""
add_items(2017, "传统阅读 Text 2", "核心词汇与搭配", raw_2017_t2)

# 2017 Text 3
raw_2017_t3 = """
conjunction n. （事物等的）结合，同时发生
overlook v. 忽略，未注意到
gap year 间隔年
fall n. 秋天
academic a. 学业的，教学的，学术的
condemn v. 谴责
perpetuate v. 使永久化，使持续
finish line 终点线
graduate school 研究生院
medical school 医学院
lucrative a. 赚大钱的，获利多的
misconception n. 错误认识，误解
hinder v. 阻碍，妨碍，阻挡
pursuit n. 事业，消遣，爱好
enhance v. 提高，增强，增进
lessen v. 减弱，减轻
brand new 全新的，崭新的
acclimation n. 适应
blunder n. 愚蠢（或粗心的）错误
inherent a. 固有的，内在的
major n. 主修课程，专业课
mandatory a. 强制的，法定的，义务的
curriculum n. 全部课程
await v. 将发生在，将降临到
switch v. （尤指突然彻底的）改变
costly a. 昂贵的
credit n. 学分
game n. 活动，行业
nursing n. 护理
pull back 把…向后拉，使后退
push ahead 促进，推进
struggle with 与…斗争、抗争
cushion the blow 缓解，缓和
throw into 使突然陷入某种状态
be convinced of 确信，认识到
take sth. off 休假，休息
make up 补上（失去的东西）；补修
figure out 弄懂，弄清楚，弄明白
"""
add_items(2017, "传统阅读 Text 3", "核心词汇与搭配", raw_2017_t3)

# 2017 Text 4
raw_2017_t4 = """
wildfire n. 不易扑灭的大火，野火
specialist n. 专家
ecology n. 生态，生态学
budget n. 预算
fund n. 基金，专款
conservation n. 保护
watershed n. （森林地带的）集水区
infrastructure n. 基础设施
upkeep n. 保养，维修
nationwide a. 全国范围的，全国性的
prone a. 易于发生某事的；很可能…的
expenditure n. 开支，支出
magnify v. 放大
redirect v. 使改变用途，重新使用
concentrate v. 使集中于，使汇聚于
hazard n. 危险，隐患
landscape n. 地形，地貌
corresponding a. 相应的，由此引起的
shift n. （想法、做法等的）转变，改变
inclusive a. 包容广阔的，范围广的
worsen v. （使）变得更差，（使）恶化
equation n. 影响因素，综合体
interaction n. 相互作用，相互影响
simplified a. 简化的
perception n. 认识，观念，看法
unleash v. 发泄，突然释放，使爆发
necessity n. 必然，必要
acknowledge v. 承认
inevitable a. 必然发生的，难以避免的
presence n. 存在，出现
disconnect v. 使分离，使脱离
tease v. 梳理
be viewed as 被视为…，被看作…
in effect 事实上，实际上
forest conservation 森林保护
infrastructure upkeep 基础设施养护
public expenditure 公共支出
magnifying glass 放大镜
greenhouse gases 温室气体
key element 关键要素
at the expense of 以…为代价
tease out 梳理，疏通
"""
add_items(2017, "传统阅读 Text 4", "核心词汇与搭配", raw_2017_t4)

# 2017 新题型
raw_2017_new = """
manufacturing n. 制造业
refrain n. 老调，一再重复的话
outsourcing n. 外包
replace v. 以…替换、更换
boomer n. 婴儿潮一代
Millennial n. 千禧一代
stiff a. 激烈的，严厉的
wage n. 工资
workforce n. 劳动力
pluck v. 拖，拉，扯
junior n. （大学）三年级学生
enroll v. 招（生），吸收（成员）
worktable n. 工作台
flustered a. 紧张的，慌乱的，激动的
assemble v. 装配，组装
recession n. （经济）衰退，萧条
concern n. 忧虑，担心
misplaced a. （把感情等）寄托于不当对象上的
shortage n. 短缺
trade n. 行业，职业
gap n. 缺口
lure v. 吸引
content a. 满足的，甘愿的
flexibility n. 灵活性
overtime n. 加班时间，额外工作时间
take a hit 遭到打击，被击中
trade deal 贸易协定
raise question 提出/提起…的问题
grapple with 尽力解决（某困难问题）
end up with 最终处于…
trade competition 贸易竞争
take sb's place 代替，取代
add up to 引发
get exposed to 接触，体验
keep an eye on 密切注意
switch to 转变，改变
electrical engineering 电气工程
win over 把（某人）争取过来
clear a hurdle 成功克服困难
live through 经历（艰难或险境）
economic downturn 经济衰退
be laid off 被辞退
blame sth. on 把…归咎于
work/life balance 工作-生活平衡
"""
add_items(2017, "新题型", "核心词汇与搭配", raw_2017_new)

# 2017 翻译与写作
raw_2017_trans_write = """
sewing n. 缝纫
personality n. 有突出个性的人
apply v. 申请
promotion n. 推广
graduate from 从…毕业
move on to 继续某事，接着做某事
fashion design 时装设计
compete with 与…竞争
to be honest 说实话
not... at all 完全不，根本不
invitation n. 邀请
presentation n. 讲座
Chinese culture 中国文化
martial arts 武术
component n. 组成部分
furthermore ad. 此外
graphic a. 图画的
visual a. 视觉的
impressive a. 给人印象深刻的
to begin with 首先
annual growth 年度增长
continuous increase 持续增加
line chart 折线图
visit museums 参观博物馆
cultural infrastructure 文化基础设施
public cultural undertaking 公共文化事业
slowdown n. 减速
dynamic momentum 强劲增长的势头
be attributed to 归因于…
endeavor n. 努力
underpin v. 构成…的基础
spiritual nutrition 精神食粮，精神营养
supply deficiency 供应不足，供不应求
decelerated growth 增长放缓
increasingly diverse need 日益多样化的需求
mobile and digital technology 移动数字技术
people's well-being 人民福祉
civilization n. 文明
cultural exchange 文化交流
grassroots culture 草根文化
cultural troupe 文化团体
renaissance n. 复兴
yield good results 取得良好的成效
e-learning n. 在线学习
underpin social progress 作为社会进步的基础
"""
add_items(2017, "翻译与写作", "核心词汇与表达", raw_2017_trans_write)

# 2016 完形填空
raw_2016_cloze = """
productive a. 多产的、富饶的
take risk 冒险
locate v. 把…设置/建造在
inclination n. 意向、倾向
compare with 将…和…相互比较
polling n. 民意测验
publicly traded firms 上市公司
sure enough 果然、果真
intensity n. 强度、力度
correlate v. 使相互关联
control for 考虑（某种因素）
indicators n. 指示物，指标
accounting for 作出解释，作出说明
codified a. 编辑成典的；固守成规的
sentiment n. 情感、情绪
relatively ad. 比较而言地，相对地
take a longer-term view 采取更加长远的眼光
plausible a. 有道理的、可信的
forward-thinking a. 前瞻的、有远见的
"""
add_items(2016, "完形填空", "核心词汇与搭配", raw_2016_cloze)

# 2016 Text 1
raw_2016_t1 = """
coding n. 编码，编程
essential a. 必不可少的
catch up 赶上，追上
introductory a. 入门的，初步的
course n. 课程
assistant dean （学院）副院长
exposure n. 接触，体验（新事物）
beneficial a. 有利的，有用的
confusing a. 令人困惑的，难懂的
string n. 一连串，一系列
artwork n. 艺术作品
hypothesis n. 假设，假说
transform v. 转换，（彻底）改变
break down 拆分
bite-sized a. 很小的
chunk n. 大块
jobs gap 职位空缺
pack v. 塞满，挤满
brim n. 口，边沿
determined a. 有决心的，意志坚定的
drive away 赶跑，使离去
start v. 开办，创办
bootcamp n. 训练营
curriculum n. 课程
gear v. 使与…相适应；使适合于
instructor n. 讲师
be based on 根据…
drop out 退学，辍学
turnover n. 倾覆、翻转
relevant a. 紧密相关的；切题的
consultant n. 顾问
sole a. 唯一的，仅有的
coax v. 劝诱，哄劝
"""
add_items(2016, "传统阅读 Text 1", "核心词汇与搭配", raw_2016_t1)

# 2016 Text 2
raw_2016_t2 = """
estimate v. 估计，估算
prairie n. （北美洲）大草原
stretch v. 延伸、绵延
occupy v. 占据，居住
range n. 生长区，分布区
crash n. 暴跌，猛跌
desperate a. 危急的，严峻的
environmentalist n. 环保人士
designate v. 指定，认定
endangered a. 濒临灭绝的
tag n. 标签，标志
flexibility n. 灵活性
confrontational a. 对抗性的，挑起冲突的
conservation n. 保护
approach n. 方法，方式
forge v. 形成，缔造
collaboration n. 合作，协作
uneasy a. 不和谐的，不协调的，矛盾的
habitat n. （动植物的）生活环境，栖息地
prosecute v. 起诉，控告，检举
unintentionally ad. 非故意地
restore v. 恢复，复原
acre n. 英亩
compensate v. 弥补，补偿
interim a. 临时的，暂时的，过渡期间的
coalition n. 联盟，联合体
monitor v. 监控，监督
rhetoric n. 华而不实的言语，花言巧语
block v. 阻止，妨碍，阻挠
challenge v. 质疑；拒绝接受
extinction n. 灭绝，绝种
as many as 多达…
lend to 给…增添
crack down on 严厉打击，镇压
try out 试，试验
call for 要求，呼吁
replace A with B 以A替代B
set aside 留出，省出
set a goal 制定目标
in the driver's seat 处于控制地位、主导地位
win-win rhetoric 双赢说辞
go too far 走得太远，做得过分
"""
add_items(2016, "传统阅读 Text 2", "核心词汇与搭配", raw_2016_t2)

# 2016 Text 3
raw_2016_t3 = """
cliché n. 陈词滥调，老生常谈
mournfully ad. 悲哀地，凄惨地
thorny a. 棘手的
odd a. 少量的，微小的；零散的
flywheel n. 飞轮，惯性轮
spin v. 旋转，转动
exhausted a. 精疲力竭的
overwhelmingly ad. 势不可挡地
incline v. 使倾向于
interrupt v. 打断
merely ad. 仅仅
maximise v. 充分利用
approach v. 对待，处理
instrumentally ad. 起作用地，有帮助地
advance v. 促进，推动
immersive a. 沉浸式的
fulfilling a. 让人感到满足的
infinite a. 无限的；极多的
conveyor belt 传送带
mind-set n. 思想倾向
schedule v. 安排，计划
fuel v. 刺激；使加剧
ritualistic a. 仪式的；例行的
soul n. 灵魂
distraction n. 使人分心的事物
providing conj. 以…为条件；如果
dip v. 浸，蘸
default a. 默认的
free up 腾出；使…可用
by contrast 相比之下
slot in 安置，安排
to-do list 任务清单
no longer 不再
"""
add_items(2016, "传统阅读 Text 3", "核心词汇与搭配", raw_2016_t3)

# 2016 Text 4
raw_2016_t4 = """
backdrop n. 背景
poll n. 民意调查，民意测验
prize v. 珍视，高度重视
milestone n. 重大事件，里程碑
constitute v. 构成
fulfilling a. 令人满意的
strikingly ad. 惹人注目地；醒目地
start v. 开始生活，开始立业
prioritize v. 确定优先顺序；优先考虑
advance v. 前进，推进
maintain v. 主张；坚持认为
serve v. 为…提供服务；满足…的需要
contrast n. 差别，差异
aftermath n. 后果，余波
searing a. 炽热的，灼痛的
the Great Recession 大衰退
define v. 给…下定义，解释；界定
virtually ad. 实际上，几乎
converge v. （观点、目标）趋同
overwhelming a. 巨大的，压倒性的
somewhat ad. 有点儿，有几分
optimistic a. 乐观的，乐观主义的
prospect n. 可能性；机会；希望；前景
climb n. 上升；晋升；提高
signpost n. 路标；标志物
secure v. 获得，取得，实现
technician n. 技师，技术人员
struggle v. 奋斗，拼搏
steadily ad. 稳定地，稳固地
mortgage n. 抵押贷款，按揭
against a backdrop of 在…背景下
population structure 人口结构
draw a road map to success 绘制一幅成功路线图
personal fulfillment 个人满足感
financially secure 有经济保障
consumer preference 消费者偏好
housing pattern 居住模式
"""
add_items(2016, "传统阅读 Text 4", "核心词汇与搭配", raw_2016_t4)

# 2016 新题型
raw_2016_new = """
mixed a. 混杂的
therapy n. 治疗，疗法
wellbeing n. 幸福
instinctively ad. 本能地
manageable a. 易控制的，易管理的
dictate v. 影响，决定，支配
suppress v. 抑制（感情）
acknowledge v. 承认
fiver n. 五元美钞
overjoyed a. 极为高兴的，十分开心的
indulge v. 沉溺于，沉湎于，纵情于
giggle v. 傻笑
endorphin n. 内啡肽
infection n. 传染病
diary n. 工作日程登记表
spree n. 作乐，狂欢
backfire v. 产生事与愿违的结果
byproduct n. 意外收获，附带的结果
have sth. down to a fine art 把某事做得很出色/精巧
for the most part 多半，在很大程度上
take sth. too far 将某事做得太过
end up doing 最终处于…
brush under the carpet 掩盖某事
move on 继续向前
silver bullet 解决某一难题的良方
fight off 抵挡，击退，竭力摆脱
an awful lot of 许多，多得可怕的
have the luxury of 难得能享受某种机会
side effect 副作用
"""
add_items(2016, "新题型", "核心词汇与搭配", raw_2016_new)

# 2016 翻译与写作
raw_2016_trans_write = """
lure v. 引诱，诱使
carry v. 备有（货物）供销售
item n. 商品（物品），货品
sheer a. 十足的，彻底的，纯粹的
overload n. 超载，超负荷
demand n. 困难的事情，要求
rationally ad. 理性地
selective a. 认真挑选的
accumulate v. 堆积，聚集
gratitude n. 谢意
suggestion n. 建议
appreciate v. 欣赏
hone skill 打磨，锤炼
read extensively 广泛阅读，博览群书
expose oneself to 让自己接触…
broad knowledge base 广泛的知识基础
keep abreast of 了解…的最新情况
sustained efforts 长期不懈的努力
public speaking skill 公共演讲技能
eloquence n. 流利的口才
conquer fear 战胜恐惧心理
proper training 正确的训练方法
foster independence 培养独立能力
see the world 见世面，见多识广
antidote to pressure 抗压良方
benefit v. 使人受益
illuminating a. 有启发性的
foster v. 培养，促进
unwind v. 使松弛，放松
recharge v. 放松休息，恢复精力
ample a. 足够的，充足的
refreshed a. 恢复精神的
revitalized a. 焕发生机的
relieve pressure 舒缓压力
come into contact with 接触到，遭到
attach meaning to 对…赋予意义
lack of practical ability 专业实践能力不足
lack of communication skills 沟通交际能力不足
"""
add_items(2016, "翻译与写作", "核心词汇与表达", raw_2016_trans_write)

with open(r'f:\obsidiannote\obsidian-\408\数据结构\考研英语二核心词背诵\data_generators\data_2017_2016.json', 'w', encoding='utf-8') as f:
    json.dump(DATA_2017_2016, f, ensure_ascii=False, indent=2)

print('Generated 2017 & 2016 items count:', len(DATA_2017_2016))
