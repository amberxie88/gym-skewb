from gym.envs.registration import register

register(
    id='Skewb-v0',
    entry_point='gym_skewb.envs:SkewbEnv',
)