# CartPole
Cart Pole  With RL Algorithm

## Introduction

This document describes in detail a reinforcement learning application using the Proximal Policy Optimization (PPO) algorithm. The goal of the project is to solve a Cart Pole task with the PPO algorithm. This document contains details such as the project objectives, the reasons for choosing the algorithm used, and how certain parameters were set. 

  

Objectives of the Project: 

The Cart Pole task is the problem of controlling a car placed on a pole that needs to be kept in balance. 

  

Algorithm Selection: 

In this project, the PPO (Proximal Policy Optimization) algorithm was preferred for the reinforcement learning task. PPO is an algorithm that has been successfully used in the reinforcement learning field and gives reliable results and the PPO algorithm was created as seen in the PPO.py file 

  

Parameter Selection: 

Several parameters have been selected that have an impact on the success and performance of the algorithm. For example, the number of timesteps was selected as 2000 and it was decided to make 100 timesteps in each learning step, and in this case, the changes in the graph were examined in each 100 timesteps and the maximum score value of 500 was reached in the average 7th stage. 


Structure of the Project: 

 

Code Structure: 

The project was written in Python and used the Stable Baselines3 library, a framework used for reinforcement learning, and the PPO algorithm was created as seen in the PPO.py file. 

  

Algorithm: 

The algorithm used is PPO. The PPO allows the agent to interact with its environment by making policy updates and supports its learning in a stable way, and this algorithm was created in the PPO.py file and used in the cartPole.py file. 

  

Parameters and Settings: 

The project was started with certain parameters. These parameters include learning speed, number of timesteps, policy update steps, reward processing method, and value function coefficients. 

Values Included in the Project: 


num_episodes: 

num_episodes value was chosen as 100 In general, the value of 100 was accepted in RL algorithms, and when the value of 100 was chosen, the model performed 100 sections at each stage and selected a series of actions in each section and calculated the total reward obtained during the section, so when the reward value was 500.00, the code completed its training and managed to keep the bar on the tool stable. 

  

mean_episode_reward(Reward value given before the model is trained): 

When this value is selected num_episode as an average of 100 because of 50 runs, the value obtained is an average of 22 in each cycle. has given. 


mean_reward:  

It represents the reward given, and when it is 500.00, it indicates that the project is working correctly. 

  

std_reward: 

It shows the standard deviation, which is about 90.00 in the initial stages, but as time passes, the standard deviation value reaches 0.00 in the average 7th step. The standard deviation value is measured to measure how much the values in the dataset deviate from the mean. 

  

Further Improvements and Areas of Study: 

  

Longer Training: 

By increasing the training time, the agent can be enabled to learn more complex strategies. For example, the total_timesteps value can be made 10000, but the project achieves the desired result total_timesteps 2000 and the car can keep the bar standing steadily. If we increase the num_episodes value, it is not preferred because it will increase the cost, the value of 100 works most accurately. 


Graphics: 

 

Example of graph the reward values that came out before the training: 
<img width="619" alt="Screenshot 2024-01-21 023138" src="https://github.com/Arda1999/CartPoleAI/assets/62334668/7373f894-221e-4d8a-97bd-1b2d6ed4084a">
 


Example of graph the reward values after the training:


<img width="619" alt="Screenshot 2024-01-21 023111" src="https://github.com/Arda1999/CartPoleAI/assets/62334668/cef47bb4-fd3e-479b-94a7-782e935683f3">


 

 

As can be seen in the graphs, although there was very variable score values before the training, the values became constant after a certain point after the training. 

Example Output:

Before the train reward values:  

Timestep 0: Mean reward: 22.65 Num episodes: 100 

Timestep 1: Mean reward: 21.43 Num episodes: 100 

Timestep 2: Mean reward: 21.29 Num episodes: 100 

Timestep 3: Mean reward: 24.56 Num episodes: 100 

Timestep 4: Mean reward: 21.19 Num episodes: 100 

Timestep 5: Mean reward: 22.8 Num episodes: 100 

Timestep 6: Mean reward: 22.94 Num episodes: 100 

Timestep 7: Mean reward: 24.89 Num episodes: 100 

Timestep 8: Mean reward: 20.69 Num episodes: 100 

Timestep 9: Mean reward: 23.57 Num episodes: 100 

Timestep 10: Mean reward: 21.8 Num episodes: 100 

Timestep 11: Mean reward: 24.29 Num episodes: 100 

Timestep 12: Mean reward: 21.44 Num episodes: 100 

Timestep 13: Mean reward: 22.93 Num episodes: 100 

Timestep 14: Mean reward: 22.15 Num episodes: 100 

Timestep 15: Mean reward: 23.44 Num episodes: 100 

Timestep 16: Mean reward: 22.69 Num episodes: 100 

Timestep 17: Mean reward: 21.38 Num episodes: 100 

Timestep 18: Mean reward: 23.08 Num episodes: 100 

Timestep 19: Mean reward: 20.95 Num episodes: 100 

Timestep 20: Mean reward: 23.53 Num episodes: 100 

Timestep 21: Mean reward: 20.88 Num episodes: 100 

Timestep 22: Mean reward: 20.98 Num episodes: 100 

Timestep 23: Mean reward: 21.92 Num episodes: 100 

Timestep 24: Mean reward: 21.71 Num episodes: 100 

Timestep 25: Mean reward: 22.06 Num episodes: 100 

Timestep 26: Mean reward: 20.44 Num episodes: 100 

Timestep 27: Mean reward: 23.75 Num episodes: 100 

Timestep 28: Mean reward: 22.75 Num episodes: 100 

Timestep 29: Mean reward: 21.77 Num episodes: 100 

Timestep 30: Mean reward: 22.17 Num episodes: 100 

Timestep 31: Mean reward: 23.86 Num episodes: 100 

Timestep 32: Mean reward: 22.97 Num episodes: 100 

Timestep 33: Mean reward: 22.1 Num episodes: 100 

Timestep 34: Mean reward: 21.89 Num episodes: 100 

Timestep 35: Mean reward: 19.97 Num episodes: 100 

Timestep 36: Mean reward: 21.56 Num episodes: 100 

Timestep 37: Mean reward: 22.68 Num episodes: 100 

Timestep 38: Mean reward: 23.33 Num episodes: 100 

Timestep 39: Mean reward: 21.91 Num episodes: 100 

Timestep 40: Mean reward: 21.12 Num episodes: 100 

Timestep 41: Mean reward: 23.52 Num episodes: 100 

Timestep 42: Mean reward: 24.67 Num episodes: 100 

Timestep 43: Mean reward: 22.24 Num episodes: 100 

Timestep 44: Mean reward: 21.93 Num episodes: 100 

Timestep 45: Mean reward: 21.15 Num episodes: 100 

Timestep 46: Mean reward: 21.33 Num episodes: 100 

Timestep 47: Mean reward: 22.06 Num episodes: 100 

Timestep 48: Mean reward: 21.05 Num episodes: 100 

Timestep 49: Mean reward: 21.83 Num episodes: 100 

Timestep 50: Mean reward: 22.62 Num episodes: 100 

Timestep 51: Mean reward: 23.09 Num episodes: 100 

Timestep 52: Mean reward: 20.04 Num episodes: 100 

Timestep 53: Mean reward: 22.1 Num episodes: 100 

Timestep 54: Mean reward: 21.21 Num episodes: 100 

Timestep 55: Mean reward: 21.85 Num episodes: 100 

Timestep 56: Mean reward: 20.14 Num episodes: 100 

Timestep 57: Mean reward: 23.86 Num episodes: 100 

Timestep 58: Mean reward: 21.25 Num episodes: 100 

Timestep 59: Mean reward: 22.46 Num episodes: 100 

Timestep 60: Mean reward: 20.57 Num episodes: 100 

Timestep 61: Mean reward: 24.14 Num episodes: 100 

Timestep 62: Mean reward: 19.85 Num episodes: 100 

Timestep 63: Mean reward: 22.64 Num episodes: 100 

Timestep 64: Mean reward: 22.81 Num episodes: 100 

Timestep 65: Mean reward: 21.22 Num episodes: 100 

Timestep 66: Mean reward: 22.43 Num episodes: 100 

Timestep 67: Mean reward: 22.45 Num episodes: 100 

Timestep 68: Mean reward: 22.6 Num episodes: 100 

Timestep 69: Mean reward: 21.88 Num episodes: 100 

Timestep 70: Mean reward: 22.84 Num episodes: 100 

Timestep 71: Mean reward: 22.2 Num episodes: 100 

Timestep 72: Mean reward: 21.3 Num episodes: 100 

Timestep 73: Mean reward: 19.93 Num episodes: 100 

Timestep 74: Mean reward: 21.55 Num episodes: 100 

Timestep 75: Mean reward: 24.69 Num episodes: 100 

Timestep 76: Mean reward: 22.85 Num episodes: 100 

Timestep 77: Mean reward: 23.44 Num episodes: 100 

Timestep 78: Mean reward: 23.61 Num episodes: 100 

Timestep 79: Mean reward: 21.8 Num episodes: 100 

Timestep 80: Mean reward: 22.63 Num episodes: 100 

Timestep 81: Mean reward: 22.38 Num episodes: 100 

Timestep 82: Mean reward: 22.29 Num episodes: 100 

Timestep 83: Mean reward: 23.08 Num episodes: 100 

Timestep 84: Mean reward: 21.89 Num episodes: 100 

Timestep 85: Mean reward: 20.95 Num episodes: 100 

Timestep 86: Mean reward: 21.79 Num episodes: 100 

Timestep 87: Mean reward: 21.19 Num episodes: 100 

Timestep 88: Mean reward: 22.88 Num episodes: 100 

Timestep 89: Mean reward: 22.51 Num episodes: 100 

Timestep 90: Mean reward: 24.53 Num episodes: 100 

Timestep 91: Mean reward: 24.1 Num episodes: 100 

Timestep 92: Mean reward: 26.02 Num episodes: 100 

Timestep 93: Mean reward: 22.39 Num episodes: 100 

Timestep 94: Mean reward: 23.0 Num episodes: 100 

Timestep 95: Mean reward: 20.65 Num episodes: 100 

Timestep 96: Mean reward: 22.73 Num episodes: 100 

Timestep 97: Mean reward: 21.71 Num episodes: 100 

Timestep 98: Mean reward: 21.93 Num episodes: 100 

Timestep 99: Mean reward: 21.67 Num episodes: 100\ 

 

 

 

After the train reward values: 

Timestep 1: Mean reward: 127.99 +/- 59.54 

Timestep 101: Mean reward: 372.73 +/- 136.60 

Timestep 201: Mean reward: 395.46 +/- 119.91 

Timestep 301: Mean reward: 371.64 +/- 124.87 

Timestep 401: Mean reward: 431.07 +/- 86.70 

Timestep 501: Mean reward: 406.11 +/- 99.17 

Timestep 601: Mean reward: 446.21 +/- 70.52 

Timestep 701: Mean reward: 460.24 +/- 59.97 

Timestep 801: Mean reward: 498.01 +/- 8.34 

Timestep 901: Mean reward: 500.00 +/- 0.00 

Timestep 1001: Mean reward: 500.00 +/- 0.00 

Timestep 1101: Mean reward: 500.00 +/- 0.00 

Timestep 1201: Mean reward: 500.00 +/- 0.00 

Timestep 1301: Mean reward: 500.00 +/- 0.00 

Timestep 1401: Mean reward: 500.00 +/- 0.00 

Timestep 1501: Mean reward: 500.00 +/- 0.00 

Timestep 1601: Mean reward: 500.00 +/- 0.00 

Timestep 1701: Mean reward: 500.00 +/- 0.00 

Timestep 1801: Mean reward: 500.00 +/- 0.00 

Timestep 1901: Mean reward: 500.00 +/- 0.00 

 

 

Project Information: 

Libraries Used: OpenAI Gym, Matplotlib, NumPy, Stable Baselines3 

Language Used: Python 

Project Resources: Stable Baselines3 GitHub 
