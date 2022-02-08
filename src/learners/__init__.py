from .q_learner import QLearner
from .coma_learner import COMALearner
from .qtran_learner import QLearner as QTranLearner
from .q_learner_simple import QLearner as QLearner_simple
from .q_learner_GRE import QLearner as QLearner_GRE

REGISTRY = {}

REGISTRY["q_learner"] = QLearner
REGISTRY["coma_learner"] = COMALearner
REGISTRY["qtran_learner"] = QTranLearner
REGISTRY["q_learner_simple"] = QLearner_simple
REGISTRY["q_learner_GRE"] = QLearner_GRE
