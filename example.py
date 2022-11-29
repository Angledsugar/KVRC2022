import gymnasium
import gym
import gym_examples

env = gym.make('gym_examples/GridWorld-v0', render_mode = "human")
env.action_space.seed(42)

observation, info = env.reset(seed=42)

for i in range(1000):
    print("Episode : ", i)
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

env.close()