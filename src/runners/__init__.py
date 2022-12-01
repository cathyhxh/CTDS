REGISTRY = {}

from .episode_runner_teach import EpisodeRunner_Teach
REGISTRY["episode_teach"] = EpisodeRunner_Teach

from .episode_runner import EpisodeRunner
REGISTRY["episode"] = EpisodeRunner