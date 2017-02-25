# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 14:05:40 2017

@author: Bill Lee
注：Q Learning 的程序
此段代码有错误，但是不知道哪里不对，先放在这里，以后再纠正
"""

import numpy as np

GAMMA = 0.8
Q_table = np.zeros((6,6))
EPISODES = 1000

#Q_table = np.array([[   0. ,    0. ,    0. ,    0. ,  144.  ,   0. ],
#                 [   0.  ,   0.   ,  0.  ,   0.   ,  0. ,  180. ],
#                 [   0.  ,   0.  ,   0.  ,  64.  ,   0. ,    0. ],
#                 [   0.  ,  80.  ,  51.2 ,   0.  , 144. ,    0. ],
#                 [   0.  ,   0.   ,  0.  ,   0.  ,   0.  , 180. ],
#                 [   0.   ,  0.   ,  0.  ,   0.  ,   0.  , 100. ]])



# reward matrix R
R_table = np.array([[-1,-1,-1,-1,0,-1],
                  [-1,-1,-1,0,-1,100],
                  [-1,-1,-1,0,-1,-1],
                  [-1,0,0,-1,0,-1],
                  [0,-1,-1,0,-1,100],
                  [-1,0,-1,-1,0,100]])

def choose_action(s, R_table, Q_table):
    rewards = R_table[s,:]
    positions = [] # 在状态s的情况下，可以走的路径为：positions
    for i in range(6):
        if rewards[i] > -1:
            positions.append(i)
    # 在Q表中处理
    values = []
    for i in range(np.size(positions)):
        values.append(Q_table[s, positions[i]])
    index_max = max_index(values)
    index = positions[index_max]
    return index
      
     
def max_index(values): # 返回数组最大数的所有索引
    count = np.size(values)
    ind_max = np.argmax(values)
    index = [ind_max]
    
    for i in range(ind_max+1, count):
        if values[i] == values[ind_max]:
            index.append(i)
            
    if np.size(index) == 1:
        return ind_max
    else:
        return np.random.choice(index)
    np.indices
    

def QLearning():
    for i in range(EPISODES):
        s = np.random.choice([0,1,2,3,4,5]) # 随机选择一个初始位置
        is_terminated = False
        while not is_terminated:
            a = choose_action(s, Q_table,R_table)
            
            if a == 5:
                is_terminated = True
            # update Q table  
            Q_table[s,a] = R_table[s,a] + GAMMA * Q_table[a,:].max()
            #update state
            s = a
    return Q_table



res = QLearning()
print(res)
#re = choose_action(5, R_table, Q_table)
#print(re)

#运行结果
#[[   0.    0.    0.    0.  400.    0.]
# [   0.    0.    0.    0.    0.  500.]
# [   0.    0.    0.  320.    0.    0.]
# [   0.  400.  256.    0.  400.    0.]
# [   0.    0.    0.    0.    0.  500.]
# [   0.    0.    0.    0.    0.  500.]]












