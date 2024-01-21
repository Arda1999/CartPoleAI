
import gym
from matplotlib import pyplot as plt
import numpy as np
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.ppo.policies import MlpPolicy
import importlib
ppo_module = importlib.import_module("PPO")
PPO = ppo_module.MyPPO

env = gym.make('CartPole-v1', render_mode="human")


model = PPO(MlpPolicy, env, verbose=0)

def evaluate(model, num_episodes=100):
    env = model.get_env()
    all_episode_rewards = []
    for i in range(num_episodes):
        episode_rewards = []
        done = False
        obs = env.reset()
        while not done:
            action, _states = model.predict(obs)
            
            obs, reward, done, info = env.step(action)
            episode_rewards.append(reward)

        all_episode_rewards.append(sum(episode_rewards))

    mean_episode_reward = np.mean(all_episode_rewards)
    
    print(f"Timestep {timestep_before}: Mean reward:", mean_episode_reward, "Num episodes:", num_episodes)

    return mean_episode_reward
mean_rewards_before = []  
timesteps_list_before = []  

for timestep_before in range(100):
    mean_reward_before_train = evaluate(model, num_episodes=100)
    
    mean_rewards_before.append(mean_reward_before_train)
    timesteps_list_before.append(timestep_before)

model.learn(total_timesteps=2000)

  
mean_rewards = [] 
timesteps_list = []  
for timestep in range(1, 2001, 100):
    model.learn(total_timesteps=100)
    mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=100)

    print(f"Timestep {timestep}: Mean reward: {mean_reward:.2f} +/- {std_reward:.2f}")

    mean_rewards.append(mean_reward)
    timesteps_list.append(timestep)

plt.plot(timesteps_list, mean_rewards)
plt.xlabel("Timesteps")
plt.ylabel("Mean Reward")
plt.title("Mean Rewards over Timesteps")
plt.grid(True)
plt.show()

plt.plot(timesteps_list_before, mean_rewards_before)
plt.xlabel("Time")
plt.ylabel("Mean Reward")
plt.title("Mean Rewards over Time Before The Train")
plt.grid(True)
plt.show()

env.render()