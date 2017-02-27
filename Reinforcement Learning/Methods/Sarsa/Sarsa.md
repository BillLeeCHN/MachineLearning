# 一、What is Sarsa?


## 二、sarsa 算法示意图
![](https://github.com/BillLeeCHN/MachineLearning/blob/Sarsa/Reinforcement%20Learning/Methods/Sarsa/pics/sarsa.png?raw=true)

## 三、与 Q-Learning 的比较
Q-Learing算法示意图
![](https://github.com/BillLeeCHN/MachineLearning/blob/master/Reinforcement%20Learning/Methods/QLearning/pics/QLearning.png?raw=true)

sarsa的算法示意图与QLearning算法示意图比较，我们发现，两者的算法几乎相同。唯一不同的是，sarsa的Q表更新方式与QLearning不同，而采取action的方式是一致。

Q-Learning:（本次state采取的action对应的reward) + γ*(下一个state对应的Q表中Q值最大的值)

Sarsa:在确定本次state的action之后，再确定下一个state的action,然后再更新Q表的值。

（本次state采取的action对应的reward）+（下一个state采取的action对应的reward值）


