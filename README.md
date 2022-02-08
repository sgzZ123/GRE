# Implementation of the paper Revisiting QMIX: Discriminative Credit Assignmentby Gradient Entropy Regularization

The code is based on PyMARL (https://github.com/oxwhirl/pymarl).

To get simple start on SMAC, you just need to follow the requirements in PyMARL and replace the src/ directory in pymarl with our src/ directory.

Use
```python
python3 src/main.py --config=qmix_GRE --env-config=sc2 with env_args.map_name=3s5z lamb=0.0001
```
to start training.

To start training with gridworld environments, follow the instructions in ma-gym (https://github.com/koulanurag/ma-gym).

