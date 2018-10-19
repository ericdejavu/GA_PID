# GA_PID
利用遗传算法调节pid参数 pid tune by using GA
遗传算法要素

1. **dna**:			作用于输入可拆分的最小可调节参数
2. **遗传与变异**:           dna片段交换的策略，以及调节参数随机突变的规则
3. **性状**:                       程序表现出来的输出参数
4. **与环境的作用**:       对应性状在评分机制下的得分

## 评分机制

#### 定义

- **峰值**(pick)

  第一次超出设定值后的所到达的极值

- **稳定性**(stable)

  在设定值不变的情况下，第二次到达设定值之后所有数据的均方差

- **反应时间**(react time)

  第一次到达设定值所用的时间

- **响应时间**(response time)

  第二次到达设定值所使用的时间

- **动态稳定性**(dynamic stable)

  在设定固定数量的节点值后，每次到达当前设定值后到第二个设定值时,计算当前的所有数据微分后的均方差，以及微分零点附近加减dv的所用时间

#### 评分参数

- **静态评分** (static_score)

  stable = sum( ( f(x) - avg( f(x) ) )**2 ) / n

  static_score = 1 / (1 + pick*stable) * 1.0

- **执行能力评分** (executable_score)

  executable_score = react_time + response_time

- **动态稳定性评分** (dynamic_stable_score)

  df(x) = f(current_x) - f(prev_x)

  stable = sum( ( df(x) - avg( df(x) ) )**2  ) / n

  zero_time = sum( between(df(x), -dv, dv) ? time1 - time2:0)

  dynamic_stable_score = 1 / (1 + zero_time*stable) * 1.0


#### QA

Q:怎样的参数结果是一个满意的调节参数

A:可以适应不同速度的同时保证执行器的运动平滑，抖动在可接受范围内

Q:如何做到筛选，最终取的参数情况

A:根据pick和stable计算出static_score筛选出在静态状态下表现优异的DNA，构建一个static_population_pool,按照react time和response time计算出的executable_score做为模糊要求的速度控制(例如，发出类似快速，慢速等这类要求)，最后利用dynamic_stable来过滤一些满足要求的executable_score,生成dynamic_population_pool,这个pool就是最终要的结果，输入通过模糊的速度控制参数和一系列节点构成





## 表结构中的定义说明

- pid_origin

  - project_group 用于标注数据是属于哪个工程的

  - pid_group 用于标注测试的序列

- measure_motor_pid

  - group_sequence 用于和pid_origin.pid_group建立关联的
  - sub_group_sequence 用于标注多次测试的序列
  - continue_group_sequence 用于标注动态性测试组的节点序列

- analyze_pid

  - group_sequence 用于和pid_origin.pid_group建立关联
  - sub_group_sequence 用于和measure_motor_pid.continue_group_sequence建立关联