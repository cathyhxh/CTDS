from .q_learner import QLearner

from .q_learner_teach import QLearner_Teach

REGISTRY = {}

REGISTRY["q_learner"] = QLearner
REGISTRY["q_learner_teach"] = QLearner_Teach
