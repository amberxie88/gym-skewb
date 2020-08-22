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
## Skewb

The Skewb representation is implemented in
```
skewb.py
```

Basic tests for correct implementation of the Skewb are in 
```
test.py
```

### Skewb Representation
The Skewb is represented as six arrays of colors. Each side has five pieces, and the following image describes the index in each array for each piece.

![skewb_layout](Skewb.png)

The four unique turns (R, L, U, F) are implemented; all others are derivations of these four. 
