# CAU56753 Challenge II: Route Search

## Problem definition / 문제정의

The second programming challenge is simpler than the first one.

In this challenge, you have to make a local search algorithm for finding the **BEST** position of your initial villages.


Here's PEAS description. According to the description, the system will automatically run your code and give you the evaluation result.


(Are you curious about how to run the evaluation? Then, go to [RUN](./#RUN) section!)

### PEAS description

#### Performance measure (수행지표)

Presented in the order of importance in evaluation.


  1. The number of errored trials (smaller is better)

  2. The expected resource income at that village, for the next five turns (larger is better)

     Note that some of resources will be weighted more compared to the other resources, when computing the expected resource income.

     For example, a game board can emphasize the importance of brick cards twice greater than the other resource cards, by giving weight two for bricks and one for the others.
    
     You can check the expected resource income for a state by calling `board.evaluate_state(state)`.

  3. The number of `board.evaluate_state()` calls (smaller is better)

  4. The maximum memory usage (smaller is better; rounded down in MB)

     The usage lower than 200MB is treated as 200MB.


**Note**: Evaluation program will automatically build a table that sort your codes' evaluation result in the order of performance measure. Also, the algorithm should finish its search procedure **within 1 minutes**.

**Note**: Also, the program should use lower than **1GB in total**, including your program code on the memory. For your information: when I tested with `default.py`, the memory usage after initial loading is 22MB.


#### Environment (환경)

Okay, the environment follows the initial set-up procedure in the Settlers of Catan game. Here, your agent is not the only one to settle down. Before you're making your decision, some of the players may have placed their initial settlements. So, you need to do is placing one of your initial village to increase your resource income. Note that the game board is randomly generated, and the importance (weight) of resource cards is hidden to the players.

1. Other players will do nothing in the game until your search is done. You don't have to worry about the thief or a knight card.

2. Note that the order of building settlement is 1-2-3-4-4-3-2-1 in the basic Catan rule. Your agent is facing one of the eight cases. So, for the latter four turns (i.e., 4-3-2-1 at the last), the agent might have a village on the board randomly.

In terms of seven characteristics, the game can be classified as:

- Almost Fully observable (거의 완전관측가능)

  You already know everything required to decide your action, except the weight of resources.

- Single-agent (단일 에이전트)

  The other agents are actually doing nothing. So you're the only one who pursues those performance measure.

- Deterministic (결정론적)

  There's no probabilistic things or unexpected chances when deciding the next state. Everything is deterministic.

- Episodic actions (일화적 행동)

  You don't need to handle the sequence of your actions to build an initial village.

- Semi-dynamic performance (준역동적 지표)

  Note that performance metrics 1, 2 are static, but the metrics 3, 4 is dynamic metric, which changes its measure by how your algorithm works. So you need some special effort for achieving good performance measure on 3 and 4, when designing your algorithm.

- Discrete action, perception, state and time (이산적인 행동, 지각, 상태 및 시간개념)

  All of your actions, perceptions, states and time will be discrete, although you can query about your current memory usage in the computing procedure.

- Known rules (규칙 알려짐)

  All rules basically follows the original Catan game, except the rules specified above.

#### Actions

You can take one of the following actions.

- **VILLAGE(v)**: Build a village at a specific node `v`.

  Here, the list of applicable nodes will be given by the board. The list may be empty if you reached the maximum number of villages, i.e., three.


**Note**: You cannot do reverse-enginnering to find out actual importance value of resource cards. All you can do is doing local search on the board.


#### Sensors

You can perceive the game state as follows:

- The board (게임 판)
  - All the place of hexes(resources), villages, roads and ports

  - You can ask the board to the list of applicable actions for.

  - You can ask the board about the expected total resource income of current state, for five turns.  
  
- Your resource cards (여러분의 자원카드 목록)



## Structure of evaluation system

The evaluation code has the following structure.

```text
/                   ... The root of this project
/README.md          ... This README file
/evaluate.py        ... The entrance file to run the evaluation code
/board.py           ... The file that specifies programming interface with the board
/actions.py         ... The file that specifies actions to be called
/util.py            ... The file that contains several utilities for board and action definitions.
/agents             ... Directory that contains multiple agents to be tested.
/agents/__init__.py ... Helper code for loading agents to be evaluated
/agents/load.py     ... Helper code for loading agents to be evaluated
/agents/default.py  ... A default DFS agent 
/agents/_skeleton.py... A skeleton code for your agent. (You should change the name of file to run your code)
```

All the codes have documentation that specifies what's happening on that code (only in English).

To deeply understand the `board.py` and `actions.py`, you may need some knowlege about [`pyCatan2` library](https://pycatan.readthedocs.io/en/latest/index.html).


### What should I submit?

You should submit an agent python file, which has a similar structure to `/agents/default.py`.
That file should contain a class name `Agent` and that `Agent` class should have a method named `search_for_longest_route(board)`.
Please use `/agents/_skeleton.py` as a skeleton code for your submission.


Also, you cannot use the followings to reduce your search time:

- multithreading / 멀티스레딩
- multiprocessing / 멀티프로세싱
- using other libraries other than basic python libraries. / 기본 파이썬 라이브러리 이외에 다른 라이브러리를 사용하는 행위

The TA will check whether you use those things or not. If so, then your evaluation result will be marked as zero.

## RUN


To run the evaluation code, do the following:

1. (Only at the first run) Install the required libraries, by run the following code on your terminal or powershell, etc:

    ```bash
    pip install -r requirements.txt
    ```

2. Place your code under `/agents` directory.

3. Execute the evaluation code, by run the following code on a terminal/powershell:

    ```bash 
    python evaluate.py
    ```

    If you want to print out all computational procedure, then put `--debug` at the end of python call, as follows:

    ```bash 
    python evaluate.py --debug
    ```

4. See what's happening.


Note: All the codes are tested both on (1) Windows 11 (23H2) with Python 3.9.13 and (2) Ubuntu 22.04 with Python 3.10. Sorry for Mac users, because you may have some unexpected errors.
