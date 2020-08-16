# gym-skewb

An OpenAI environment for the Skewb

## Installation

Install the [OpenAI gym](https://gym.openai.com/docs/).

Then install this package via

```
pip install -e .
```

## Usage

```
import gym
import gym_skewb

env = gym.make('Skewb-v0')
env.reset()
for _ in range(3):
    env.render()
    observation, reward, done, info = env.step(env.action_space.sample()) 
```