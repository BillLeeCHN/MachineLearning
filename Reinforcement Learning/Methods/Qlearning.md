# A Painless Q-learning Tutorial

>   本文是对 http://mnemstudio.org/path-finding-q-learning-tutorial.htm 的翻译，共分两部分，第一部分为中文翻译，第二部分为英文原文。翻译时为方便读者理解，有些地方采用了意译的方式，此外，原文中有几处笔误，在翻译时已进行了更正。这篇教程通俗易懂，是一份很不错的学习理解 Q-learning 算法工作原理的材料。
>
>   中文版来源：http://blog.csdn.net/pi9nc/article/details/27649323

## **Section 1：中文翻译**

![picture_1](https://github.com/BillLeeCHN/MachineLearning/blob/QLearning/Reinforcement%20Learning/Methods/pics/1.png?raw=true)

![picture_2](https://github.com/BillLeeCHN/MachineLearning/blob/QLearning/Reinforcement%20Learning/Methods/pics/2.png?raw=true)

![picture_3](https://github.com/BillLeeCHN/MachineLearning/blob/QLearning/Reinforcement%20Learning/Methods/pics/3.png?raw=true)

![](https://github.com/BillLeeCHN/MachineLearning/blob/QLearning/Reinforcement%20Learning/Methods/pics/4.png?raw=true)

![](https://github.com/BillLeeCHN/MachineLearning/blob/QLearning/Reinforcement%20Learning/Methods/pics/5.png?raw=true)

![](https://github.com/BillLeeCHN/MachineLearning/blob/QLearning/Reinforcement%20Learning/Methods/pics/6.png?raw=true)

![](https://github.com/BillLeeCHN/MachineLearning/blob/QLearning/Reinforcement%20Learning/Methods/pics/7.png?raw=true)

![](https://github.com/BillLeeCHN/MachineLearning/blob/QLearning/Reinforcement%20Learning/Methods/pics/8.png?raw=true)

# Section 2

## 2.1 转移规则

公式(1.1)是更新状态的一种方程。

另外一个公式如下：

![](https://github.com/BillLeeCHN/MachineLearning/blob/QLearning/Reinforcement%20Learning/Methods/pics/update%20state.png?raw=true)

其中：$\alpha$为学习效率(learning rate):学习速率α越大，保留之前训练的效果就越少.

$\gamma$为折扣因子(discount factor):

## 2.2 选择行为action

选择行为action有不同的方式，分为 exploration only 和 exploitation only 以及两者兼顾，此时就会引入ε-greedy参数(0 = ε-greedy < 1)。

1.  exploration only：仅探索，即每一次选择action时，总是在可以做的动作中，随机选择一个动作。优点：具有探索精神，能够找到最优的路径。缺点：运行时间长


2.  exploitation only：仅利用，即每一次选择action时，总是选择Q表值最大的行为。优点：安稳，快速。缺点：缺乏探索精神，所选的路径不一定是最好的。

3.  exploration  and exploitation ：两者兼顾，引入ε-greedy。即每一次选择action时，有概率ε-greedy的可能性选择exploration ，有概率(1-ε-greedy)的可能性选择exploitation 。优点：上述两点的优点的集合








