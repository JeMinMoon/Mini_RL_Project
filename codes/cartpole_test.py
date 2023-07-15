import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

vec_env = make_vec_env("CartPole-v1", n_envs=4, seed=0)

model = PPO("MlpPolicy", vec_env, verbose=1)
model.learn(total_timesteps=25000)
#model.save("ppo_cartpole")

del model

model = PPO.load("ppo_cartpole")

obs = vec_env.reset()
while True:
    action, _states = model.predict(obs)
    obs,reward, dones, info = vec_env.step(action)
    vec_env.render(mode="human")
