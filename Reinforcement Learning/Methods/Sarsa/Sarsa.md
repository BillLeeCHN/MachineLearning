# Sarsa


## 1、sarsa 算法示意图
![](https://github.com/BillLeeCHN/MachineLearning/blob/Sarsa/Reinforcement%20Learning/Methods/Sarsa/pics/sarsa.png?raw=true)

## 2、与 Q-Learning 的比较
Q-Learing算法示意图


![](https://github.com/BillLeeCHN/MachineLearning/blob/master/Reinforcement%20Learning/Methods/QLearning/pics/QLearning.png?raw=true)

Sarsa的算法示意图与Q-Learning算法示意图比较，我们发现，两者的算法几乎相同。唯一不同的是，sarsa的Q表更新方式与QLearning不同，而采取action的方式是一致。

-   Q-Learning:（本次state采取的action对应的reward) + γ*(下一个state对应的Q表中Q值最大的值)


-   Sarsa:在确定本次state的action之后，再确定下一个state的action,然后再更新Q表的值。


（本次state采取的action对应的reward）+（下一个state采取action对应的reward值）


# Sarsa Lambda

## 1、Sarsa Lambda 算法示意图

![](https://github.com/BillLeeCHN/MachineLearning/blob/Sarsa/Reinforcement%20Learning/Methods/Sarsa/pics/Sarsa_lambda.png?raw=true)

Sarsa Lambda 算法是Sarsa算法的改进版本。

特点是：

-   有一个与Q table相同行列数的表格叫做Eligibility table，row是state,column是action。
-   Eligibility table存放着每一个(s,a)的衰变值，在每一个step中，执行的(s,a)值自加1，即E(s,a) = E(s,a) + 1。其他的位置没有执行，值不改变。
-   使用此Eligibility table 对Q表执行相应计算
-   最后对Eligibility table所有的值进行一次衰变
-   λ=0时，E(s,a) 的值每次更新完Q表之后就会归零，此时与Sarsa算法一致
-   λ=1时，λ对E(s,a) 的值不产生影响，只由γ对E(s,a) 的值产生影响。

