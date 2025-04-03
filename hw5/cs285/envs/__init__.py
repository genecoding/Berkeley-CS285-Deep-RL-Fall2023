import gym

from .pointmass import Pointmass

gym.register(
    id="PointmassEasy-v0",
    entry_point=Pointmass,
    kwargs={"difficulty": 0},
)

gym.register(
    id="PointmassMedium-v0",
    entry_point=Pointmass,
    kwargs={"difficulty": 1},
)

gym.register(
    id="PointmassHard-v0",
    entry_point=Pointmass,
    kwargs={"difficulty": 2},
)

gym.register(
    id="PointmassVeryHard-Spiral11x11-v0",
    entry_point=Pointmass,
    kwargs={"difficulty": 3,
            "maze": "Spiral11x11"},
)

gym.register(
    id="PointmassVeryHard-Maze11x11-v0",
    entry_point=Pointmass,
    kwargs={"difficulty": 3,
            "maze": "Maze11x11"},
)

gym.register(
    id="PointmassVeryHard-Tunnel-v0",
    entry_point=Pointmass,
    kwargs={"difficulty": 3,
            "maze": "Tunnel"},
)

gym.register(
    id="PointmassVeryHard-Tree-v0",
    entry_point=Pointmass,
    kwargs={"difficulty": 3,
            "maze": "Tree"},
)

gym.register(
    id="PointmassVeryHard-UMulti-v0",
    entry_point=Pointmass,
    kwargs={"difficulty": 3,
            "maze": "UMulti"},
)

gym.register(
    id="PointmassVeryHard-FlyTrapSmall-v0",
    entry_point=Pointmass,
    kwargs={"difficulty": 3,
            "maze": "FlyTrapSmall"},
)

gym.register(
    id="PointmassVeryHard-FlyTrapBig-v0",
    entry_point=Pointmass,
    kwargs={"difficulty": 3,
            "maze": "FlyTrapBig"},
)

gym.register(
    id="PointmassVeryHard-Galton-v0",
    entry_point=Pointmass,
    kwargs={"difficulty": 3,
            "maze": "Galton"},
)
