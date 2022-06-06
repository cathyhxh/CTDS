from .q_learner import QLearner
from .dmaq_qatten_learner import DMAQ_qattenLearner
from .q_learner_teach import QLearner_Teach
from .dmaq_qatten_learner_teach import DMAQ_qattenLearner_teach
REGISTRY = {}

REGISTRY["q_learner"] = QLearner
REGISTRY["q_learner_teach"] = QLearner_Teach
REGISTRY["dmaq_qatten_learner"] = DMAQ_qattenLearner
REGISTRY["dmaq_qatten_learner_teach"] = DMAQ_qattenLearner_teach