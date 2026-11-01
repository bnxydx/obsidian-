# -*- coding: utf-8 -*-
import json

DATA_2021_2020 = []

def add_items(year, section, subcategory, raw_lines):
    for line in raw_lines.strip().split('\n'):
        line = line.strip()
        if not line or line.startswith('【') or line.startswith('第') or line.startswith('Text'):
            continue
        # Split word and definition
        # Formats:
        # 1. "staff n.全体职员；员工"
        # 2. "jump the red light 闯红灯"
        # 3. "consequence n,结果；后果"
        # 4. "multiple a.多部分的；多种多样的"
        parts = line.split(maxsplit=1)
        if len(parts) == 1:
            continue
        
        # Check if the word itself has multiple words (like a phrase) or single word
        # If parts[1] starts with a part of speech like 'n.', 'v.', 'a.', 'ad.', 'prep.', 'conj.'
        # or 'n,', 'v,', 'a,', 'ad,'
        word = parts[0]
        rest = parts[1]
        
        # Sometimes phrase has spaces: e.g. "set target 设定目标" -> word "set target", rest "设定目标"
        # Let's detect if parts[1] contains Chinese or pos
        # If parts[0] doesn't look like a whole phrase and rest has no pos, let's see:
        # e.g. "jump the red light 闯红灯" -> word="jump the red light", rest="闯红灯"
        # e.g. "at the expense of 以…为代" -> word="at the expense of", rest="以…为代"
        
        # Let's write a robust parser:
        import re
        # Find first Chinese character
        match = re.search(r'[\u4e00-\u9fa5（［]', line)
        if match:
            idx = match.start()
            eng_part = line[:idx].strip()
            cn_part = line[idx:].strip()
            
            # Check if eng_part ends with pos like 'n.', 'v.', 'a.', 'ad.', 'prep.', 'conj.', 'n,', 'v,'
            pos_match = re.search(r'\b(n|v|a|ad|prep|conj|pl)\.?\s*$', eng_part)
            pos = ""
            if pos_match:
                pos = pos_match.group(0).strip('., ')
                eng_word = eng_part[:pos_match.start()].strip()
            else:
                # check if there's pos inside
                # e.g. "criterion n. （pl. criteria）标准；准则"
                m2 = re.search(r'^(.*?)\s+([a-z]{1,4}[\.,])\s*(.*)$', eng_part)
                if m2:
                    eng_word = m2.group(1).strip()
                    pos = m2.group(2).strip('., ')
                    if m2.group(3).strip():
                        cn_part = m2.group(3).strip() + " " + cn_part
                else:
                    eng_word = eng_part
            
            DATA_2021_2020.append({
                "year": year,
                "section": section,
                "category": subcategory,
                "word": eng_word,
                "pos": pos,
                "trans": cn_part
            })
        else:
            DATA_2021_2020.append({
                "year": year,
                "section": section,
                "category": subcategory,
                "word": line,
                "pos": "",
                "trans": ""
            })

# 2021 完形填空
raw_2021_cloze = """
set target 设定目标
staff n. 全体职员；员工
consequence n. 结果；后果
multiple a. 多部分的；多种多样的
component n. 组成部分
distorted a. 扭曲的
inspect v. 检查；查看
jump the red light 闯红灯
cyclist n. 骑自行车的人
infrequent a. 不常发生的
bus lane 公共汽车专用道
hit v. 碰撞；击中
sensitive a. 敏感的；灵敏的
obey v. 服从；遵守
at the expense of 以…为代价
immensely ad. 极端地；非常
tailwind n. 顺风
Bill 把（某人或事物）宣传为
criterion n. （pl. criteria）标准；准则
maywell 很可能；有充分理由
unforeseen a. 未想到的；始料不及的
against prep. 反对
feedback n. 反馈
trick n. 诀窍；窍门
"""
add_items(2021, "完形填空", "核心词汇", raw_2021_cloze)

# 2021 Text 1
raw_2021_t1 = """
reskilling n. 再培训
buzzword n. 时髦用语；流行术语
requirement n. 要求；必要条件
would-be a. 想要成为...的；未来的
forum n. 论坛
timeline n. 时间期限
thorny a. 棘手的
temptation n. 诱惑；诱惑人的东西
massive a. 庞大的；大规模的
pledge v. 承诺；发誓
mismatch n. 不匹配；错配
arguably ad. 可论证地；可以说
languid a. 慢悠悠的；迟缓无力的
pandemic n. （全国或全球性）流行病
respectively ad. 分别；各自
generational a. 一代的
spike v. 猛增；急升
personnel n. 全体人员，职员
furlough v. 使被迫休假；使暂时下岗
laid-off a. 被解雇的
effort n. 有组织的活动
get left behind 落伍；被时代淘汰
in demand 很需要的
let go of sth 放弃
gold standard 在同类事物中作为尺规的好事物
go with sth 接受（看法或计划）
at best 充其量；至多
unemployment rates 失业率
worker shortages 员工短缺
as of 直至；在…时
take an example 举个例子
close a gap 弥合缺口
all concerned 有关各方
cabin staff 空乘人员
startup （使）启动，开始
"""
add_items(2021, "传统阅读 Text 1", "核心词汇与搭配", raw_2021_t1)

# 2021 Text 2
raw_2021_t2 = """
hit v. 达到（某水平）
forecast n. 预测；预报
double v. （使）加倍；（使）增加一倍
Brexit n. 英国脱欧
reverse v. 逆转；反转
self-sufficiency n. 自给自足
requirement n. 要求；必要条件
would-be a. 想要成为...的；未来的
forum n. 论坛
timeline n. 时间期限
thorny a. 棘手的
temptation n. 诱惑；诱惑人的东西
sovereignty n. 主权
feasible a. 可行的；行得通的
vision n. 想象；展望
cover v. 足以负担；足以满足
cover in 用…遮盖；把…铺在…上
livestock farm 畜牧场
caveat n. 提醒；警告
grave a. 严峻的；严重的
drastically ad. 大幅度地；激烈地
consumption n. 食用；（食物的）消耗
intensively ad. 集约型地；集中地
switch v. 转变；转向
dominate v. 占据统治地位
husbandry n. 农牧业
terrain n. 地形；地势；地带
crop n. 农作物；庄稼
arable a. 适于耕种的
convert v. 转变；改变
boost n. 增加
home-grown a. 本国产的
extreme a. 极端的
grain n. 谷物
bulk n. 大部分
calorie n. 卡路里（食物热量单位）
intake n. 摄取量；摄入量
keep pace with 与…并驾齐驱；与…步调一致
make the headlines 成为新闻焦点
talking point 话题；论题
be associated with 与…相关的；相联系的
animal food 动物性食品
animal husbandry 畜牧业
on a commercial basis 商业性地
nature reserve 自然保护区
crop production 作物产量
fresh produce 新鲜农产品
the bulk of 大部分
calorie intake 卡路里摄入量
"""
add_items(2021, "传统阅读 Text 2", "核心词汇与搭配", raw_2021_t2)

# 2021 Text 3
raw_2021_t3 = """
newcomer n. 新来者；新手
considerable a. 相当大的
buzz n. 嘈杂声
dominate v. 占支配地位；（比赛中）占优势
start-up n. 初创企业（尤指互联网公司）
scrap v. 取消；报废
feature n. 特色；特征；特点
feed v. 满足（需要、愿望、欲望等）
talent n. 人才
fate n. 命中注定的事（尤指坏事）
remorseless a. 残酷的；无情的
driven a. （为达到某目的的）有组织的努力
seedling n. 幼苗
complain v. 抱怨；埋怨；发牢骚
partner n. 合伙人
venture n. 风险项目；投机活动
business n. 企业；公司
decline v. 谢绝；婉言拒绝
comment v. 表达意见
admit v. 承认（不好、不快或尴尬的事实）
acquisition n. 收购；购置
stage n. （发展/进展的）时期；阶段
prospect n. 前景；展望
regulator n. 监管者/机构
combined a. 加在一起的
rifle v. 快速寻找；匆忙翻找
prominent a. 显眼的；突出的
momentum n. 动力；势头
tactic n. 策略；手段
from the ground up 从头开始
stay on 保持；继续留下
acqui-hire 人才收购；人才并购
chew up 嚼碎；毁坏
in one's path 挡某人的道
wade into sth 介入；插手
beyond one's reach 鞭长莫及；力所不能及
beside the point 不是重点；无关紧要
a drop in the ocean 沧海一粟；九牛一毛
venture capital 风险资本
"""
add_items(2021, "传统阅读 Text 3", "核心词汇与搭配", raw_2021_t3)

# 2021 Text 4
raw_2021_t4 = """
slice n. （切下的食物）薄片，片
deliberation n. 细想；考虑
extraneous a. 非必要的；无关的
intrusive a. 打搅的；侵扰的
late a. 已故的
correlate v. 相互关联；极为相似
clip n. （电影或电视节目的）剪辑，片段
intuitive a. 凭直觉得到的；直觉的
nature n. 本质；基本特征
critically ad. 极为重要地；很大程度上
dramatically ad. 突然地；明显地
utterance n. 说话方式
interplay n. 相互影响（或作用）
holistic a. 整体的；全面的
detect v. 发现；查明
deception n. 欺骗；蒙骗
preference n. 偏爱的事物
jam n. 果酱
align v. 使一致
rationale n. 全部理由；逻辑依据
objectively ad. 客观（地）
complex a. 复杂的
unleash v. 突然释放；使爆发
circumstance n. 条件；环境
battery n. 一组；一系列
tap v. 利用（已有的资源、知识）
discern v. 识别；了解
comprehend v. 理解
generate v. 产生
gut n. 内心；直觉
hunch n. 预感；直觉
first impression 第一印象
range from... to... 在一定幅度内变化，变动
count backward 倒数
stick shift 换挡杆；手动变速车
on automatic pilot 习惯性地，机械地
figure of speech 修辞格；修辞手段
"""
add_items(2021, "传统阅读 Text 4", "核心词汇与搭配", raw_2021_t4)

# 2021 新题型
raw_2021_new = """
propose v. 提出；提议
initiative n. 方案；计划
outline v. 草拟；画…的轮廓
valid a. 有理的；令人信服的
delay v. 推迟；延期
credibility n. 信誉；可信度
assume v. 假定；臆断
overtly ad. 明显地；公开地
contextualize v. 将…情景化
disagreeable a. 难相处的
subordinate n. 下属
deferential a. 遵从的；顺从的
quarter n. 季度；三个月时间
commitment n. 投身的事
reasoning n. 推理；推论
verbally ad. 口头上
opt v. 选择
race v. （心脏因害怕或激动而）急速跳动
neutral a. 中性的；无强烈感情的
reluctance n. 不情愿；勉强
undercut v. 削弱；使降低效力
counterpart n. 对应的人；对手方
deliberately ad. 从容地；小心翼翼地
panicky a. 焦虑不安的；惊慌的
even a. 平和的；镇静的
tone n. 语气；腔调
gospel n. 绝对真理
well-informed a. 基于大量事实的
tentatively ad. 试探性地；不确定地
understate v. 淡化（程度）
make v. （尽力）达到
assert v. 坚定地陈述
critique n. 评论
project timeline 项目时间表
speak up 大胆地说；公开表态
hold off on 推迟；延缓
voice one's opinion 表达自己的观点
think through 全面考虑
in private 私下地；非公开地
boxing match 拳击比赛
layout 详细解释（计划、论点等）
set a deadline 规定最后期限
make it 让达到预定目标；做到
"""
add_items(2021, "新题型", "核心词汇与搭配", raw_2021_new)

# 2021 翻译与写作
raw_2021_trans_write = """
connection n. 联系；关联
interact v. 交流；沟通
boost n. 增长；提高
instruct v. 指示；通知
commuter n. 上下班往返的人
participant n. 参与者
casual a. 漫不经心的；随便的
interaction n. 交流；沟通
misplaced a. 不合时宜的；给错对象的
tend to 倾向；趋于
feeling of belonging 归属感
strike up 交谈起来；建立友谊
shy away from 回避；逃避
turn out 结果是；证明是
be flattered 被奉承得高兴；感到荣幸
be scheduled for 把…安排在；预定
with the theme of 以…为主题
aim to 目的是；旨在
a wide variety of 种种；多种多样的
engage in （使）从事，参加
enthusiast n. 热衷于...的人；爱好者
be welcome to do sth （用于邀请）欢迎某人做……
insight n. 了解；见解
for one's reference 供…参考
respondent n. 被调查人
on account of 由于；因为
flexibility n. 灵活性；弹性
convenience n. 方便；便利
jog v. 慢跑
in advance 预先；事先
a wide range of 各种各样的
workout n. 锻炼
daily routine 日常惯例；日常生活
apart ad. 不在一起；分离
advisable a. 明智的；可取的
motivated a. 有积极性的
hit the gym 去健身房
fitness equipment 健身器材
dumbbell n. 哑铃
push-up n. 俯卧撑
age difference 年龄差异
fitness center 健身中心
yoga mat 瑜伽垫
treadmill n. 跑步机
aerobics n. 有氧运动
physical fitness 身体素质
independent travel 自由行
self-drive tour 自驾游
exclusive small group tour 独家小团游
self-guided tour 半自助游
group tour 跟团游
"""
add_items(2021, "翻译与写作", "核心词汇与表达", raw_2021_trans_write)

# 2020 完形填空
raw_2020_cloze = """
Parenting n. 养育，抚养
rule-following a. 遵守规则的
sibling n. 兄弟姐妹
composed a. 镇静的，平静的，沉着的
push sb. too far 逼人太甚
lose one's patience 失去耐心
scream at sb 朝某人吼叫
do sb. good 对某人有好处
start over 从头开始
keep in mind 记住
fatigue n. 疲劳，疲乏
self-esteem n. 自尊
consistently ad. 一贯地；始终
inadvertently ad. 无意地，不经意地
model v. 塑造
regulate v. 调节，规定；控制
incredibly ad. 难以置信地；极其
practical a. 实际的，务实的
to the best 尽全力
be faced with 面对；面临
as a result of 由于；作为…的结果
"""
add_items(2020, "完形填空", "核心词汇与搭配", raw_2020_cloze)

# 2020 Text 1
raw_2020_t1 = """
attuned a. 敏锐的
identify v. 识别
house v. 供…居住
asocial a. 不合群的，缺乏社交性的
minimalist a. 极简抽象的
resemble v. 像，类似
chunky a. 矮胖的
marking n. 标记
trapped a. 受困的，被捕获的
release v. 释放
lever n. 杠杆
trial n. 试验
genuine a. 真正的，名副其实的
communal a. 公共的，团体的
reciprocal a. 互惠的
readiness n. 愿意
regular a. 普通的
assume v. 假定，设想
sensitive a. 敏感的
fascinate v. 使着迷
extend to 适用于…
social signal 社交信号
perceive... as... 将…视为…
bond with 与…建立关系
return the favour 回报
minimal design 极简设计
facial feature 面部特征
social cues 社交信号
"""
add_items(2020, "传统阅读 Text 1", "核心词汇与搭配", raw_2020_t1)

# 2020 Text 2
raw_2020_t2 = """
varying a. 不同的
model n. 模型
dynamic a. 推动的，动力的；有干劲的
element n. 要素
sense n. 判断力，理解力
predecessor n. 前任；前辈
slipup n. 失误，疏忽
mind-boggling a. 难以置信的；十分惊人的
plus ad. 外加地；另外
virtually ad. 几乎
rigorous a. 严格的；严厉的
principally ad. 主要地
recruit v. 招募；聘用
cozy a. 舒适的；安逸的
pick n. 选中的人（或物）；挑选出来的人（或物）
depredation n. 掠夺；劫掠
say v. 比方说；假设
stock n. 股份；股票
confirm v. 证明；巩固；加强
motive v. 使有动机，使产生动机；激起（行动）
justify v. 证明…正确（或正当、有理）
go up 增长
on average 平均
publicly traded corporation 上市公司
up one's game 做出更好表现；做出更多努力
relative to 相对于
contribute to 有助于，促成；是…的部分原因
ever before 以前；以往任何时候
supply chain 供应链
one way or another 用某种方法；不管怎样
beyond this 除外
day-to-day work 日常工作
be all about 重要的［问题］是…
rip sb. off 剥削；欺诈；敲…竹杠
by most measures 从大多数方面来看；以多数标准衡量
in one's interest 符合…的利益；有助于
at the expense of 在牺牲…的情况下
tie sth. to sth. 使…紧密贴合，使…连接
build up 逐渐增大，增强
"""
add_items(2020, "传统阅读 Text 2", "核心词汇与搭配", raw_2020_t2)

# 2020 Text 3
raw_2020_t3 = """
beacon n. 引路人，指路明灯
restriction n. 限制条例
suspend v. （使）暂停
enforcement n. 执行，实施
demise n. 终止；死亡
centrepiece n. （最佳的/最具吸引力的）部分
overrule v. 否决
decision n. 决议
levy v. 征（税）
reinstate v. 恢复（法律、机构或条例等）
employ v. 使用，采用
contentious a. 引起争议的
vulnerable a. 易招致抨击的，易受攻击的
inevitably ad. 必然发生地
cheating n. 舞弊（指做违法乱纪之事）
toxic a. 有毒的
deem v. 认为，相信
mild a. （惩罚等）轻微的，不严重的
reversal n. （过程、政策或趋势的）逆转
issue n. 议题
extend v. 延伸，扩展
lever n. （用作施加压力等的）手段，方法
deliver v. 递送（货物等），文中延伸为“带来（影响）”
stroke n. 中风
dementia n. 痴呆
asthma n. 哮喘
councilor n. 议员
effort n. 有组织的活动，特别行动
regulation n. 法规；条例
compliance n. 遵从，遵守
introduce v. 采用，推行
supervision n. 监督，管理
hail as 称赞…为…
roll out 开展［新的政治运动］；正式推出［新的产品］
conservation city council 保守派掌控的市议会
election campaign 竞选运动
legal battles 司法拉锯战
be biased against 对…有偏见/不公的
spark intense opposition from 引发…激烈反抗
do everything but do 除了做…其他该做的都做了
clean up 治理［污染］
follow regulation 遵守法规
"""
add_items(2020, "传统阅读 Text 3", "核心词汇与搭配", raw_2020_t3)

# 2020 Text 4
raw_2020_t4 = """
inhabit v. 占据，留在
cubicle n. 小房间，隔间
entitle v. 使有权利，使有资格
Millennial n. 千禧一代
catchword n. 关键词；代表性口号
pragmatist n. 实用主义者
impressionable a. （尤因年轻而）易受影响的
assuage v. 缓和，减轻
underlying a. 根本的，潜在的
balance n. （债务的）余款，结欠
senior n. 毕业班学生
secure a. 稳定的，稳固的
dedicated a. 有奉献精神的，满腔热忱的
flexibility n. 灵活性，弹性
associate a. 副的；准的
financial a. 财务的；金融的
commonly-accepted ［为人们］普遍接受的
give or take 相差不到…，出入至多…
hit the streets ［商品］大量上市
fairly or not 无论是否恰当
career counselor 职业顾问
train wreck 火车失事
take a chance 冒险，碰运气
job security 工作保障/稳定
serve the greater good 服务于宏大的高尚事业
brand manager 品牌经理
gig economy 零工经济
risk averse 不愿冒险的，风险规避
"""
add_items(2020, "传统阅读 Text 4", "核心词汇与搭配", raw_2020_t4)

# 2020 新题型
raw_2020_new = """
compliment n. 赞扬，称赞
tailor v. 专门制作；调整
tight-lipped a. 紧闭双唇，忍住不说的
consistently ad. 一贯地，始终如一地
upfront a. 坦率的，诚实的
studiously ad. 有意地，故意地
stash v. 隐藏
receptive a. 乐于倾听他人意见的
stray a. 偶尔发生（或遇到）的；零星的
valid a. 足够重视的，值得说或做的
genuine a. 真正的，名副其实的
confidant n. （可吐露秘密的）知己
horizon n. （思想，经验等的）范围；眼界
minimal a. 极少的，最少的
feedback n. 反馈意见或信息
exceptional a. 杰出的，卓越的
engender v. 产生，引起
overdo v. 做得过分，过火
verbalize v. 用言语或文字表达
straightforward a. 直截了当的
land v. 成功，达到预期效果
much less 更不用说，更何况
on one's side 在某人一边，支持某人
have a bone to pick with sb 对某人生气，想与之理论
an open book 一览无遗的事物
hear out 听完，仔细倾听
be available to 对…是可获取/利用的
premature birth 早产
untimely death 早逝
a response to 对…做出反应/响应
absence of 缺乏
engage sb. in sth 使某人参与某事
meet up with 结识，与某人碰面
go a long way 帮助很大，作用很大
pull off 做成，完成（困难的事情）
deal with sb 与某人打交道
watch out for sth 密切留意
small talk 闲聊，寒暄
dig into sth 探究，细查
"""
add_items(2020, "新题型", "核心词汇与搭配", raw_2020_new)

# 2020 翻译与写作
raw_2020_trans_write = """
incredible a. 难以置信的；极好的
lesson n. 经验，教训
stop v. 击败；阻挡
otherwise ad. 与此不同地，相反地
strong a. 坚强的，强大的
unexpected a. 以外的，意想不到的
go through 经历；遭受
be up to sb 由……决定；是……的职责
be meant to 应当或必须做某事
only if 只有
tour / trip / travel 旅游
historical site 历史遗迹/名胜
archaeological discovery 考古发现
tip / advice / suggestion 建议
life-size a. 与真人/实物大小一样的
warrior n. （尤指旧时的）战士，勇士
breathtaking a. 激动人心的，惊人的
public holidays 公共假日
informative a. 有用信息的，增长见闻的
suit one's taste 符合某人的口味，爱好
offer a glimpse into 短暂体味
glimpse n. 一眼，一瞥
pie chart 饼状图
account for 占…（比例）
illustrate v. （用例子或图表）阐明
mobile reading 手机阅读
gain / acquire knowledge 学习知识
obtain information 获取信息
kill time 消磨时间
respondent n. 受访者，调查对象
expand one's horizons 拓宽眼界，开阔视野
popularization n. 普及，推广
intense a. 激烈的，剧烈的
gain an edge over 胜过…
applicant n. （求职或进入高校的）申请人
be bound to 一定会，必然会
rise in popularity 变得更受欢迎
cater to 迎合
have also played a part in 在某方面也起到了一定的作用
play a part / role 扮演一定的角色；发挥一定的作用
portable a. 便携的
digital reading 数字阅读
mobile device 移动设备
intellectual curiosity 求知欲
decent salaries 可观的薪资
hit a career plateau 遭遇职业瓶颈
rapid economic growth 经济发展迅速
numerous job opportunities 大把工作机会
foreign-educated Chinese students 海外留学生
beloved family members and bosom friends 亲朋好友
enormous potential for career development 职业发展潜力巨大
be optimistic about job prospects 对就业前景乐观
be pessimistic about job prospects 对就业前景悲观
"""
add_items(2020, "翻译与写作", "核心词汇与表达", raw_2020_trans_write)

with open(r'f:\obsidiannote\obsidian-\408\数据结构\考研英语二核心词背诵\data_generators\data_2021_2020.json', 'w', encoding='utf-8') as f:
    json.dump(DATA_2021_2020, f, ensure_ascii=False, indent=2)

print('Generated 2021 & 2020 items count:', len(DATA_2021_2020))
