# -*- coding: utf-8 -*-
import json, re

DATA_2013_2012 = []

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
            
            DATA_2013_2012.append({
                "year": year,
                "section": section,
                "category": subcategory,
                "word": eng_word,
                "pos": pos,
                "trans": cn_part
            })
        else:
            DATA_2013_2012.append({
                "year": year,
                "section": section,
                "category": subcategory,
                "word": line,
                "pos": "",
                "trans": ""
            })

# 2013 完形填空
raw_2013_cloze = """
given prep. 考虑到，鉴于（表示原因）
cashless a. 无现金的
around the corner 很近，就在附近
come to fruition 完成，实现
means n. 方法，手段
revolutionize v. 彻底改革，彻底变革
set up 建立，创立，建造
telecommunication n. 电磁通信，远距离通信
receipt n. 收据，收条
cash v. 将…兑换成现金
issuer n. 开出支票者，出票人
account n. 账户，户头
in the meantime 在此期间，同时
concern n. 担心，忧虑
unauthorized a. 未经授权的，未经认可的
hacker n. 电脑黑客
access v. 存取（计算机文件），获取
database n. 数据库
occurrence n. 事件，发生的事
fraud n. 欺骗，诈骗
violate v. 干扰，侵犯（个人自由等）
"""
add_items(2013, "完形填空", "核心词汇与搭配", raw_2013_cloze)

# 2013 Text 1
raw_2013_t1 = """
entitle v. 称做…；定名为…
relate v. 叙述，讲述，讲（故事）
textile n. 纺织品，织物
automate v. 自动化
stubbornly ad. 顽固地；倔强地
decline v. 下降；衰退
recession n. 衰退；不景气；后退
average n. 平均水平，一般水准
access n. 使用权；通路
robotics n. 机器人科学（或技术）
extra n. 额外的事物
acceleration n. 加速，促进
note v. 指出，特别提到
shed v. 去除；摆脱
erase v. 抹去，消除
previous a. 以前的，以往的
revolution n. 革命
support v. 支持，支撑
ensure v. 保证，确保
make it 达到目标，获得成功
textile mill 纺织厂
keep sb. away from 使某人远离…
make the point 表明观点
more than ever 比以往任何时候都更…
replace with 以…代替…
stand out 突出，脱颖而出
shed workers 裁员
above average 超越平庸，高于平均水平
post-high school education 高中以后教育
"""
add_items(2013, "传统阅读 Text 1", "核心词汇与搭配", raw_2013_t1)

# 2013 Text 2
raw_2013_t2 = """
immigrant n. 移民，外侨
sojourner n. 旅居者；逗留者
depart v. 离开；出发，起程
affectionate a. 深情的；充满深情的
nickname n. 绰号，昵称
rigid a. 严格的；僵硬的，死板的
brand v. 打烙印于…；印商标于…
alien n. 外国人
framework n. 框架，骨架；体系、体制
mightily ad. 很，非常
paralysis n. 麻痹；无力；停顿；瘫痪
thrive v. 兴旺发达，繁荣，蓬勃发展
violinist n. 小提琴手
entrepreneur n. 企业家；承包人
aide n. 助手，助理
participant n. 参与者
straddle v. 跨立于；跨越
jurisdiction n. 管辖范围
identity n. 身份
commit v. 承诺，保证
accommodate v. 提供住宿，容纳
in motion 在运动中的
middle ground 中间立场，中间地带
accomplish v. 完成；实现；达到
from across the Atlantic 来自大西洋彼岸
look to do sth 寻找做某事的机会
make a permanent home 建立永久家园，长留某地
make money 赚钱
a quarter of 四分之一
for good 永远地，永久地
birds of passage 候鸟，漂泊的人
divide into two categories 分为两类
hail as 誉为
in the making 在酝酿中的
brand as 归于…（不好的事物）
kick out 踢出
contribute to 导致…，有助于…
look beyond 超越…看问题
gray area 灰色区域，中间区域
driven by 由…驱动
"""
add_items(2013, "传统阅读 Text 2", "核心词汇与搭配", raw_2013_t2)

# 2013 Text 3
raw_2013_t3 = """
prefer to 喜欢…，愿意…
manage to 设法做到
with ease 轻而易举地
imagine as 将…想象为
for a while 暂时，一会儿
commit oneself to 承诺…
belong to 属于
culture war 文化战争
prone a. 有…倾向的；易于；倾向于
snap a. 仓促的、匆忙的
eliminate v. 消除；排除
hard-wired a. 直觉的、天生的、本能的
mechanism n. 机制
assess v. 评定，评估
preferably ad. 较好，更适宜
neuroticism n. 神经质，情绪不稳定性
stimuli n. 刺激
exclusive a. 独有的，专有的，独占的
realm n. 领域，范围
prime v. 使准备好
impulse n. 冲动，心血来潮
reverse v. 颠倒；逆转
screener n. 筛选者
bias n. 偏见，偏爱
slice v. 切下；把…分成部分
ground v. 打基础；使接触地面
retreat n. 僻静处，隐居处，休息寓所
mute v. 减弱…声音；控制、抑制
differentiate v. 区分，区别
intermittently ad. 间歇地，断断续续地
contemplate v. 沉思，思忖
temptation n. 引诱；诱惑物
snap decision 快速决策，仓促决定
important defense mechanism 重要防御机制
be hard-wired to do 天生会做某事
interpersonal realm 人际领域
prime sb. to do 使某人准备好应付
have little to do with 与…无关
associate with 将…和…联系起来
housing options 住房选择
real estate agent 房产中介
rise above 超越，克服
"""
add_items(2013, "传统阅读 Text 3", "核心词汇与搭配", raw_2013_t3)

# 2013 Text 4
raw_2013_t4 = """
corporate a. 法人的，公司的
senior a. 高级的，地位较高的，级别高的
overwhelmingly ad. 压倒性地；不可抵抗地
board n. 董事会，委员会，理事会
legislation n. 立法，法律
compel v. 强迫，迫使
proportion n. 比例；部分
mandate n. 授权；命令，指令
frustration n. 挫折，挫败
sign up for 报名参加
appeal n. 呼吁
quota n. 定量，定额，指标
ladder n. 阶梯
glass ceiling 玻璃天花板
binding a. 有约束力的
reluctance n. 勉强，不情愿
run counter to 违反，背道而驰
meritocracy n. 英才教育（制度）
obstacle n. 障碍，干扰
temporarily ad. 暂时
order v. 命令，要求
evade v. 逃避；规避；逃脱
break through to 突破，突围
summit n. 顶点；最高阶层
precisely ad. 确实
exception n. 例外
appropriate a. 适当的；合适的
in place 准备妥当，在正确位置
newsworthy a. 有报道价值的
just a. 公正的，合理的
gender-equality heaven 性别平等的天堂
senior management decisions 高层管理决策
corporate boards 董事会
maintain a certain proportion of 保持一定比例
climb the corporate ladder 攀爬企业晋升阶梯
balance work and family 平衡工作和家庭
legally binding provisions 具有法律约束力的条款
the summit of corporate power 公司权力高层
highly capable person 优秀人才，卓越人士
"""
add_items(2013, "传统阅读 Text 4", "核心词汇与搭配", raw_2013_t4)

# 2013 新题型
raw_2013_new = """
chronicle v. 按事件发生顺序记载
live on 靠…生活
benefit n. 救济金，补助金
burn out 烧尽；筋疲力尽；出故障
validation n. 承认，认可
council flat 公营公寓
field v. 处理，应付（问题或意见）
on a budget 避免不必要开支，节省费用
impulsive a. 冲动的；任性的
ingredient n. 原料；材料；食材
exact a. 准确的，精密的；精确的
template n. 模板，样板
cost effective 符合成本效益的，划算的
fancy v. 喜爱，想要
anonymity n. 匿名，不知名
come in handy 派得上用场
embarrassment n. 窘迫，难堪
greengrocer n. 蔬菜水果商；菜贩
chiller n. 冷却装置，冷柜
leftover n. 剩余物，残羹剩饭
stock n. 高汤，原汤
eliminate v. 消除，消灭
surplus a. 剩余的；过剩的
threaten v. 预示凶兆，有…危险
frugal a. 节俭的；朴素的；花钱少的
deli n. 熟食店
knuckle n. 关节骨
carcass n. 尸体；兽体
set lunch 午间套餐
Michelin-starred a. 米其林星级的
"""
add_items(2013, "新题型", "核心词汇与搭配", raw_2013_new)

# 2013 翻译与写作
raw_2013_trans_write = """
pick v. 选择，挑选
instantly ad. 立即，即刻
overwhelmed a. 不知所措的
absorb v. 吸收，理解，掌握
neatly ad. 整洁地，整齐有序地
acute a. 敏锐的；激烈的
vivid a. 生动的；鲜明的；逼真的
pop into 跃入，突然出现
charity sale 义卖
donate v. 捐献
gain n. 收益
the Project Hope 希望工程
schedule v. 将于…举办、实施
for the sake of 为了
on the verge of …的边缘
be desirous of 希望
sufficient a. 足够的
financially strained families 家境贫寒的
achieve this aim 实现目的
desired a. 喜欢的，心仪的
at a discount 打折
secondhand a. 二手的
flea market 跳蚤市场
donated products 捐赠的产品
socially responsible company 具有社会责任感的公司
raise money 筹集资金
history of Chinese film 中国电影的历史
director n. 导演
actor n. 演员
actress n. 女演员
rate n. 比率
rise annually 逐年上升
take part-time jobs 兼职
gain practical experience 获得实践经验
strike a balance 谋求平衡
occur v. 发生
motive n. 动机
reach a record high 创下历史新高
erosion of study time 侵蚀学习时间
suffer academically 学业上受到损害
relieve economic burden 缓解经济负担
gain insight into real society 了解真正的社会
put knowledge into practice 学以致用
flexible schedule 灵活的时间安排
civil service examination 公务员考试
secure career 安全的职业生涯
good social status 良好的社会地位
"""
add_items(2013, "翻译与写作", "核心词汇与表达", raw_2013_trans_write)

# 2012 完形填空
raw_2012_cloze = """
mindless a. 没头脑的，盲目的，无谓的
military adventurism 军事冒险主义
liberate v. 解放，使…自由
tear away from 使依依不舍地离开，忍痛离去
foxhole n. 散兵坑
shelter n. 庇护处，庇护所
stick it out 坚持到底，忍受下去
Nazi reign of murder 纳粹杀戮统治
volunteer n. 志愿者，自告奋勇者
fierce a. 凶猛的，凶狠的
brutal a. 残忍的，野蛮的
abbreviation n. 缩写词，缩写形式
article n. 物件，物品
working class 工人阶级，劳动阶级
secretary of state 国务卿，部长
career n. 生涯，履历
personality n. 性格，个性
correspondent n. 记者，通讯员
portray v. 扮演（某角色）
cover v. 报道，电视报道
capture v. 用武力夺取，攻占
cartoon n. 漫画，讽刺画
exhaustion n. 筋疲力尽，耗尽
civilization n. 文明，社会文明
"""
add_items(2012, "完形填空", "核心词汇与搭配", raw_2012_cloze)

# 2012 Text 1
raw_2012_t1 = """
scorn v. 蔑视，鄙视
revise v. 改变，修正
ritual n. 惯例，老规矩，例行公事
inflexible a. 僵化的，缺乏弹性的
mandate v. 命令，指示
address v. （着手）解决、处理（问题）
impoverished a. 贫困的
chaotic a. 混乱的
contradictory a. 矛盾的
essentially ad. 本质上，根本上
pass n. 通行证
implication n. 含义，暗示
skip v. 不做（本来应做的事）
report card 成绩单
empower v. 授权（某人或组织做某事）
flat a. 固定的
across-the-board a. 一刀切的
thorny a. 棘手的
conversely a. 相反地，另一方面
portion n. （某物的）一部分
put on hold 搁置，暂缓实施
hearing n. 听证会，审讯，聆讯
be popular with 受…欢迎
across the country 全国
with the exception of 除…之外
academic grade 学业成绩
be meant to 旨在…
give a pass to 对…给予通行证
be allowed to 被允许做某事
no more than 仅仅，只有
empower sb. to do 赋予某人权力
at the same time 与此同时
thorny questions 棘手的问题
academic achievement 学业成绩
a significant portion of …的很大一部分
school board 董事会
be responsible for 负责
look into 调查
conduct public hearings 举行公众听证会
it is not too late 为时不晚
"""
add_items(2012, "传统阅读 Text 1", "核心词汇与搭配", raw_2012_t1)

# 2012 Text 2
raw_2012_t2 = """
pervasive a. 普遍的，无处不在的
intrinsically ad. 从本质上（讲）
celebrate v. 表扬、歌颂
fuse v. 使熔合
singular a. 突出的，非凡的
encode v. 编码，加密
associate a. 副的
nursery n. 育儿室，托儿所
pastel a. （色彩）淡的，柔和的
amplify v. 扩大，增强
dictate v. 控制，支配
toddler n. 幼童
consumerism n. 消费主义
counsel v. 建议
split v. 分裂，分开
segment v. 分割，划分，细分
magnify v. 放大，扩大
pretty in pink 穿粉色好看，粉红佳人
be obsessed with 痴迷于…
be pervasive in 充斥于…
a tiny slice of …的一小片
singular lack of imagination 缺乏想象力
encoded in one's DNA 编码至某人DNA
associate professor 副教授
domestic washing machine 家用洗衣机
as a practical matter 出于实用角度
gender-neutral dress 中性衣服
marketing strategy 市场策略
come into its own 显示出用处
marketing trend 营销趋势
core belief 核心观念
psychological development 心理发展
turn out 结果是
clothing manufacture 服装制造商
department store 百货商店
increase sales 增加销售额
stepping stone 踏脚石，跳板
boost profits 提高利润
segment a market 细分市场
"""
add_items(2012, "传统阅读 Text 2", "核心词汇与搭配", raw_2012_t2)

# 2012 Text 3
raw_2012_t3 = """
patent n. 专利证书
isolate v. 分离（物质、疾病等以作研究）
violently ad. 激烈地，强烈地
agitated a. 紧张不安的，焦虑的
preliminary a. 初步的，预备的
federal appeals court 联邦上诉法院
overturn v. 使倾覆，打翻
prior a. 先前的，较早的
rule v. 判决，裁定
blessing n. 幸事，幸运，福气
alike ad. 同样都
personalised a. 个性化的
suppress v. 镇压，制止，压制
reward v. 酬谢，报答，奖赏
monopoly n. 垄断者，垄断企业
file v. 提出，提交，发表
molecule n. 分子
genome n. 基因组
violate v. 侵犯
the Supreme Court 最高法院
advance v. 进步，进展
suit n. 诉讼，讼案
domain n. 领域，范围
interact v. 互动，相互作用
correlation n. 相互关系，关联
convention n. 会议
session n. 会议
shifting a. 移动着的，变化着的
landscape n. 形势
packed a. 挤满人的，非常拥挤的
federal judge 联邦法官
biotech industry 生物科技产业
shake to its core 彻底震撼…
win patents for 获取关于…的专利
overturned prior decision 推翻先前判决
hold patents to 持有…的专利
a blessing to …的福音
make arguments against 提出反对…理由
suppress innovation 抑制创新
restrict access to 限制对…的使用
file a brief 提交案情摘要
separate from 将…从…中分离
in the public domain 属于公共领域
drug's efficacy 药物疗效
be eager to win 急于赢取…
"""
add_items(2012, "传统阅读 Text 3", "核心词汇与搭配", raw_2012_t3)

# 2012 Text 4
raw_2012_t4 = """
course n. 自然的进展，通常的过程
reshape v. 重塑
lining n. 衬里，里子
materialistic a. 物质主义的（含贬义）
prudent a. 明智谨慎的，节俭的
respect n. 方面
fever n. 狂热，高度兴奋
reckless a. 轻率的，鲁莽的，不顾后果的
lengthy a. 长时间的，过长的
stagnation n. 经济停滞
mean-spirited a. 心胸狭隘的
inclusive a. 包容的，范围广阔的
sentiment n. 观点，感想，意见
shrink v. （使）缩小，（使）收缩
reinforce v. 加强，强化
graduate v. 逐渐发展；升级
dim v. （使）变黯淡
resentment n. 怨气，怨恨，不满
discern v. 识别，看清，领悟
lean a. 不景气的
poll n. 民意调查，民意测验
social fabric 社会结构
great recession 经济大衰退，经济萧条
high joblessness 高失业率
life course 生命历程
find silver linings 寻找一线希望
better off 更好
fever dream 狂热之梦
put an end to 对…作出终结
economic stagnation 经济停滞
class divides 阶级分化
catch up to 赶上
lean times 经济不景气时期
"""
add_items(2012, "传统阅读 Text 4", "核心词汇与搭配", raw_2012_t4)

# 2012 新题型
raw_2012_new = """
accomplish v. 完成，实现
sage n. 哲人，先知
craze n. 时尚，时髦，热潮
approach v. 对付，处理，研究
empathy n. 同情，同感，共鸣
inspiration n. 启示，鼓舞
the Renaissance 文艺复兴（时期）
exemplary a. 模范的，可做楷模的
rambling a. （讲话或文章）杂乱无章的
champion v. 捍卫，维护
cunning n. 狡猾，狡诈
ruthlessness n. 无情，冷酷
commemorate v. 庆祝，纪念
catalogue n. 目录，名录
furnish v. 提供，供应
resolute a. 坚决的，坚定的
steadfast a. 忠诚的，坚贞不渝的
beacon n. 引路人，指路明灯
bourgeois a. 市侩的，庸俗的，追求物质的
epochal a. 具有时代意义的
bombast n. 空洞华丽的（言论）
hitherto ad. 迄今，至今
immense a. 巨大的
wage v. 发动，进行（战争，战斗）
nurture v. 培养，培育
unpick v. 分析，研究
multiplicity n. 多样性
downstairs n. 底层（阶级）
upstairs n. 上层（阶级）
"""
add_items(2012, "新题型", "核心词汇与搭配", raw_2012_new)

# 2012 翻译与写作
raw_2012_trans_write = """
migration n. 移民
prospect n. 前景，很可能会发生的事情
departure n. 离开，启程
privilege v. 给予…特权；特别优待
emigrate v. 移居外国
brain drain 人才流失
deprive v. 剥夺
can't work normally 不能正常工作
provide a new one 提供新的
repair v. 维修
demand a refund 退款
to my dismay 让我难过的是
shut itself down automatically 自动关机
intolerable frequency 让人无法忍受的频率
replacement n. 更换
follow warranty policy 履行保修协议
satisfaction n. 满意
reach v. 与…联系
short battery life 电池使用时间短
broken screen 坏的屏幕
frequent application crash 频繁退出程序
table n. 表格
employee above 50 years old 50岁以上的雇员
employee 40 years or younger 40岁以下的雇员
job satisfaction 工作满意度
content/satisfied a. 满意
employee age 雇员年龄
energetic a. 有活力的
competent a. 有能力的
professional n. 专业人士
consequent a. 相应的
occasional a. 偶尔的
reach a career plateau 进入职场高原
sense of powerlessness 无力感
upward spiral 处在上升阶段
career maturity 职业发展成熟
retirement life 退休生活
career advance opportunities 职业发展机会
relationship with management 与领导层的关系
work environment 工作环境
financial stability 财务稳定性
benefits n. 利益
middle-income consumer 中等收入消费者
low-income consumer 低收入消费者
high-income consumer 高收入消费者
"""
add_items(2012, "翻译与写作", "核心词汇与表达", raw_2012_trans_write)

with open(r'f:\obsidiannote\obsidian-\408\数据结构\考研英语二核心词背诵\data_generators\data_2013_2012.json', 'w', encoding='utf-8') as f:
    json.dump(DATA_2013_2012, f, ensure_ascii=False, indent=2)

print('Generated 2013 & 2012 items count:', len(DATA_2013_2012))
