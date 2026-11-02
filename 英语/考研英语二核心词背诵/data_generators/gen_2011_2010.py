# -*- coding: utf-8 -*-
import json, re

DATA_2011_2010 = []

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
            
            DATA_2011_2010.append({
                "year": year,
                "section": section,
                "category": subcategory,
                "word": eng_word,
                "pos": pos,
                "trans": cn_part
            })
        else:
            DATA_2011_2010.append({
                "year": year,
                "section": section,
                "category": subcategory,
                "word": line,
                "pos": "",
                "trans": ""
            })

# 2011 完形填空
raw_2011_cloze = """
afford v. 提供，给予
anonymity n. 匿名，名字不公开
blessing n. 好事，有益之事
explosion n. 激增
cyber-crime n. 网络犯罪
preserve v. 保护，维护
cyber-czar n. 网络总管
voluntary a. 自愿的，自动的
identity n. 身份，身份认证
credential n. 证书，凭据
authenticate v. 证实，证明…是真的
federation n. 联合，联邦，联盟
registered a. 注册的，登记过的
navigate v. 浏览（网站）
ecosystem n. 生态系统
transaction n. 交易，买卖
infrastructure n. 基础设施，基础建设
administration n. 政府
activist n. 积极分子，活跃分子
applaud v. 称赞，赞许
concerned a. 担忧的，焦急的
initiative n. 倡议，新方案
compulsory a. 必须做的，强制的
mentality n. 心态，思想状况
greet sb. with 对…作出某种反应
envision v. 展望，想象
"""
add_items(2011, "完形填空", "核心词汇与搭配", raw_2011_cloze)

# 2011 Text 1
raw_2011_t1 = """
criticism n. 批评，批判
under fire 受到攻击和批评
compensation n. 报酬，薪水
enormous a. 巨大的；庞大的
bonus payouts 奖金支出
be supposed to do 应当做某事；理应做某事
biased a. 有偏见的；结果偏倚的
presumably ad. 据推测；大概；可能
weather v. 平安渡过（难关），挨过
proxy n. 代表权，委托书
departure n. 离开，离去
subsequently ad. 其后，随后，接着
restate v. 重申；重新申报
likelihood n. 可能，可能性
suggestive a. 提示的；暗示的，提醒的
blow n. 打击，意外的灾害，摧毁
reputation n. 名气，信誉，声望
incentive n. 动机，鼓励，刺激
otherwise conj. 否则，不然
firm's board 公司董事会
make one's wealth and reputations 成就功名
proxy statement 股东委托书
depart a board 从董事会离职
concentrate on 集中注意力于
a surprise departure 突然离职
restate earnings 重申盈利
federal class-action lawsuit 联邦集体诉讼
jump off a sinking ship 跳离沉船
a blow to reputations 有损名誉
be on the board 在董事会任职
follow the example of 效仿
"""
add_items(2011, "传统阅读 Text 1", "核心词汇与搭配", raw_2011_t1)

# 2011 Text 2
raw_2011_t2 = """
recession n. 经济衰退，不景气，经济萎缩
chronicle v. 记录（大事）
commission n. 委员会，委员
launch v. 发动；开展（活动、计划等）
charitable a. 公益的，慈善的
subsidize v. 以津贴补助
inhabit v. 居住；在…出现；填满
margin n. 利润，盈余
routine n. 常规，通常情况
afloat ad. 漂浮着的，漂浮不定
overboard ad. 越过船边坠入水中
delivery n. 传达，投递
revenues n. 总收入
reliance n. 依靠，依赖
proportion n. 比，比率，比例
stable a. 稳定的
whirlwind n. 旋风；猛烈的势力
distinctive a. 有特色的，与众不同的
bureau n. 局，处，科；办事处
savagely ad. 野蛮地；残忍地；粗野地
virtue n. 美德；德行；价值；长处
flee to the Internet 转向互联网
launch a round of talks 发起一轮讨论
charitable corporation 慈善公司
shrug off 对…满不在乎，不屑一顾
profit margins 利润空间
stay afloat 维持运营
push overboard 抛弃、甩掉某人/某事
have the nerve 好意思做某事，有胆量做某事
desperate measures 孤注一掷的措施
a healthier mix of revenues 更加健康的收益比例
not surprisingly 毫无疑问
sweep through 掠过、扫过
film reviewers 电影评论员
"""
add_items(2011, "传统阅读 Text 2", "核心词汇与搭配", raw_2011_t2)

# 2011 Text 3
raw_2011_t3 = """
prosperity n. 繁荣，兴旺，昌盛
restraint n. 抑制，控制，限制，约束
stylish a. 时髦的，流行的，入时的
stimulus n. 刺激物，刺激因素
popularize v. 使受欢迎，普及，使流行
architect n. 建筑师，设计师
exert v. 发挥；运用；使受（影响等）
signature n. 签名，署名；识别标志，鲜明特征
derive from 由…起源；取自
laminated a. 由薄片叠成的，分层的
symbolize v. 象征，用符号表现
sophisticated a. 复杂的，精致的
elegant a. 优美的，漂亮的，简练的
equivalent n. 对等物
foreign a. 外国的，外来的
modest a. 适度的，适中的，端庄的
commission v. 委任，授予
aesthetic a. 美学的，审美的
forthright a. 直率的，明确的
mechanical a. 机械的，机械驱动的
acquire v. 获得，取得
desirable a. 令人满意的，可取的
inevitable a. 不可避免的；必然发生的
tend to 往往，易于
by the millions 数以百万计
line up 排队
when it comes to 在某个方面，说到某事
common sense 常识
live with 忍受，容忍
take up posts 就职
signature phrase 口头禅
take for granted 认为…理所当然
mask the fact 掩盖事实
Gold Coast 黄金海岸
abstract art 抽象艺术
"""
add_items(2011, "传统阅读 Text 3", "核心词汇与搭配", raw_2011_t3)

# 2011 Text 4
raw_2011_t4 = """
cheerleader n. 啦啦队长；支持者
chronic a. 慢性的，长期的，习惯性的
acute a. 尖锐的，严重的
converge v. 会于一点；使聚集
devaluation n. （货币）贬值
disintegration n. 瓦解，崩溃
stuck a. 动不了的，被卡住的，被难住的
dominant a. 占优势的，统治的，支配的
harmonisation n. 和谐，协调，相称
quasi-automatic a. 半自动的，准自动的
sanction n. 制裁，处罚
mega-project 特大型项目
suspension n. 暂停，悬挂
ministerial a. 内阁的，部长的，行政上的
rigour n. 严苛，严酷
intervene v. 介于…之间，干预，介入
redistribution n. （尤指钱或土地的）重新分配
fiscal a. 财政上的
transfer n. 转移，调动
murmur v. 咕哝，发牢骚，私下抱怨
curb v. 制止，束缚；限制，抑制
remarkably ad. 引人注目地，明显地
liberal a. 开明的，自由的
blunt v. 使迟钝
benign a. 温和的，仁慈的，善良的
make it 及时到达，成功
talk of 谈论，议论
as well as 和…一样，除了
quick fix 应急措施，权宜之计
save from 使…免遭
dominant powers 主导力量
backed by 依靠，在…支持下
headed by 由…带领的
fiscal transfers 财政转移
corporate-tax rates 企业税率
labour costs 劳动力成本
write off 认定…不重要
trading block 贸易集团，贸易区块
at its best 处在最佳状态/全盛时期时
"""
add_items(2011, "传统阅读 Text 4", "核心词汇与搭配", raw_2011_t4)

# 2011 新题型
raw_2011_new = """
weigh in 参加，加入（争论等）
impose v. 强加；征税
figure n. 人物
outlet n. 经销店；廉价经销店
sponsorship n. 赞助者的地位；赞助行为
halt v. 使停止；使中断；阻止
spiral v. 盘旋上升（或下降）
diabetes n. 糖尿病；多尿症
Paediatrics n. 儿科学；小儿科
excessive a. 过度的，极度的，过分的
inconceivable a. 不能想象的，不可思议的
in respect of 关于，涉及
alarm v. 警告
campaigner n. 运动领导者，运动参加者
take the lead 带头，为首
centerpiece n. 最重要的项目（或物品）
celebrity n. 名人，知名人士，名流
lecture v. 给…作演讲；教训；讲课
potential a. 潜在的，有可能的
billboard n. 广告牌；告示牌
bold a. 勇敢的，无畏的，莽撞的
product placement 产品置入；植入式广告
scheme n. 计划
inducement n. 诱导，诱惑，诱因
lure v. 吸引，引诱
available a. 可获得的，可购得的
up front 预先；在最前面
urge v. 促进，推进，力劝
takeaway n. 外卖食品，外卖店
vision n. 视力，视野
set out 陈述，列述
back v. 支持
radical a. 激进的，彻底的
tactics n. 战术，策略，手段
deploy v. 展开，施展，部署
"""
add_items(2011, "新题型", "核心词汇与搭配", raw_2011_new)

# 2011 翻译与写作
raw_2011_trans_write = """
volume n. 量
emission n. 排放，排放物，散发物
take a toll on 造成损失（或危害、伤亡）
leak v. 使泄露
attempt n. 试图，尝试
maintain v. 保持，维持；保养，维护
monitor v. 搜集，记录；测定；监督
efficiency n. 效率，效能
congratulate v. 祝贺
admission to university 被大学录取
university life 大学生活
win the competition 赢得竞争
extraordinary capacity 杰出的能力
purposefully ad. 有目的地
glittering career 辉煌的事业
approaching a. 即将到来的
important adjustment 做出重要调整
grow into an adult 成长为成人
diligence n. 勤奋
flexibility n. 灵活
good health 健康
thrift n. 节俭
self-discipline n. 自我约束能力
independent thinking 独立思考的能力
communication ability 沟通能力
solve conflicts 解决冲突的能力
self-learning ability 自学能力
learn from others 向别人学习
don't fear to make mistakes 不要害怕犯错误
never shift responsibility 绝不逃避责任
strive for self-improvement 努力自我提升
auto market 汽车市场
market share 市场份额
brand n. 品牌
quality n. 质量
auto producer 汽车制造商
promotion strategies 推广策略
reputation crisis 信誉危机
dominate v. 支配、控制
noticeable a. 明显的
slip v. 下降
bargain n. 便宜商品
plight n. 困境
reminder n. 提醒认识的事物
slight increase 小幅上涨
displaced from leading position 被取代主导地位
expand one's share 增加市场份额
reliable quality 可信赖的质量
narrow technology gap 缩小技术差距
appetite for 对…的喜好
quality complaint 质量投诉
technological improvement 技术进步
effective price strategy 有效的价格策略
price advantage 价格优势
smart phone market 全球智能手机市场
Nokia 诺基亚
Samsung 三星
iPhone 苹果手机
"""
add_items(2011, "翻译与写作", "核心词汇与表达", raw_2011_trans_write)

# 2010 完形填空
raw_2010_cloze = """
outbreak n. （战争或疾病的）爆发
swine flu 猪流感
detect v. 发现，察觉
epidemic n. 传染病，流行病
heightened a. 提高的，增加的
alert n. 警惕，警戒
assemble v. 召集（会议），（会议）召开
severity n. 严重程度
overwhelming a. 压倒性的，势不可挡的，巨大的
mild a. 轻微的
symptom n. （临床）症状
authority n. 当局，官方
hospitalization n. 长期住院，住院治疗
at the height of 在…顶点；在…的顶峰或鼎盛时期
panic n. 恐慌，惊慌
fade v. 逐渐消失
virtually ad. 几乎，事实上
seasonal flu 季节性流感
federal a. 联邦的，同盟的
stockpile n. 库存，积蓄
vaccine n. 疫苗
dose n. （药物的）剂量，一剂
nasal spray 鼻用喷雾
vaccinate v. 给…注射疫苗
"""
add_items(2010, "完形填空", "核心词汇与搭配", raw_2010_cloze)

# 2010 Text 1
raw_2010_t1 = """
bull n. （股票市场上）买空者
run n. 态势，状况，趋势
note n. 气氛，特征
fetch v. 售得、卖得
auctioneer n. 拍卖师
bid n. 出价
bankruptcy n. 破产
momentum n. 势头
bewilderingly ad. 令人费解地
reckon v. 认为
generate v. 产生
ego n. 自我
greed n. 贪婪
controversy n. 争议
unfashionable a. 不合时宜的
gallery n. 画廊、美术馆
salerooms n. 拍卖场
contemporary a. 当代的
overheated a. 过热的
guarantee n. 保证、担保
downturn n. （经济活动、生产等）下降、衰退
Impressionist n. 印象派
fluctuant a. 波动的
slump n. （价格、数值等）暴跌、不景气、萧条
deliver v. 输送
bull run 牛市态势
on a dramatic note 以一种戏剧般的方式
call out bids 喊出报价
file for 申请
lose momentum 失去发展势头
for a while 一段时间
rise bewilderingly 急剧增长
at its peak 在其顶峰时期
come down to 下降到…
far beyond 远远超过
enormous egos 自负，以自我为中心
stay away from 远离
contemporary art 当代艺术
auction house 拍卖行
pay out 偿付、支付
downturn in the art market 艺术品市场的衰退
at the bottom 处于谷底
"""
add_items(2010, "传统阅读 Text 1", "核心词汇与搭配", raw_2010_t1)

# 2010 Text 2
raw_2010_t2 = """
address v. 发表演说，向…讲话
gathering n. 聚会
suburban a. 郊区的
talkative a. 健谈的
anecdote n. 奇闻、轶事
comment v. 发表意见
gesture v. 做手势，做动作示意
puzzled a. 困惑的
episode n. 插曲
crystallize v. 使明确化、使具体化
irony n. 具有讽刺意味的情况
wreak v. （对某物）造成破坏
havoc n. 灾难、混乱
sociologist n. 社会学家
virtual a. 实际上的、几乎的
epidemic n. 流行病
tangible a. 确凿的，实在的
inequity n. 不平等
accompany v. 陪伴
share n. （某人应有或承担的）一份
observe v. 评论
expectation n. 期望
represent v. 代表
crisis n. 危机
stereotypical a. 典型的
scene n. 场景
address a gathering 在聚会上演讲
nod in agreement 点头表示同意
gesture toward 用手势示意，指着
burst into laughter 爆发笑声
keep the conversation going 使谈话继续
tend to 倾向于，趋于
wreak havoc with 给…带来浩劫
in the late 1970s 1970年代后期
lack of 缺乏
amount to 相当于；总计
focus on 集中于…
give up 放弃
conversational partner 谈话伙伴
first and foremost 首先、首要
glare at 怒视，瞪视
"""
add_items(2010, "传统阅读 Text 2", "核心词汇与搭配", raw_2010_t2)

# 2010 Text 3
raw_2010_t3 = """
perfect v. 使完美、完善
automatic a. 自动的
snack n. 零食、小吃
wipe v. 擦、抹
counter n. 柜台
cue n. 提示、暗示
fundamental a. 基本的
hygiene n. 卫生（学）
tropical a. 热带的
subtle a. 微妙的
corporation n. 大型公司、企业集团
routine n. 惯例
chew v. 咀嚼
moisturizer n. 润肤膏
disinfecting a. 消毒的
purifier n. 净化器
fabric n. 针织物
vitamin n. 维他命、维生素
multiple a. 多次的
shrewd a. 精明的
campaign n. 宣传活动
cavity-preventing a. 口腔预防的
scrub n. 擦洗
beverage n. 饮料
bottle v. 把…装进瓶
spring n. 泉、山泉
sip v. 小口地喝
primarily ad. 首先地
adolescent a. 青春期的
feature v. 以…为特色
commercial n. 商业广告
ritual n. 仪式
slip v. 滑
psychologist n. 心理学家
viable a. 可行的
ruthless a. 无情的、残忍的
erupt v. 爆发
tactic n. 策略
automatic behaviors 无意识行为
carefully designed 精心设计的
daily cues 日常触机
public health problems 公共健康问题
figure out 弄懂、弄明白
soap habit 用香皂洗手的习惯
learn from 向…学习
turn to 求助于
bottle the springs 将泉水装瓶
slip between 将…悄悄放在两者之间
daily patterns 每天的惯例
be essential to 对…来说具有决定作用
tie to 将…系于…
"""
add_items(2010, "传统阅读 Text 3", "核心词汇与搭配", raw_2010_t3)

# 2010 Text 4
raw_2010_t4 = """
jury n. （由12位公民组成的）陪审团
concrete a. 具体的
democratic a. 民主的
minimal a. 最低限度的
qualification n. 限定性条件
literacy n. 文化程度、有文化
competent a. 能胜任的、有能力的
randomly ad. 随机地
defendant n. 被告
entitled a. 有资格的
trial n. 审判
verdict n. 裁定
conscience n. 良心
procedure n. 程序
prohibit v. 禁止
intentional a. 有意的
discrimination n. 歧视
elite n. 精英
blue-ribbon a. 一流的、头等的
eligible a. 有资格的
exempt v. 免除、豁免
justify v. 证明…有道理
unrepresentative a. 不能代表的
abolish v. 废除
landmark n. 里程碑
declare v. 宣布
unconstitutional a. 不符合宪法的
jury system 陪审团制度
regard as 把…看作
be entitled to 享有…权利
letter of the law 法律条文字面意思
direct democracy 直接民主
representative democracy 代议制民主
jury selection procedures 陪审团遴选程序
racial discrimination 种族歧视
antidiscrimination law 反歧视法案
eligible for 有…资格的
exempt from 使免除，使免疫
on the jury list 在陪审团名单之列
at random 随机地
be representative of 代表…
sex discrimination 性别歧视
"""
add_items(2010, "传统阅读 Text 4", "核心词汇与搭配", raw_2010_t4)

# 2010 新题型
raw_2010_new = """
trumpet v. 大声宣告、宣扬
respectively ad. 分别地
lightweight a. 比通常重量轻的
composite n. 复合材料
make a difference 有作用，有影响
naturalistic a. 自然的
formation n. 编队、形成
expend v. 消耗
curl v. 盘绕、缭绕
wingtip n. 翼尖，翼梢
upwash n. 上升气流
drag n. 负重、累赘
propel v. 推进
aeronautics n. 航空学
substantially ad. 实质上、大体上
depart v. 出发
assemble v. 集合
inverted a. 倒转的
favorable a. 有利的
proceed v. 继续进行
consume v. 消耗；消费
carbon-dioxide n. 二氧化碳
nitrogen-oxide n. 一氧化氮
emission n. 排放
cruise v. 以平稳速度行驶
portion n. 部分
knot n. 结、疙瘩（指“问题”）
perception n. 察觉
companion n. 同伴、结伴
nautical a. 航海的
intimate a. 亲近的
peer v. 仔细看、盯着看
separation n. 分开
air-traffic-control n. 空中交通管制
regulation n. 规定
aviation n. 航空
blueprint n. 计划、蓝图
operation a. 操作的
turbulence n. 湍流、强气流
wake n. 航空轨迹
decay v. 消退
diminish v. 变小、减小
investigate v. 调查
co-ordinate v. 协调
destination n. 目的地
reschedule v. 重新安排日程
unsubstantiated a. 未经证实的
skipper n. 机长
"""
add_items(2010, "新题型", "核心词汇与搭配", raw_2010_new)

# 2010 翻译与写作
raw_2010_trans_write = """
sustainability n. 忍受力
concept n. 概念
endure v. 忍耐、忍受
oriented a. 以…为目标的、主要的
confusing a. 令人困惑的
insurance n. 保险
be through 经历
dot-com a. 与互联网相关的
boom n. 激增
burst n. 爆炸
desperate a. 非常需要的
sign on with 与…签约
dilemma n. 进退两难的境地
translate v. 导致、造成
predictably ad. 可以预期地
miserable a. 痛苦的
ceiling n. 天花板
turn the corner 情况好转
receive v. 接待
reception n. 接待
appreciate v. 感激
reciprocate v. 报答
hospitality n. 款待
delegate n. 代表
considerate a. 体贴的
feel at home 在家中般轻松自在
detailed explanation 详尽的解说
get over 克服
culture shock 文化冲击
additionally ad. 此外
fantastic a. 极好的，不可思议的
gain deep insight into 深刻理解…
express gratitude 表达感恩
comfortable lodging 舒适的住宿
well-organized competition 井然有序的比赛
delicious regional snacks 美味的小吃
deep friendship 深厚的友谊
grow v. 增长
moderate increase 缓慢的增长
stagnant a. 停滞的
mobile phone subscriber 手机用户
mobile phone market 手机市场
market environment 市场环境
diagram n. 图表
demonstrate v. 展示，演示
contrastingly ad. 形成鲜明对比的是
reach saturation 达到饱和
population size 人口规模
at a fast rate 以飞快的速度
extra demand 额外的需求
market demand 市场需求
broad market 广阔的市场
purchasing power 购买力
Supply falls short of demand 供不应求
Supply exceeds demand 供过于求
Internet video users 网络视频用户
netizen n. 网民
Internet industry 互联网行业
expand in scale 大规模扩大
"""
add_items(2010, "翻译与写作", "核心词汇与表达", raw_2010_trans_write)

with open(r'f:\obsidiannote\obsidian-\408\数据结构\考研英语二核心词背诵\data_generators\data_2011_2010.json', 'w', encoding='utf-8') as f:
    json.dump(DATA_2011_2010, f, ensure_ascii=False, indent=2)

print('Generated 2011 & 2010 items count:', len(DATA_2011_2010))
