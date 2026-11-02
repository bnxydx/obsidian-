# -*- coding: utf-8 -*-
import json, re

DATA_2022_2026 = []

def add_items(year, section, raw_lines):
    for line in raw_lines.strip().split('\n'):
        line = line.strip()
        if not line or line.startswith('【') or line.startswith('第') or line.startswith('Text'):
            continue
        
        # Match the first Chinese character or punctuation
        match = re.search(r'[\u4e00-\u9fa5（［]', line)
        if match:
            idx = match.start()
            eng_part = line[:idx].strip()
            cn_part = line[idx:].strip()
            
            # Check pos
            pos_match = re.search(r'\b(n|v|a|ad|adj|prep|conj|pl)\.?\s*$', eng_part)
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
            
            DATA_2022_2026.append({
                "year": year,
                "section": section,
                "category": "核心词汇与搭配",
                "word": eng_word,
                "pos": pos,
                "trans": cn_part
            })
        else:
            DATA_2022_2026.append({
                "year": year,
                "section": section,
                "category": "核心词汇与搭配",
                "word": line,
                "pos": "",
                "trans": ""
            })

# ================= 2022 年 =================
# Text 1
raw_2022_t1 = """
sunny a. 阳光充足的；艳阳高照的
roam v. 徜徉；闲逛；漫步
windswept a. 迎风的；当风的；无遮挡的
acre n. 英亩
rest v. 休息；放松
shade n. 阴凉处；背阴处
park v. 停放（车辆）
cow n. 母牛；奶牛
random a. 随机的；随意的
bet v. 下赌注；打赌；敢说
considerably ad. 非常；很；相当多的
replacement n. 接替者；替代者
by design 由于精心设计；有计划地；有意地
bet that (以钱、物等)打赌断定/确信…
the next big thing 下一个风口/趋势；明日之星
regular shopper 常客；老顾客
debut n. (新产品的)首次亮相
shelf n. 架子；搁板
dozen n. (一)打；十二个
label v. 贴标签于；用标签标明
regenerative a. 再生的；更生的
cultivate v. 培育；培养
trap v. 收集；吸收；捕获
market v. 推销；促销
make one's debut 首次亮相
as much as 像…那么多；多达
rich soil 肥沃土壤
greenhouse gas 温室气体
market sth as 将某事物作为…投放市场；将某事物宣传/推销为…
harvest v. 收获
draw v. 吸引；招引；引来
worm n. 蠕虫
cricket n. 蟋蟀；蛐蛐
waste n. 粪便
fertilize v. 施肥于
hen n. 母鸡
forage v. 觅(食)；四处搜寻(食物等)
feed n. (家畜的)饲料
disposal n. 去掉；清除；处理
cover crop 覆土作物；肥田作物；绿肥
forage for sth 觅食；四处搜寻食物
push n. 推销运动；广告活动
test n. 检验；考验
premium a. 高昂的；优质的
offering n. (供出售的)产品
barely ad. 不超过；只有；仅仅
dismiss v. 对……不屑；拒绝考虑；否定
niche a. (产品)针对特定小群体的
probiotic n. 含益生菌的食品
explode v. 突然出现；迸发；突然演变为
category n. (人或事物的)类别，种类
rollout n. (产品或服务的)正式推出；(新产品的)推出市场
floodgate n. 防洪闸门；泄水闸门
broccoli n. 绿菜花；西兰花
setback n. 挫折；阻碍；退步
promotional a. 广告宣传的；推销的
be dismissed as 被贬低/摒弃为
niche product 特殊定向产品；利基产品；小众产品
explode into sth 突然演变成某事物
open the floodgates for 解除对某事物的限制；引发更多类似事件
and beyond 及其他人或事物；及以后的任人或事物
tough a. 艰难的；棘手的
associate a. 非正式的；准的；副的
minimal a. 极小的；极少的；最小的
protein n. 蛋白质
a hard sell 滞销品；不容易被接受的事物
attribute n. 属性；性质；特征
free-range a. (家畜，尤指家禽)自由放养的
GMO n. 转基因生物
pasture n. 牧场；牧草地
raise v. 养育；培养
embrace v. 欣然接受；乐意采纳
survey n. 民意调查；民意测验
concerned a. 关心的；关切的；关注的
chalk v. 记下(某人所做的事、所欠的账等)
signal v. 表达；表示；显示
absolutely ad. 完全地；无保留地；极其
alter v. (使)改变；更改；改动
beyond prep. 超出；非……可及；无法
chalk sth up to sth 把某事物归因于另一事物
"""
add_items(2022, "传统阅读 Text 1", raw_2022_t1)

# Text 2
raw_2022_t2 = """
retirement n. 退休；退休年龄
upend v. 使颠倒；颠覆
workforce n. 劳动力
opt to do sth 选择做某事
threaten to do sth 可能造成某不利之事
settle down 过安定的生活
culprit n. 引起问题的事物；问题的起因
fulfilment n. 满足感
depression n. 抑郁症；忧郁
respondent n. 调查对象
evolve v. 逐步发展；逐渐演变
drive v. 驱使
stay mentally fit 保持精神健康
be tied to sth 与某事相关
make ends meet 使收支相抵；勉强维持生计
pattern n. 模式
segment n. 部分
boomer n. 生育高峰期出生的人；婴儿潮一代
double v. (使)加倍
the share of 的比例，份额
expect sb to do sth 预计某人会做某事
labor force 劳动力
an all-time high 空前的高点
boost v. 使增长
preserve v. 保护；保存
overall a. 总体的
secure v. (尤指经过努力)获得；取得
maximize v. 使增加到最大限度
contribution n. 定期缴款
life span 寿命
nest egg 备用的钱；储备金
do sth in anticipation of 因预料到某事而做某事
unfortunately ad. 令人遗憾地
ultimately ad. 最终；最后
emotional a. 感情的；情感的；情绪的
be worried about sth 担忧某事
set long-term goals 设定长期目标
"""
add_items(2022, "传统阅读 Text 2", raw_2022_t2)

# Text 3
raw_2022_t3 = """
encounter v. 遭遇；遇到
trick v. 欺骗；欺诈
frustrated a. 受挫的；沮丧的
membership n. 会员身份；成员资格
subscription n. 订阅；订购
seamless a. 无缝的；无停顿的
sign-up n. 注册；签约
cancel v. 注销；终止
transparent a. 易懂的
complicated a. 复杂的；难懂的
impair v. 损害；削弱
pattern n. 模式；方式
coin v. 创造(新词语)
catch-all a. 含义甚广的；笼统的
practice n. 通常做法；行为
manipulate v. (暗中)控制；操纵
identify v. 找到；发现
roach n. 蟑螂
intuitive a. 易懂的；使用简便的
user experience 用户体验
user interface 用户界面
range from...to... 包括从…到…之间的各类事物
get out 离开；从…出来
page n. 页面；版面
employ v. 应用；运用
prevalent a. 普遍存在的；盛行的
engender v. 导致；造成
aware of sth 意识到，明白…
gray area 灰色区域；中间地带
compliance n. 合规；遵从
coder n. 编码员
marketer n. 市场商人；市场营销人员
checkout n. 付款处；结账
promotion n. 促销活动；广告宣传
deception n. 欺骗；欺诈
a line between...and... 两者之间的界限，区别
engage in 从事；参加
responsible for sth 对…负责
play a role 发挥作用
ambiguity n. 模棱两可；不明确
announce v. 宣布；宣告
ensure v. 担保；确保
mislead v. 误导；使误信
prohibit v. (尤指以法令)禁止
Attorney General 司法部长
data privacy right 数据隐私权
opt out 决定退出；选择不参与
promulgate v. 颁布；公布
accountability n. 负有责任
business community 工商业界；企业界
hold sb accountable 让某人负有责任
"""
add_items(2022, "传统阅读 Text 3", raw_2022_t3)

# Text 4
raw_2022_t4 = """
ethics n. 伦理学；道德学
unsure a. 无把握；不确知
actually ad. 的确；真实地；事实上
contrived a. 设计的；人为的
unreliable a. 不可靠的；不能信赖的
self-report n. 自陈报告
lasting a. 持久的
rely on 依赖；依靠
at least 至少
have effect 产生…的影响
investigate v. 研究；调查
session n. 上课时间
variable a. 多变的；易变的
unstable a. 不稳定的；易变的
measurable a. 可测量的
largely ad. 在很大程度上；主要地
optionally ad. 非强制地
anonymize v. 使匿名
focus on 集中(注意力、精力等)于…
charitable giving 慈善捐赠
predict v. 预测
intervention n. 干涉；干预
donation n. 捐献
contain v. 包含；含有
decrease v. 降低
steady a. 稳定的
duration n. 持续时间；期间
remain v. 保持不变
differ from 与…不同
a range of 一系列…
blood donation 献血
hold steady 保持稳定
note v. 指出；特别提到
reversible a. 可逆转的
nudge n. 轻推；激起
rule out 把…排除在外
confounding variable 混杂变量
Easy come easy go 来得快，去得也快
suspect v. 推测；认为
vegetarianism n. 素食主义
achievable a. 可实现的
emotional a. 情感的；情绪的
rouse v. 使产生兴趣
rational a. 理性的
probe v. 探究
exposure n. 接触；体验
play a role 发挥…的作用
eat one's words 食言；收回前言
"""
add_items(2022, "传统阅读 Text 4", raw_2022_t4)


# ================= 2023 年 =================
# Text 1
raw_2023_t1 = """
quest n. 寻求；追求
homeowner n. 房主
shortcut n. 捷径
pay the price 付出代价；吃苦头
square meter 平方米
circle n. 圈子；界
fake grass 人造草坪
event n. 公开活动；社交场合
ethos n. 理念；精神特质
horticultural a. 园艺的
society n. 社团；协会
biodiversity n. 生物多样性
launch v. 发起；推出
in line with 与……一致
support v. 维持……的生存
alleviate v. 减轻；缓解
flooding n. 水灾；洪水泛滥
cool v. (使)变凉，冷却
campaigner n. 活动家；运动参加者
cut through 刺穿；戳穿
greenwash n. 绿色外衣；环保幌子
artificial grass 人造草坪
follower n. 关注者；粉丝
petition n. 请愿书
ecological a. 生态的
signature n. 签名；署名
mow v. 割；修剪
weed n. 杂草；野草
weed killer 除草剂
treatment n. 处理(清理、保护等)
lay v. 铺放；铺设
shrub n. 灌木
gather v. 搜集；收集
respond v. 回应；回复
legislate v. 立法；制定法律
comply with 遵守；依从
safeguard n. 保护措施；保障措施
in place 在运作的；就位的
sustainable a. 可持续的
drainage n. 排水；放水
sustainable drainage 排水的可持续性
serve to do sth 有助于做某事
public authority 公共当局
sustainable alternative 可持续的替代方案
"""
add_items(2023, "传统阅读 Text 1", raw_2023_t1)

# Text 2
raw_2023_t2 = """
absurd a. 荒唐的；不合理的
plug v. 填补；补足
chronic a. 长期存在的
delivery n. 递送的货物
line up 排成一行；排队
redwood n. 红杉；红木
maintenance n. 维护；保养
backlog n. 积压的工作
trail n. 路线；路径
crumble v. 败落；损坏
privatize v. 使私有化
commercialize v. 使商业化
campground n. 露营地
cure-all n. 万灵药；灵丹妙药
portion n. 部分
service n. 公共事业机构
privatization n. 私有化
drumbeat n. 击鼓声
commercial drumbeat 商业喧嚣
overwhelm v. 淹没；使应接不暇
chronically ad. 长期地
starve v. 使极其缺乏
taxpayer n. 纳税人
significant a. 数量相当大的
intact a. 完好无损的
respondent n. 回答者；受访者
value n. 用途；好处
extensive a. 各种各样的
sequestration n. 封存
artistic a. 艺术的；艺术家的
alive a. 继续存在的
jurisdiction n. 管辖区域
site n. 遗址；原址
bring sth to life 使某事物更生动
shoestring n. 小额资本；零星资金
on a shoestring 以极少的钱
flat a. 数量不变的；固定的
inflation n. 通货膨胀
onetime a. 一次性的
meanwhile ad. 相比之下
"""
add_items(2023, "传统阅读 Text 2", raw_2023_t2)

# Text 3
raw_2023_t3 = """
lead v. 指挥；主持
factoid n. 有趣消息；趣闻
ostrich n. 鸵鸟
erase v. 抹去；删除
save v. 保存
folder n. 文件夹
deteriorate v. 恶化；退化
communications technology 通信技术
hard drive 硬盘
cognitive a. 认知的；感知的
offload v. 卸载
data bank 数据库；资料库
upside n. 好的一面
individual facts 个别事实
memorization n. 记住
conceptual a. 概念的
all that much 那么多
memorize v. 记忆；记住
experimental a. 科学实验的
interfere v. 干涉；干预
interfere with sth 干扰某物
surf v. 浏览；漫游
savvy a. 有经验的；知识渊博的
neuroscience n. 神经科学
reliance n. 依赖；依靠
imagine v. 料想；认为
outweigh v. 大于；超过
observe v. 说；评论
"""
add_items(2023, "传统阅读 Text 3", raw_2023_t3)

# Text 4
raw_2023_t4 = """
paradoxical a. 自相矛盾的
detached a. 不动感情的；客观的
paradox n. 自相矛盾
personal a. 个性的；性格的
adolescence n. 青春期；青春
dependent a. 依赖的；不自立的
grown-up n. 成年人；大人
independent a. 有主见的
compliant a. 顺从的
rebellious a. 叛逆的；桀骜不驯的
go hand in hand 密切关联；相伴随行
concentrate on 专注于
rebellious traits 叛逆特性质
fill out 填写
questionnaire n. 问卷
altruistic a. 利他的；无私的
sacrifice one's own interests 牺牲某人自己的利益
stay out late 晚归
fade away 逐渐消逝；逐渐消失
hold v. 持续有效
prosocial behavior 亲社会行为
unselfishly ad. 无私地
correlation n. 相关；关联
positive correlation 正相关
prosociality n. 亲社会性
rebelliousness n. 叛逆性
underlie v. 是……的原因
apparently ad. 看来；似乎
contradictory a. 矛盾的
sensitivity n. 敏感性；灵敏度
reward sensitivity 回报敏感性
involve doing sth 需要做某事
measure v. 衡量；评估
outweigh risk 覆盖风险
social rewards 社交奖励
risk-taking n. 冒险
age v. 年龄增长；变老
couch n. 长沙发
"""
add_items(2023, "传统阅读 Text 4", raw_2023_t4)


# ================= 2024 年 =================
# Text 1
raw_2024_t1 = """
cog n. 齿轮
thing n. 形势；情况
gain n. 财富(或资源)的增长
evenly ad. 平均地；均等地
share v. 分配；分摊
millionaire n. 百万富翁；富豪
billionaire n. 亿万富翁；巨富
gig a. (尤指临时的)工作
gig worker 零工工人
undercut v. 削弱；暗中破坏
automation n. 自动化
sustainable a. 可持续的
prosperity n. 繁荣；富足
boost v. 促进；推动
productivity n. 生产率；生产力
sector n. 领域；行业
health care 医疗保健
construction n. 建筑业
embrace v. 欣然接受(或支持)
benefit n. 好处；益处
roadblock n. 障碍
deploy v. 有效使用；利用
disruption n. 扰乱；打乱
transformative a. 变革性的
tremendous a. 巨大的；极大的
buy-in n. (对政策或变更的)认可，接受
resentment n. 愤恨；不满
simmer v. 充满，郁积着(难以控制的感情)
perceive v. 认为；将……视为
elite n. 精英；上层人士
a handful of sb 少数人(或物)
prosperous a. 繁荣的；富足的
institution n. 机构；学会
roughly ad. 大约；差不多
concentrated a. 密集的；集中的
account for (数量上、比例上)占
asset n. 资产；财产
capability n. 能力；才能
commercialization n. 商业化
geographical a. 地域的；地理的
disparity n. 差异；悬殊
soar v. 急升；猛增
foster v. 促进；助长
unrest n. 动荡；动乱
hold back 阻碍；妨碍
regional a. 区域的；地区的
lie in 在于；位于
somehow ad. 以某种方式(或方法)
loosen v. 放宽；使变松
stranglehold n. 压制；绝对控制
Big Tech 大型科技公司
agenda n. 议题；议程
federal funding 联邦资金
tech giant 科技巨头
immediate a. 立即的；立刻的
broaden v. 拓宽；使扩大
conceive v. 构想；设想
manufacturing n. 制造业
"""
add_items(2024, "传统阅读 Text 1", raw_2024_t1)

# Text 2
raw_2024_t2 = """
construction n. 建筑；建筑业
crisis n. 危机；危急关头
failure n. 未能做到
forestry n. 林业；造林术
body n. 团体；机构
call for 要求；呼吁
reliance n. 依赖；依靠
timber n. 木材；原木
import n. 进口；进口商品
currently ad. 目前；当下
requirement n. 需求；需要的东西
home-grown a. 自产的；本国产的
fresh a. 新近的；新近出现的
incentive n. 激励；刺激措施
landowner n. 土地拥有者
boost v. 使增长；促进
carbon n. 碳
executive n. 主管；执行官
invest v. 投资
domestic a. 本国的；国内的
leave v. 使处于某种状态
fluctuate v. 波动；起伏不定
low-carbon a. 低碳的
home n. (可买卖的)房子，住宅
leader n. 处于领先地位的人
certify v. 确保；保证
sustainably ad. 可持续地
manage v. 经营管理(土地)
Scottish a. 苏格兰的
position n. 处境；状况
complex a. 复杂的
range v. 包括(各类事物)
outdated a. 过时的；陈旧的
perception n. 看法；认知
productive a. 生产性的；有生产力的
decimation n. 大量毁坏；严重破坏
squirrel n. 松鼠
encompass v. 包含；包括
hesitation n. 犹豫；不情愿
on behalf of sb 在某人一方的；由某人做的
deliver v. 提供；产生
financial a. 财政的；财务的
rural economy 乡村经济
net-zero strategy 净零排放战略
rewilding n. 再野化；恢复原始样貌
solely ad. 仅；单独地
biodiversity n. 生物多样性
secure a. 可靠的；稳定的
state v. 声明；表明
on the ground 切实地
impetus n. 动力；推动力
aspiration n. 抱负；志向
ensure v. 保证；确保
meet v. 满足；使满意
"""
add_items(2024, "传统阅读 Text 2", raw_2024_t2)

# Text 3
raw_2024_t3 = """
convince v. 说服；使相信
turn over 移交(控制权、责任)
complete a. 完全的；彻底的
force v. 强迫；迫使
former a. 前任的；曾经当过……的
risk n. 风险；危险
association n. 协会；联盟
physician n. 医生；(尤指)内科医生
substantial a. 实质上存在的；实质性的
impairment n. 障碍；缺陷
imply v. 暗示……为必然结果
threat n. 构成威胁的人(或事物)
privilege n. 特权；特殊待遇
ignore v. 忽视；对……不予理会
desirable a. 值得去做的；可取的
ethical a. 合乎道德的；合乎道德规范的
notify v. 申报；报告
motor a. 有引擎的；机动的
require v. 规定；要求
mandate v. 命令；强制要求
breach n. 违背；违反
confidentiality n. 保密性；机密性
liability n. 责任；义务
penalty n. 惩罚；刑罚
accordance n. 一致；和谐
counsel v. 建议；劝告
address v. 考虑处理；解决
piecemeal ad. 零散地；不成体系地
profession n. 职业人士；专业人员
gerontologist n. 老年学专家
administration n. 管理部门；行政机关
official n. 要员；官员
automotive a. 汽车的；机动车的
engineer n. 工程师；设计师
national a. 全国的；全国性的
institute n. 研究所；协会
work v. 产生预期效果；有效
license n. (官方)许可证，执照
renewal n. 展期；有效期延长
mandatory a. 强制的；必须遵守的
be associated with 与……有关联
fatal a. 致命的
crash n. 撞车；碰撞
vision n. 视力；视觉
produce v. 引起；导致
combine v. 同时做；兼做
see v. 会见；与……见面
afford v. 负担得起；付得起
setting n. 设定位置；调节点
pedal n. (汽车或机器的)踏板
self-driving a. 自动驾驶的；无人驾驶的
solve v. 解决；处理
avoid v. 避免；防止
pose v. 造成；引起
algorithm n. 算法；运算法则
comfortably ad. 舒适地；轻松地
"""
add_items(2024, "传统阅读 Text 3", raw_2024_t3)

# Text 4
raw_2024_t4 = """
chance n. 可能性
related a. 相关的；有关的
probably ad. 很可能；大概
mental health 心理健康
fitness n. 健身
tracker n. 跟踪仪；追踪器
connected a. 连接的；相连的
device n. 装置；设备
take advantage of 利用某物
keep track of 了解……的动态
in some shape or form 以某种形式
review n. 审查；检查
available a. 可获得的；可购得的
launch v. 上市；发行
a great deal 大量；很多
input v. 输入(信息)
safeguard v. 保护；捍卫
existing a. 现存的；现行的
privacy n. 隐私
insurance n. 保险
portability n. 可转移性；可移植性
accountability n. 负有责任；责任性
act n. 法案；法令
primarily ad. 主要地；通常
clinic n. 诊所；门诊部
store v. (在计算机里)储存
record n. 记录；档案
track v. 跟踪；追踪
wearable n. 可穿戴设备
typically ad. 通常；一般
additional a. 额外的；附加的
in place 到位的；已就绪的
potentially ad. 潜在地；可能地
monetize v. 赚钱；获利
authorize v. 授权；批准
anticipate v. 预见；预计
commission n. 委员会
investigation n. 调查；侦查
allege v. 指控；声称
complaint n. 指控；控告
express a. 明确表达的；明白表示的
sensitive a. 敏感的；限制透露的
fertility n. 生育能力；繁殖力
third party 第三方
settle v. 结束；解决
consent n. 同意；准许
order n. (法院的)决议，指令
affirmative a. 同意的；赞成的
instruct v. 告知；通知
delete v. 删去；删除
section n. (法律的)条，款，项
empower v. 授权
initiate v. 开始实施；发起
enforcement n. 强制执行；强行实施
deceptive a. 欺骗性的；误导的
practice n. 实际行动；实践活动
unjustified a. 不公正的；不正当的
handling n. 处理；对待
rate n. 速度；进度
hit v. 到达(某地)
demonstrate v. 证明；证实
immense a. 极大的；巨大的
prospect n. 成功的机会；前景
legislation n. 立法；制定法律
commentator n. 评论家
comprehensive a. 全面的；详尽的
in the short term 短期内
implement v. 执行；实施
shore up 支撑；加强
generate v. 生成
forefront n. 最前线；最重要的位置
at the forefront 位于最前列；处于领先地位
effort n. 行动；活动
pass v. 经表决通过
"""
add_items(2024, "传统阅读 Text 4", raw_2024_t4)


# ================= 2025 年 =================
# Text 1
raw_2025_t1 = """
customer n. 顾客；客户
historically ad. 在过去；以往
tip v. 给小费；付小费
assume v. 假定；认为
earn v. 赚得；挣钱
income n. 收入；收益
via prep. 通过；凭借
server n. 侍者；服务员
minimum a. 最低的；最小的
wage n. 工资；工钱
range n. 一系列
business n. 企业；商业机构
process v. 处理；审核
purchase n. 购买；采买
digital a. 数字的；数码的
payment n. 付款；支付
system n. 系统
prompt v. 提示；提醒
previously ad. 以前；先前
request n. 要求；请求
connected a. 关联的；相关的
norm n. 规范；行为标准
used to 过去；曾经
determine v. 决定；影响
receive v. 得到；接受
conclusion n. 结束；结尾
deliver v. 递送；传送
timing n. 时机的掌握
reward v. 奖励；奖赏
incentive n. 激励；刺激
provide v. 提供；给予
common a. 常见的；普遍的
beforehand ad. 预先；提前
automatically ad. 自动地
add v. 添加；增加
prevalence n. 普遍存在；广泛应用
device n. 仪器；设备
explain v. 解释；说明
creep v. 悄然渗透；渐渐侵入
routinely ad. 惯常地；例行地
menu n. 功能选项单；菜单
default n. 默认状态；系统预设状态
option n. 选择；选择权
well ad. 相当；远远地
owe v. 欠(债)；欠(账)
amount n. 金额
expectation n. 预期；期待
vital a. 必不可少的；极其重要的
supplement v. 增补；补充
notably ad. 以令人注意的方式
primarily ad. 主要地；首要地
ensure v. 保证；确保
ban v. 禁止；取缔
movement n. 积极的改变趋势
largely ad. 在很大程度上；多半
fizzle v. 逐渐失败；草草结束
fizzle out 结果失败；终成泡影
succumb v. 屈服；抵挡不住
temptation n. 引诱；诱惑
frustrated a. 恼怒的；失望的
ask for 要；要求
emphasize v. 使明显；使突出
coercive a. 强制的；胁迫的
generous a. 慷慨的；大方的
dissociate v. 脱离；与……分开
generosity n. 慷慨；大方
essential a. 至关重要的；必不可少的
diligence n. 勤奋；勤勉
optional a. 可选择的；非必须的
in advance 提前；预先
contribute to 为……作贡献；有助于……
diversification n. 多样
emergence n. 出现；兴起
guarantee v. 确保；保证
reflect v. 反映；显示
"""
add_items(2025, "传统阅读 Text 1", raw_2025_t1)

# Text 2
raw_2025_t2 = """
establish v. 建立；创立
health n. 医疗；卫生
visionary a. 有创见的；有远见卓识的
timely a. 及时的；适时的
meet v. 满足；使满意
dominant a. 首要的；主要的
population n. 全体居民；全体国民
serve v. 为(一地区、一群人)提供产品(或服务)
model n. 模式；模型
out of date 过时的；陈旧的
life expectancy 预期寿命
cancer n. 癌；癌症
infant n. 婴儿；幼儿
mortality n. 死亡数量；死亡率
lag v. 落在后面；滞后
peer n. 同等社会地位(或能力)的人
waitlist n. 等候者名单
healthcare n. 医疗保健服务
increasingly ad. 越来越多地；不断增加地
inaccessible a. 难以达到的；不易获得的
opt v. 选择；挑选
squeeze v. 压缩，减少(金钱等)
investment n. 投资
workforce n. 全体员工；全体从业人员
breaking point (压力的)极限，崩溃点
acute a. 严重的；剧烈的
answer n. 解决办法；答案
rehearse v. 照搬；重复
divert v. 转变(方向或用途)
manage v. 管理；处理
invest v. (把资金)投入
community care 社区护理服务
primary care 初级保健护理；初级医疗
reliance n. 依赖；依靠
capacity n. 容纳能力；办事能力
live with 忍受；容忍
long-term a. 长期的；长远的
condition n. 疾病；健康问题
strategy n. 战略；策略
reform n. 改革；变革
fail v. 失败；未能(做到)
meaningful a. 重要的；有意义的
think tank 智库；智囊团
programme n. 计划；方案
entitle v. 给……命名(或题名)
reimagine v. 重新构想；重新设想
call for 呼吁；公开要求
honest a. 坦率的；坦诚的
urgent a. 紧迫的；迫切的
rethink n. 反思；重新思考
hospital-centric a. 以医院为中心的
retain v. 保持；保留
maximise v. 使增加到最大限度
fix v. 维修；修理
estimate v. 估计；估算
account for (数量上、比例上)占
outcome n. 结局；结果
health outcome 健康结局
socialise v. 参加社交活动；交际
determinant n. 决定性因素
worse ad. 更糟糕的是；更倒霉的是
obesity n. 肥胖；肥胖症
scrap v. 废除；取消
price tag 费用；花费
diabetes n. 糖尿病
power n. 权力；职权
resource n. 资源(指钱、物、人等)
distribute v. 分发；分配
function n. 功能；职能
remain v. 遗留；继续存在
responsible a. 有责任的；负责……的
create v. 引起；导致
understanding n. 了解；熟悉
deficiency n. 缺乏；不足
barely ad. 几乎不；几乎没有
boost v. 增加；提高
lighten v. 减轻；减少
reinforce v. 加强；巩固
readjust v. 重新调整；重新调节
restructure v. 调整结构；重组
resume v. 重新开始，继续
suspend v. 暂停；中止
introduce v. 推行；实施
pay due attention to 对……给予充分的关注
reevaluate v. 重新评估；再评价
exercise v. 行使；运用
sense of responsibility 责任感
"""
add_items(2025, "传统阅读 Text 2", raw_2025_t2)

# Text 3
raw_2025_t3 = """
heat n. 炎热天气；高温
proliferate v. 激增；猛增
spell out 清楚地说明；详细地解释
official n. 官员；高级职员
issue v. 公布；发出
warning n. 警告；预警
alert v. 向……发出警报；使警觉
institution n. 社会机构；组织
call for 规定；要求
set aside 留出；拨出
ward n. 病房；病室
treat v. 医治；治疗
heatstroke n. 中暑
construction n. 建筑；建造
implementation n. 实施；执行
existing a. 现存的；现行的
uneven a. 不稳定的；有好有坏的
policy n. 政策；方针
adequate a. 足够的；能满足需要的
funding n. 基金；资金
trigger v. 启动；触发
threshold n. 临界点；阈
customize v. 改制；定制
temperature n. 温度；气温
serve v. 起作用；产生效果
humidity n. 湿度；湿气
gauge n. 依据；标准
high n. 最高气温；最高点
highlight v. 突出；强调
nuanced a. 精准入微的
localized a. 地区性的；小范围的
roughly ad. 大约；大致
shy a. 不足；未达到
coastal a. 沿海的；靠近海岸的
meteorological a. 气象的
authority n. 当局；官方
amplify v. 使变得明显；增强
neglected a. 被忽视的；未被重视的
shade n. 阴凉处；(树)荫
ceremony n. 典礼；仪式
urban a. 城市的；城镇的
outline v. 概述；概括
best practice 最佳做法；最佳实践
adapt v. 调整；使适合
condition n. 环境；条件
vulnerability n. 易受伤(性)；脆弱(性)
response n. 反应；响应
at risk 处于危险中的；可能遭受伤害的
complex a. 复杂的；难懂的
look at 思考；考虑
key a. 最重要的；关键的
parameter n. 起限定作用的因素；参数
neighborhood n. 街区；住宅区
informal a. 非正式的；非正规的
dwelling n. 住宅；住所
cope with 对付；处理
special a. 专用的；专门针对……的
bolster v. 支持；加强
project n. 项目；计划
in the event of 如果……发生；倘若
short-term a. 短期的；近期的
recommend v. 劝告做，建议(某事)
medium-term a. 中期的
long-term a. 长期的；长远的
retrofit v. 对(机器、建筑等)进行改型翻新；加装(部件)
modify v. 修改；改进
regulation n. 规章制度；法规
measure n. 办法；措施
tackle v. 决心处理(问题，难题)
monitor v. 监视；关注
address v. (着手)解决，处理(问题)
criteria n. 标准；准则
subtle a. 难以察觉的；细微的
prioritize v. 优先考虑；给……优先权
coverage n. 覆盖范围
heat-stricken a. 遭到高温打击的
grant n. 拨款；补助金
"""
add_items(2025, "传统阅读 Text 3", raw_2025_t3)

# Text 4
raw_2025_t4 = """
navigate v. 走过；经过
organised a. 规划整齐的；井然有序的
pavement n. 硬路面；人行道
urban a. 城市的；城镇的
desire path 欲望路径
footprint n. 脚印；足迹
community n. 社区；社会
reveal v. 表明；证明；揭示
shortcut n. 捷径；近路
collective a. 集体的；共同的
tread v. 踩出；踩踏
track n. (人踩出的)小道，小径
otherwise ad. 除此之外
route n. 路线；路途
disobedience n. 顺从；违抗
cut corners 抄近路；走捷径
bisect v. 对半分；二等分
natural capability 天生能力
interpret v. 理解；诠释
convenient a. 方便的；省事的
insight n. 洞悉；见解
dynamic n. 相互作用的方式
the Oval 椭圆草坪公园
proceed v. 接着做；继而做
pave v. 铺路；铺设
establish v. 建立；创立
reluctance n. 勉强；不情愿
persist v. 维持；持续存在
integrate v. 使结合；使合并
cite v. 提及(原因)；举出(示例)
aesthetics n. 美学
be devoted to 致力于……；专于……
boast v. 自夸；自吹自擂
showcase v. 展示；展现
adhere to 遵守；遵行
designate v. 指定；选定
underscore v. 强调；突出
inherent a. 固有的；内在的
clash n. 争论；分歧
highlight v. 突出；强调
ongoing a. 持续的；进行中的
organic a. 演进的；自然的
evolution n. 演变；发展
curate v. 策划(展览)
historical a. 历史上的；过去的
Native American 美洲原住民
settlement n. 定居点；聚居地
trail n. (踩出来的)小道，小径
Dutch a. 荷兰的；荷兰人的
colonist n. 殖民地定居者；殖民者
widen v. (使)变宽；拓宽
assumption n. (权力的)获得
notably ad. 尤其是；值得注意的是
stand out 更突出；更重要
defy v. 违抗；不遵守
grid-based a. 基于网格的
system n. 系统
apply v. 使用；应用
cut across 抄近路穿过；对直通过
diagonal n. 斜线；对角线
spark v. 引发；激发
fascination n. 入迷；迷恋
approach v. 接近(某数量或水平)
obsession n. 痴迷；着魔
serve as 可用作；可当……使
hub n. 中心；核心
contributor n. 撰稿人
alternate a. 另外的；非主流的
forge v. 艰苦干成；努力加强
carve v. 开创；创造
adaptability n. 适应性
criss-cross v. 构成十字形或交叉图案
physical a. 现实的；有形的
virtual a. 虚拟的；模拟的
stand as 作为……存在
insistence n. 坚持；固执
unconventional a. 非传统的
embrace v. 欣然接受(思想等)
the spirit of ……精神
communal a. 公共的；共同的
curiosity n. 好奇心；求知欲
solitude n. 独处；独居
intend to do sth 打算做某事
take a positive view of 对某事持积极看法
conflicting a. 冲突的；相矛盾的
upgrade v. 升级；改进
recognition n. 承认；认可
crucial a. 至关重要的；关键性的
imitation n. 模仿；效仿
trait n. 特点；特性
"""
add_items(2025, "传统阅读 Text 4", raw_2025_t4)


# ================= 2026 年 =================
# Text 1
raw_2026_t1 = """
image n. (心目中的)形象，印象
spring to mind 立即被想到
dusty a. 布满灰尘的；灰尘覆盖的
old-fashioned a. 陈旧的；过时的
sort n. 种类；类别
anyway ad. 况且；而且；再说
startlingly ad. 惊人地；显著地
the culture department 文化部
commission v. 授权或委托(人、组织)做或制造(某事物)
conduct v. 实施；执行
independent review 独立评估
up and down 到处；四面八方
learn v. 发现；得知；认识到
branch n. 分支；分部；分店
a hive of activity 忙碌的场所；繁忙的地方
multitude n. 众多；大量
offer v. 提供(东西或机会)；供应
employment n. 就业
digital a. 数字的；数字化的
access n. (使用或见到的)机会，权利
intellectual property 知识产权
entrepreneur n. 创业者；企业家
carry out 进行；完成
check n. 检查；查看
GP n. 全科医生
surgery n. 诊所
Fifa-standard a. 国际足联标准的
free ad. 免费地
in return for 作为对……的回报
precisely ad. 确切地；准确地
charge n. (商品和服务所需的)要价，收费
justify v. 证明……有道理
leave sb alone 不去打扰某人；让某人独自待着
institution n. (大学、银行等规模大的)机构
overlook v. 忽视；忽略
underappreciate v. 未充分认可
overall a. 全面的；整体的
struggle v. 挣扎；艰难运营
authority n. 官方机构；政府部门
come under 面临；承受
disputed a. 有争议的
chartered a. 合格的；特许的
institute n. 学会；协会；机构
accountancy n. 会计行业；会计工作
put sth at sth 估计……为(某一数量)
statistic n. 统计数据；统计资料
hold v. 持有；拥有
council n. (顾问、研究、基金等)委员会
record v. 标明；显示
raise v. 增加，提高(数量、水平等)
awareness n. 认识；认知
recommend v. 劝告；建议
branding n. 品牌创建；品牌打造
campaign n. 运动；活动
physical a. 物质的；有形的
presence n. 存在；出现
reintroduction n. 再次使用；重新引人
scheme n. 计划；方案
automatic a. 自动的
membership n. 会员资格；成员资格
end up 最终成为；最后处于
for some time 许久
document v. 记录，记载(详情)
expansion n. 扩张；扩展
obtain v. (尤指经努力)获得，赢得
look into 调查
boast v. 拥有(值得自豪的东西)
collection n. (一批)收藏品
diversify v. (使)多样化，不同
impose v. 推行；强制实行
upgrade v. 使(机器、计算机系统等)升级
advancement n. 促进；推动；发展
flaw n. 错误；缺点
invite v. 请求；要求
seek v. 寻求；争取
funding n. 基金；资金
"""
add_items(2026, "传统阅读 Text 1", raw_2026_t1)

# Text 2
raw_2026_t2 = """
guidance n. 指导；指引
personal a. 个人的；私人的
professional a. 职业上的；工作上的
engage with 与……建立密切关系
leave v. 使处于某种状态
hear v. 倾听；注意听
isolated a. 孤独的；孤立的
newfound a. 新获得的；新得到的
connection n. 情感纽带；亲密关系
share v. 将……告诉；向……倾诉
sensitive a. 敏感的；须慎重处理的
highly ad. 高度地；非常地
confidential a. 机密的；保密的
information n. 信息；资料
realise v. 认识到；意识到
platform n. 平台
be good at 擅长；善于
keep v. (使)保持，处于(某种状态)
secret n. 秘密；机密
implication n. 可能的影响(或作用、结果)
consider v. 不妨看看；参考一下
gain v. 使获得；使得到
input v. 输入(信息)
output v. 输出(信息)
see v. 认为；看待
fit a. 社会准则所允许的；恰当的
share v. 分享；共享
third party 第三方
mean v. 产生……结果；意思是
potentially ad. 潜在地；可能地
expose v. 使(隐藏或私密的事物)暴露，显露
take note 注意到；关注到
take action 采取行动
outright ad. 全部地；彻底地
ban v. 禁止；取缔
regulate v. 约束；管理
in place 到位；准备就绪
choose v. 选定；决定
break v. 违反；不执行
productivity n. 生产力；生产效率
offer v. 提供；给予
present v. 使发生或存在
delicate a. 微妙的；需要小心处理的
leverage v. 利用；充分运用
gain n. 改进；增益
exposure n. 泄露；暴露
manage v. 明智地使用；管理
the same as 和……相同的……
care n. 谨慎；小心
storage n. 存储；储存
knowledge gap 知识缺口；知识空白
address v. 处理；设法应对
individual n. 个人；个体
retain v. 保留；维持
ownership n. 所有权；产权
content n. (书、网站等的)内容
instill v. 逐渐灌输，逐步培养(思想或行为)
practice n. 通常的做法；惯例
engagement n. 使用特定系统或技术的行为
evolve v. 逐步发展，逐渐演变
positively ad. 积极地；有助益地
shift v. 改变；调整
landscape n. 全貌；图景
simplify v. 简化；使简单
admin n. 行政工作；管理事务
enhance v. 提升；增强
navigate v. 应对；处理；导航
cautiously ad. 谨慎地；小心地
compromise v. 损害；妥协
privacy n. 隐私；私密
back away from 从……后退；对……避而远之
as long as 只要……就……
be equipped with 装备有……；备有……
make sure 确保；设法保证
challenge n. 挑战；艰巨任务
lie v. 存在；在于
promote v. 推广；宣传；促销
advertising n. 广告；广告活动
market v. 推销；促销
budget n. 预算；经费
victim n. 受害者；上当的人
responsibility n. 责任感；责任心
spill the beans 泄露秘密；说漏嘴
facilitate v. 促进；促使
cite v. 举出(示例)；列举
pose v. 造成(威胁、问题等)
generate v. 产生；引起
encourage v. 鼓励；激励
access n. (使用或见到的)机会，权利
well-informed a. 消息灵通的；见多识广的
transparency n. 透明度；公开性
prioritise v. 优先处理；把……放在优先地位
perspective n. 看法；视角
adjust to 调整……以适应……
limited a. 有限的；受限制的
underestimate v. 低估；看轻
be exposed to 接触某事；暴露于某事
"""
add_items(2026, "传统阅读 Text 2", raw_2026_t2)

# Text 3
raw_2026_t3 = """
launch n. 投放市场；推出
preferred a. 更合意的；优先选取的
means n. 方式；方法
cover v. 走完(一段路程)
in terms of 在……方面；从……角度来看
leisure n. 休闲；闲暇
delay n. 延误；耽搁
numerous a. 众多的；许多的
maintenance n. 维护；保养
work n. (道路、桥梁等修建)工程
throw into 使处于，使陷入(某种状态)
chaos n. 混乱；无秩序状态
matter v. 事关紧要；有重大影响
account for (数量或比例上)占
disruption n. 扰乱；中断
frequent a. 频繁的；频发的
fixture n. 固定事物；长期存在的一部分
coverage n. 新闻报道
publicly ad. 国有(而非私营公司拥有)
operator n. 经营者；专业公司
improvement n. 改进处；改善的事物
obsolete a. 过时的；陈旧的
infrastructure n. 基础设施
explain v. 是……的原因
recovery n. 恢复；复苏
beneficiary n. 受益者；受益机构
capacity n. 生产(或运输)能力
in the meantime 在此期间；与此同时
inevitable a. 不可避免的；必然发生的
mixed a. 混合的；混杂的
spare a. 备用的；额外的
hiccup n. 小问题；暂时的耽搁
complex a. 错综复杂的；费解的
mean v. 产生……结果；意味着
regular a. 通常的；惯常的
route n. 常规路线；固定线路
pass through 通过；穿过
congestion n. (交通)拥堵；塞车
local a. (汽车或火车)每站都停的，慢的
break down (机器或车辆)停止运转，出故障
upgrade n. 升级；改进
segregation n. 隔离；分隔
construction n. 建筑；建造
underground a. 地下的
density n. 密度
satellite n. 人造卫星
signal v. 用信号传递信息或指示；发信号
reduction n. 减少；缩小
distance n. 距离；间距
given a. 指的；特定的
fluidity n. 流畅
outdated a. 过时的；陈旧的
popular a. 大众喜爱的；广受欢迎的
inadequately ad. 不充分地；不足地
utilise v. 使用；利用
occurrence n. 发生的事；事件
shortage n. 短缺；不足
massive a. 大量的；大规模的
scale n. 规模；范围
operational a. 运转的；运营的
spending n. 开支；支出
comfort n. 舒适；舒服
reconstruct v. 重建；修复
shorten v. (使)变短，缩短
interval n. 间隔；间距
"""
add_items(2026, "传统阅读 Text 3", raw_2026_t3)

# Text 4
raw_2026_t4 = """
beloved a. 钟爱的；深受喜爱的
festival n. 节；会演
block party 街头聚会；街区派对
stage v. 上演；举办
community n. 社区；社会
announce v. 宣布；宣告
neighborhood n. 街区；社区
blossom v. 发展；繁荣
massive a. 巨大的；强大的
event n. 公开活动；社交场合
abruptly ad. 突然地；意外地
shut down 停业；停止运行
point to 提出；指出
production n. 上演；制作
attendee n. 出席者；在场者
donation n. 捐赠物；捐款
highlight v. 突出；强调
produce v. 上演；制作
skyrocket v. 飞涨；飙升
security n. 保护措施；安全工作
entertainment n. 娱乐活动；文娱表演
portable a. 临时搭建的；可移动的
insurance n. 保险；保险服务
fencing n. 围栏；围栏搭建
staffing n. 人力；人员配备
dramatically ad. 巨大而热烈地；急剧地
more than just 不仅仅
engine n. 原动力；手段
drive v. 推动；带动
foot traffic 人流量；客流量
foster v. 促进；培养
vibrancy n. 活力；活跃
solicit v. 恳求；募集
request v. 请求；要求
funding n. 专款；资金
sponsorship n. 资助；赞助款
vendor n. 摊贩；小贩
cover v. 足以支付；够付
anticipated a. 受期待的；令人期待的
draw v. 吸引；使感兴趣
upward of 超过；多于
live a. 现场演出的；现场的
indie a. 非主要唱片公司的；独立制作的
connection n. (情感)联结；融洽
record-breaking a. 破纪录的；创纪录的
attendance n. 出席人数；参与人数
turnout n. 出席人数；到场人数
scale back 减少；缩减
footprint n. 规模大小；影响范围
eliminate v. 消除；除去
book v. 预约；预雇
strive to do sth 努力做某事
true a. 忠实的；恪守的
spirit n. 本质；基本精神
reputation n. 名声；口碑
festgoer n. 节庆活动参与者
thriving a. 兴盛的；繁荣的
chip in 凑份子；共同出钱
be replaced by 被……取代
fame n. 名声；声誉
appealing a. 有吸引力的；令人感兴趣的
sufficient a. 足够的；充足的
facility n. 设施；设备
tackle v. 应对；解决
step up 增加；提高
relieve v. 调剂；使不单调
contribute to 对……做出贡献
count on 依赖；指望
amateur a. 业余的；非专业的
prominent a. 显著的；突出的
feature n. 特色；特点
collaborate with 与……合作
generosity n. 慷慨；大方
expenditure n. 花费；开支
"""
add_items(2026, "传统阅读 Text 4", raw_2026_t4)

with open(r'f:\obsidiannote\obsidian-\408\数据结构\考研英语二核心词背诵\data_generators\data_2022_2026.json', 'w', encoding='utf-8') as f:
    json.dump(DATA_2022_2026, f, ensure_ascii=False, indent=2)

print('Generated 2022-2026 items count:', len(DATA_2022_2026))
