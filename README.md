# CTDS:Centralized Teacher with Decentralized Student for Multi-Agent Reinforcement Learning

This codebase accompanies paper *Centralized Teacher with Decentralized Student for Multi-Agent Reinforcement Learning.*

It is written in PyTorch and are based on the [Pymarl](https://github.com/oxwhirl/pymarl) algorithm library and  [SMAC](https://github.com/oxwhirl/smac)  codebases which are open-sourced.

The modified SMAC of CTDS is illustrated in the folder /smac of supplymentary material.

CTDS is a novel framework for deep multi-agent reinforcement learning and includes implementations of the following algorithms:

- [**VDN**: Value-Decomposition Networks For Cooperative Multi-Agent Learning](https://arxiv.org/abs/1706.05296) 
- [**QMIX**: QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning](https://arxiv.org/abs/1803.11485)
- [**QPLEX**: QPLEX: DUPLEX DUELING MULTI-AGENT Q-LEARNING](https://arxiv.org/pdf/2008.01062.pdf)

We also apply the corresponding algorithms implementations with the framework of CTDE as baselines.

## Installation instructions

Build the Dockerfile using 
```shell
cd docker
bash build.sh
```

Set up StarCraft II and SMAC:
```shell
bash install_sc2.sh
```

This will download SC2 into the 3rdparty folder and copy the maps necessary to run over.

The requirements.txt file can be used to install the necessary packages into a virtual environment (not recomended).

As for grid world environment $Combat$ , install it by

```
git clone https://github.com/koulanurag/ma-gym.git
```

and then replay ma-gym/ma_gym/envs/combat/combat.py by the version we provide.

## Run an experiment 

### In Combat

The following commands train QMIX  the paradigm "CTDS".

```shell
python3 src/main.py --config=qmix --env-config=gymma with env_args.key="ma_gym:Combat-v0" t_max=500000 paradigm='CTDS'
```

The following commands train QMIX  the paradigm "CTDE".

```shell
python3 src/main.py --config=qmix --env-config=gymma with env_args.key="ma_gym:Combat-v0" t_max=500000 paradigm='CTDE'
```

## In StarCraft

The following commands train QMIX  the paradigm "CTDS".

```shell
python3 src/main.py --config=qmix --env-config=sc2 with env_args.map_name=2s3z paradigm='CTDS'
```

The following commands train QMIX  the paradigm "CTDE".

```shell
python3 src/main.py --config=qmix --env-config=sc2 with env_args.map_name=2s3z paradigm='CTDE'
```

## Saving and loading learnt models

### Saving models

You can save the learnt models to disk by setting `save_model = True`, which is set to `False` by default. The frequency of saving models can be adjusted using `save_model_interval` configuration. Models will be saved in the result directory, under the folder called *models*. The directory corresponding each run will contain models saved throughout the experiment, each within a folder corresponding to the number of timesteps passed since starting the learning process.

### Loading models

Learnt models can be loaded using the `checkpoint_path` parameter, after which the learning will proceed from the corresponding timestep. 

## Watching StarCraft II replays

`save_replay` option allows saving replays of models which are loaded using `checkpoint_path`. Once the model is successfully loaded, `test_nepisode` number of episodes are run on the test mode and a .SC2Replay file is saved in the Replay directory of StarCraft II. Please make sure to use the episode runner if you wish to save a replay, i.e., `runner=episode`. The name of the saved replay file starts with the given `env_args.save_replay_prefix` (map_name if empty), followed by the current timestamp. 

The saved replays can be watched by double-clicking on them or using the following command:

```shell
python -m pysc2.bin.play --norender --rgb_minimap_size 0 --replay NAME.SC2Replay
```

**Note:** Replays cannot be watched using the Linux version of StarCraft II. Please use either the Mac or Windows version of the StarCraft II client.


