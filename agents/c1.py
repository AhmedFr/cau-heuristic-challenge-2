from random import choice
from time import time
from typing import Tuple, List

from action import *
from board import GameBoard


class Agent:  # Do not change the name of this class!
    """
    An agent class (Skeleton)
    """
      
    # local search algorithm, Hill climbing
    def decide_new_village(self, board: GameBoard, time_limit: float = None) -> Tuple[int, int]:
        """
        This algorithm search for the best place of placing a new village.

        :param board: Game board to manipulate
        :param time_limit: Timestamp for the deadline of this search.
        :return: Tuple of coordinates
        """
        initial = board.get_state()
        applicable_villages = board.get_applicable_villages()
        current = choice(applicable_villages)
        board.simulate_action(initial, VILLAGE(current))
        current_fitness = board.evaluate_state()
        while time() < time_limit:
            next_pos = choice(applicable_villages)
            board.simulate_action(initial, VILLAGE(next_pos))
            next_fitness = board.evaluate_state()
            if next_fitness < current_fitness:
                current = next_pos
                current_fitness = next_fitness
        return current
