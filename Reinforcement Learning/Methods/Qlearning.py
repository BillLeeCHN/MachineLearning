# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 14:05:40 2017

@author: Bill Lee
注：Q Learning 的程序
"""

import numpy as np

np.random.seed(2) # 每次产生的随机数不相同

GAMMA = 0.8
Q_table = np.zeros([6,6])
EPISODES = 3000
EPSILON = 0.1 # greedy policy

# reward array R
R_table = np.array([[-1,-1,-1,-1,0,-1],
                  [-1,-1,-1,0,-1,100],
                  [-1,-1,-1,0,-1,-1],
                  [-1,0,0,-1,0,-1],
                  [0,-1,-1,0,-1,100],
                  [-1,0,-1,-1,0,100]])

# exploitation only, 仅利用，每一步的action按照Q表值大的选择
def choose_action_exploitation(s, R_table, Q_table):
    rewards = R_table[s,:]
    positions = [] # 在状态s的情况下，可以走的路径为：positions
    for i in range(6):
        if rewards[i] >= 0:
            positions.append(i)
    # 在Q表中处理
    values = []
    for i in range(np.size(positions)):
        values.append(Q_table[s, positions[i]])

    index_max = max_index(values)
    index = positions[index_max]

    return index
      
# exploration only, 仅探索：每一步的action随机选择
def choose_action_exploration(s, R_table, Q_table):
    rewards = R_table[s,:]
    positions = [] # 在状态s的情况下，可以走的路径为：positions
    for i in range(6):
        if rewards[i] >= 0:
            positions.append(i)
    # exploration only
    index = np.random.choice(positions)
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

def choose_action(s, R_table, Q_table):
    # exploration, 随机选择
    if (np.random.uniform() < EPSILON):
        return choose_action_exploration(s, R_table, Q_table)
    else: # exploitation
        return choose_action_exploitation(s, R_table, Q_table)
        
        
        
def QLearning():
    for i in range(EPISODES):
        s = np.random.choice([0,1,2,3,4,5]) # 随机选择一个初始位置
        is_terminated = False
        while not is_terminated:
            # exploration only
            a = choose_action_exploration(s,R_table, Q_table)
            # exploitation only
#            a = choose_action_exploitation(s,R_table, Q_table)
            # exploration and exploitation
#            a = choose_action(s, R_table, Q_table)
            # update Q table  
            Q_table[s,a] = R_table[s,a] + GAMMA * Q_table[a,:].max()
            
            if a == 5:
                is_terminated = True
                
            #update state
            s = a
    return Q_table


# run function
res = QLearning()
print(res)

# result of exploration only
#[[   0.    0.    0.    0.  400.    0.]
# [   0.    0.    0.  320.    0.  500.]
# [   0.    0.    0.  320.    0.    0.]
# [   0.  400.  256.    0.  400.    0.]
# [ 320.    0.    0.  320.    0.  500.]
# [   0.  400.    0.    0.  400.  500.]]

# result of exploitation only
#[[   0.    0.    0.    0.  400.    0.]
# [   0.    0.    0.    0.    0.  500.]
# [   0.    0.    0.  320.    0.    0.]
# [   0.    0.    0.    0.  400.    0.]
# [   0.    0.    0.    0.    0.  500.]
# [   0.    0.    0.    0.    0.  500.]]

