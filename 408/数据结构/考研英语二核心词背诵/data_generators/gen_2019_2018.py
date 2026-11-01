# -*- coding: utf-8 -*-
import json, re

DATA_2019_2018 = []

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
            
            DATA_2019_2018.append({
                "year": year,
                "section": section,
                "category": subcategory,
                "word": eng_word,
                "pos": pos,
                "trans": cn_part
            })
        else:
            DATA_2019_2018.append({
                "year": year,
                "section": section,
                "category": subcategory,
                "word": line,
                "pos": "",
                "trans": ""
            })

# 2019 完形填空
raw_2019_cloze = """
stay aware of 保持…的意识；随时留意…
fluctuation n. 起伏，波动
as for 至于，关于
shift from 从…转移
generally healthy 整体健康
physically active 精力富足；身体活跃
scale n. 天平；秤
overall fitness 整体健康状况
gain weight 体重增加
muscle mass 肌肉重量
alter v. 改变，更改
conflict with 冲突；与…抵触
accurate a. 精确的
hard work 努力锻炼
gym n. 健身房
observe v. 观察
inch n. 英寸；（身体）尺寸
switch to 切换到；转变成
bimonthly a. 两月一次的；一月两次的
schedule n. 计划表，进度表，日程表
significant a. 相当数量的；影响显著的；重要的
weigh-in n. 称体重
nutrition n. 营养（作用）；滋养
intensity n. 强度；强烈
constantly ad. 持续不断地；经常地
caloric a. 热量的
intake n. （食物、饮料等的）摄入量，摄取量
work wonders 创造奇迹/取得惊人成效
overall a. 总的，全部的
fitness n. 健壮，健康
zeal n. 热情，热忱
work out 锻炼
burden n. 重担，负担
rather than 而不是
focus n. 焦点；（注意力的）集中点，中心点
"""
add_items(2019, "完形填空", "核心词汇与搭配", raw_2019_cloze)

# 2019 Text 1
raw_2019_t1 = """
emerge v. 出现；显露
grasp n. 理解，领会
norms n. 规范，行为标准
appease v. 安抚，抚慰
conscience n. 道德心；良心
equivalent n. 相等的东西
revival n. 复苏，复兴
binary a. 二进制的；二元的
advantageous a. 有利的，有好处的
destructive a. 破坏性的，引起破坏的
prompt v. 促使，导致
species n. 物种
glue n. 胶水，胶
compensate v. 补偿，弥补
deficiency n. 缺乏；缺陷
represent v. 代表
pathway n. 路径，途径
shortfall n. 不足，差额
impulse n. 冲动
assessment n. 评价，看法
rate v. 评估，评价
transgression n. 越轨，违背道德
anonymous a. 名字不公开的，匿名的
inclined a. 有…的倾向
prone a. 有做…倾向的，易于遭受…的
deprivation n. 匮乏，缺少
prosocial a. 亲社会的，忠实于既定社会道德准则的
in conjunction with 与…一起，连同
in the right amount 适量
the popular imagination 在大众眼中
bad rap 口碑差，无理指责
alert sb. to sth 使认识到，使意识到
make up for 弥补，补偿
hold together 使保持团结
rein in 严格控制，抑制
vice versa 反之亦然
substitute for 替代，取代
turn on sth 依靠，取决于
"""
add_items(2019, "传统阅读 Text 1", "核心词汇与搭配", raw_2019_t1)

# 2019 Text 2
raw_2019_t2 = """
climate change 气候变化
carbon dioxide 二氧化碳
hasten v. 加速
emit v. 发出；散发
absorb v. 吸收
trap n. 陷阱；困境
involve v. 包含，需要；牵涉
subtle a. 微妙的；机智的
flourish v. 繁荣，兴旺
carbon sink 碳汇
capacity n. 能力；容量
effort n. 有组织的活动
young tree 幼树
brush n. 灌木丛地带；矮树丛
temporarily ad. 临时地，临时
draw v. 获取；吸取
moisture n. 水分
thrive v. 茁壮成长
restore v. 恢复；修复
landscape n. 自然景色
render v. 致使
burnable a. 可燃的；易燃的
consume v. 耗尽，毁灭
urgent a. 紧急的；急迫的
drought n. 干旱
wildfire n. 野火
acre n. 英亩
proceed n. 收入，获利
emissions-permit 排放许可证
auction n. 拍卖
prioritize v. 优先处理；优先考虑
woody a. 木质的
lumber n. 木材
biofuel n. 生物燃料
fossil fuel 矿物燃料，化石燃料
wildlife n. 野生动植物
watershed n. 流域
recreation n. 重现；重建
store v. 贮藏，储存
finalize v. 把最后定下来；定案
governor n. 地方长官；州长
in the light against 与…的斗争/战斗
even as 正当，恰好在…的时候
count on 指望；依靠
soak up 吸收
a good share of 许多，大量
leave sb. with sth 将…留给某人
a way out 摆脱困难的方法
strike a balance 达成平衡
lead the way 带路，示范
figure out 想出；弄明白；解决
double efforts 加倍努力
thin out 一份；份额
pull from 分离；取出
fend off 避开；挡住
in the event of sth 如果某事发生，万一
be financed from 从…中获得资金
in all 总共，合计
at risk of 处于…的风险之中
lock away 把…锁起妥藏
run on 用…驱动
under way 在进行中
be accustomed to 习惯于…
come to 开始；逐渐
"""
add_items(2019, "传统阅读 Text 2", "核心词汇与搭配", raw_2019_t2)

# 2019 Text 3
raw_2019_t3 = """
overhaul n. （制度或方法的）彻底改革
obstruct v. 阻碍，阻挠
straightforward a. 简单的，不复杂的
loser n. 损失者，受害者
undocumented a. 非法的，无证的
characteristic n. 特征
predominantly ad. 主要地
cure n. 对策，措施
implausible a. 似乎不合情理的
mechanization n. 机械化
soybean n. 大豆
strawberry n. 草莓
dairy a. 生产乳品的
automated a. 自动化的
temporary a. 暂时的，临时的
sharply ad. 急剧地，突然大幅度地
issue v. （正式）发出
numerical a. 数字的
cap n. 最高限度
cumbersome a. 缓慢复杂的
bureaucratic a. 官僚的，官僚主义的
compound v. 加剧
raid n. 突击搜查
raisin n. 葡萄干
berry n. 浆果，莓
operation n. 业务
share n. （分担的）一部分
labor shortage 劳动力短缺
oft-debated 备受争议的
all along 自始至终，一直
high-value 高价值的
labor-intensive 劳动密集型的
guest worker （尤指来自穷国的）外籍务工者
fill the gaps 填补空缺
in effect 实际上
"""
add_items(2019, "传统阅读 Text 3", "核心词汇与搭配", raw_2019_t3)

# 2019 Text 4
raw_2019_t4 = """
star v. 担任主角，主演
single-use a. 一次性的
staple n. 日常必需品
straw n. 吸管
cutlery n. 餐具
combat v. 与…战斗，与…斗争
enact v. 通过（法律），将…制定成法律
legislation n. 法律，法规
curb v. 控制，抑制
overarching a. 首要的；中心的
concern n. 忧虑，担心
detrimental a. 有害的，不利的
bold a. 果敢的，无畏的
allay v. 消除或减轻（恐惧/担忧等）
ignore v. 忽视，置之不理
imply v. 暗示，暗指
sustainably ad. 可持续地
acknowledge v. 承认（事实或情况）
priority n. 优先考虑、处理的事，当务之急
collectively ad. 集体地，共同地
implement v. 贯彻，执行
problematic a. 难对付的，成问题的
ban v. 禁止，取缔
altogether ad. 完全地
eliminate v. 消灭，根除
incentive-based a. 激励性的
recycling n. 再利用，回收利用
trash n. 废物，垃圾
disposal n. 丢弃，清除
primary a. 首要的，主要的
perspective n. 合理判断，正确认识
progressive a. 进步的，先进的
shape v. 塑造
alongside prep. 与…一起/同时
engaged a. 被卷入的，参与的
a bunch of 大量的
swap out 将…替换掉
put together 整理；汇总
be directed at 对准…，针对…
grocery store 食品杂货店
do one's bit 尽本分
moral licensing 道德许可效应（做出好行为后放纵自己）
"""
add_items(2019, "传统阅读 Text 4", "核心词汇与搭配", raw_2019_t4)

# 2019 新题型
raw_2019_new = """
in charge 主管的，负责的
hold sb. to account 追究…的责任
push for sth 努力争取…，一再要求…
write off 认为…不重要，忽视
rein in 控制
housing n. 住房
poll n. 民意调查，民意测验
buck v. 反抗，抵抗
proclivity n. （尤指坏的）倾向，嗜好
realty n. 房地产 (real estate)
agent n. 经纪人，代理人
involve v. 使参与
ownership n. 所有权
overwhelming a. 令人不知所措的
remove v. 移走，搬走
current a. 现时的，当前的
broker n. 经纪人，掮客
associate n. 生意伙伴，合伙人
convince v. 使信服
proximity n. （时间或距离的）接近，临近
attorney n. 律师
ruin v. 毁掉，毁坏
solely ad. 唯一地，仅仅
issue n. 问题；要点
shelter n. 住处，躲避处
mindset n. 思维模式
consequence n. 后果
feature n. 特点，特色
remind v. 使想起，提醒
harsh a. 刺耳的，令人不快的
contingent a. 取决于…
customize v. 定做，定制
relevant a. 有价值的，有意义的
embrace v. 欣然接受，乐意接纳
despite prep. 尽管，虽然
remark v. 评论道，谈道
note v. 特别提到，指出
assume v. 假定，假设，认为
weigh heavily on 对…有重大影响
in the dark 全然不知，一无所知
have mixed views 持有不同观点，看法不一
cope with 处理，应付
support system 支持体系
in regards to 关于，至于
place emphasis on 重视，强调…
tend to do sth 往往会…
get stuck in 陷入…
not... but rather 不是…而是…
meet one's needs 满足某人的需求
even as 正当…时
housing crunch 住房紧张
pose challenges to 对…造成挑战
rather than 而不是
"""
add_items(2019, "新题型", "核心词汇与搭配", raw_2019_new)

# 2019 翻译与写作
raw_2019_trans_write = """
underestimate v. 低估
readable a. 可读的，易读的
imitate v. 模仿
abundance n. 充裕，丰富
polished a. 精致的，精彩的
suffer v. 遭受，蒙受
determined a. 意志坚定的
contrary to 与…相反
have a go at 尝试
the majority of 大部分，大多数
along the way 一路上，沿途
earn the hard way 来之不易
literary field 文学领域
debate topic 辩题
express one's opinions 发表观点
traffic n. 交通状况
infrastructure n. 基础设施
relevant policy 相关政策
competition n. 竞赛，比赛
except for 除了…之外
inadequate a. 不足的
paralysis n. 瘫痪，停顿
involve v. 包含，涉及
argumentation n. 辩论；论证
surround v. 与…密切相关；围绕
concerning prep. 关于，涉及
with regard to 关于
bar chart 柱状图（条形图）
career path 职业道路
enter the workforce 就业
postgraduate study 升学，深造
start up a business 创业
employment rate 就业率
salary / wage 薪水
become self-employed 自主创业
display v. 显示（信息），展露
specifically ad. 具体来说；特定地
whereas conj. 但是，却
ascend v. 上升，升高
witness v. 见证，证明
shift n. 转变，改变
financial stress 经济压力
increasingly ad. 越来越多地，渐增地
undertake v. 承担，接受
professional n. 专业人士，专家
threshold n. 门槛
climb up the career ladder 攀登事业阶梯
embark on the path of 走上…道路
fresh-faced graduate 初出茅庐的大学毕业生
entrepreneurial a. 企业家的，创业者的
employment prospects 就业前景
corporate culture 企业文化
work-life balance 生活与工作平衡
"""
add_items(2019, "翻译与写作", "核心词汇与表达", raw_2019_trans_write)

# 2018 完形填空
raw_2018_cloze = """
painful a. 令人痛苦的；令人不快的
inherent a. 内在的，固有的；生来就有的
willingness n. 乐意；心甘情愿
stimuli n. 刺激（物）（stimulus 的复数）
twist n. 意外转折
shock n. 电击，触电
electrified a. 带电的
incur v. 招致；遭受；引起
subsequent a. 随后的，继…之后的
reproduce v. 使再次发生；再现
fingernail n. 手指甲
chalkboard n. 黑板
drive n. 本能的需求，基本欲求
shelter n. 栖身之处，住处；庇护所
instinct n. 本能；直觉
backfire v. 产生事与愿违的结果
insight n. 洞悉；深刻见解
profound a. 知识渊博的；理解深刻的
follow through 进行到底；坚持完成
ahead of time 提前，提早
determine v. 查明；测定，确定
endeavor n. 尝试，努力
"""
add_items(2018, "完形填空", "核心词汇与搭配", raw_2018_cloze)

# 2018 Text 1
raw_2018_t1 = """
justify v. 证明别人认为不合理的事有道理，为…辩护
effort n. 努力，试图
pioneering a. 开创性的，探索性的
practical a. 实际的，动手的
name v. 叫出，说出
utterly ad. 完全地，十足地
overwhelm v. 使不知所措
graffiti v. 涂鸦，乱涂乱画
insidious a. 暗中危害的
prejudice n. 偏见
inferiority n. 低等，劣等
academically ad. 纯理论地，学术上地［与实践相对］
evaporate v. 逐渐消逝
headlong a. 轻率/仓促的
subtle a. 微妙的
devalue v. 贬低
vanish v. 消失
diversity n. 多样性，差异
gift n. 天赋
It's curious that 有些奇怪
as though 好像，似乎
give sb. a better future 给某人一个更好的未来
accepted wisdom 传统信念，普遍看法
mechanical memorization 机械记忆
as sb. knows 正如某人所知
stuck with sth 粘住，无法摆脱
assemble a bicycle 组装自行车
working with hands 用双手工作，实践性劳动
vocational education 职业教育
make it 赶上；获得成功
bachelor's degree 学士学位
in other words 换句话说
turn sth. on its head 使人完全改变思路
be staring sb. in the face 非常清楚/容易看见
be equipped to do 能够胜任做某事
wake-up call 叫醒电话，警示，警钟
risk doing sth 冒险做某事
one-size-fits-all 一刀切
"""
add_items(2018, "传统阅读 Text 1", "核心词汇与搭配", raw_2018_t1)

# 2018 Text 2
raw_2018_t2 = """
roughly ad. 粗略地，大致上
renewable a. 可再生的，可恢复的
momentum n. 势头
commitment n. 承诺
farsighted a. 有远见的
plummeting a. 直线下降的，暴跌的
principal a. 最重要的，主要的
notably ad. 尤其是，特别地
remarkable a. 显著的
quick a. 聪明的，敏锐的，脑子反应快的
put-down n. 贬损的话，奚落的话
skeptic n. 持怀疑态度的人
advance n. 进步，进展
massive a. （尺寸、数量、规模）非常大的
picture n. 情况，局面
spike v. （数量或比率的）激增
meaningful a. 有意义的，重要的
fossil fuel 化石燃料
account for （数量、比例上）占
go on line 在运转，在运行
stem from 出自，来源于
solar panel 太阳能电池板
wind turbine 风力涡轮机
take the lead 取得领先地位
in part 在某种程度上
place big bets on 在…上下大赌注
be a rarity 极为罕见
trend line 趋势线
speed up 加速
alternative energy 替代能源
"""
add_items(2018, "传统阅读 Text 2", "核心词汇与搭配", raw_2018_t2)

# 2018 Text 3
raw_2018_t3 = """
upmarket a. 高级的，高端的
acquire v. 购得，得到
intricate a. 错综复杂的
detailed a. 详尽的；精细的；细致的
enormously ad. 极其，非常
revealing a. 揭示内情的，泄密的
makeup n. （小组或团队的）组成，构成
plot v. 密谋，策划
address v. （着手）解决，处理（问题）
clumsy a. 笨拙、不灵活的；使用不便的
remedy v. 纠正，改正；治疗，救治
abuse n. 滥用
conceptual a. 观念上的，概念上的
virtual a. 实际上的；［计］虚拟的
convert v. 使转变，转化；改装，改造
farm v. 养殖；耕种；承包出去
bug n. 昆虫，小虫子；缺陷
aphid n. 蚜虫
predatory a. 捕食性的，食肉的
spammer n. 垃圾邮件发送者
analogy n. 类推；类似；类比
digital economy 数字经济
grocery chain 连锁杂货店
physical product 实体产品
link to 使挂钩，使联系起来
go through 被认可，成交；通过
party whip 党鞭，党组织秘书
not so much... but 与其说…毋宁说…
interpret with 把…理解/解释为…
to sb's disadvantage 对…不利
for sb's benefit 为了某人的利益，为了帮助某人
even if 即使，就算
"""
add_items(2018, "传统阅读 Text 3", "核心词汇与搭配", raw_2018_t3)

# 2018 Text 4
raw_2018_t4 = """
combat v. 防止，减轻
distracted a. 心烦意乱的，思想不集中的
retreat n. 静修期间（或活动）
ritual n. 程序，仪规；习惯
journalistic a. 新闻工作（者）的
seize v. 抓住，把握（机会、时机、主动等）
immediate a. 当前的，迫切的
scheduling n. 日程安排，排程
interruption n. 打扰，打岔
roughly ad. 大约，差不多
prioritise v. 按重要性排列
craft v. 精心制作
well-structured a. 结构良好的，条理清晰的
demotivate v. 使失去动力，使消极
render v. 使变得；使处于某状态
improvisation n. 即兴表演
reap v. 收获，取得（成果）
downtime n. 停工期，休息
idleness n. 懒惰，空闲
indulgence n. 沉溺，放纵
vice n. 恶行，堕落
psychiatry n. 精神病学
circuit n. 电路，回路
desirable a. 可取的，理想的
put a premium on 重视，珍视
be dedicated to 献身于，专注于
throughout the day 终日，整天
stick to 坚持，忠于
keep to 坚持；信守，固守（习惯等）
to-do list 任务清单，待办事项清单
make the most of 充分利用
"""
add_items(2018, "传统阅读 Text 4", "核心词汇与搭配", raw_2018_t4)

# 2018 新题型
raw_2018_new = """
compliment n. 赞扬，称赞
skip v. 跳过，略过
grocery n. 食品杂货店
cab n. 出租车
stuck a. 卡住的
flow v. （说话或思考）流畅
rut n. （生活或工作）刻板乏味，一成不变
jolt n. 颠簸，震动，摇晃；一阵强烈感情
multitask v. 同时做多件事情
wholeheartedly ad. 全心全意地
feel v. 留下印象，给…感觉
awkward a. 令人尴尬的，令人难堪的
investor n. 投资者；投入（时间等）的人
small talk 寒暄；闲谈
security guard 保安人员
make the first move 迈出第一步，先采取行动
come out （言语以某种方式）被说出
get out 说出（难以启齿的事情）
put on 假装有，装出…
fail to do sth 失败，未能做到…
be willing to do 乐意做…，愿意做…
make an effort 勉力想做某事
in common 共用的，公有的；共同的
all of a sudden 突然
pour out 倾吐，倾诉，尽情地诉说
eye contact 对视，目光接触
"""
add_items(2018, "新题型", "核心词汇与搭配", raw_2018_new)

# 2018 翻译与写作
raw_2018_trans_write = """
grader n. …年级学生
tick v. 打勾；打对号
astronaut n. 宇航员
convinced a. 坚信的；深信的
encyclopedia n. 百科全书
institute v. 制定（政策等）；实行
title n. （书刊的）一种，一本
avenue n. 途径；手段
apologize v. 道歉
cancel v. 取消
appointment n. 约定
reschedule v. 重新安排
terribly ad. 非常
necessitate v. 使…不可避免
look forward to 期待
unexpectedly ad. 出乎意料地
substitute for 替代，顶替
fall ill 生病
attend v. 出席
pie chart 饼状图
account for 占…（比例）
constitute v. 组成
make up 构成
take into account 考虑
per capita 人均
dine out 外出进餐
illustrate v. 阐明
distinguishing a. 有区别的
proportion n. 部分
respectively ad. 各自地
disposable income 可支配收入
primary concern 首要关心的问题
predictably ad. 可预见地
catering companies 餐饮企业
prosperity n. 繁荣
boom n. 繁荣兴旺
economic recovery 经济复苏
purchasing power 购买力
service industry 服务行业
enterprise image 企业形象
advertisement campaign 广告宣传活动
obtain news 获取新闻
approach n. 途径
mobile phone 手机
laptop n. 笔记本电脑
newspaper n. 报纸
magazine n. 杂志
"""
add_items(2018, "翻译与写作", "核心词汇与表达", raw_2018_trans_write)

with open(r'f:\obsidiannote\obsidian-\408\数据结构\考研英语二核心词背诵\data_generators\data_2019_2018.json', 'w', encoding='utf-8') as f:
    json.dump(DATA_2019_2018, f, ensure_ascii=False, indent=2)

print('Generated 2019 & 2018 items count:', len(DATA_2019_2018))
