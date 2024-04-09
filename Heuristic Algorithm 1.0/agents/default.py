from random import choice
from time import time
from typing import Tuple, List

from action import *
from board import GameBoard


class Agent:  # Do not change the name of this class!
    """
    An agent class, with hill climbing method
    """

    def get_random_neighborhood(self, candidates: List[Tuple[int, int]], current: Tuple[int, int]) -> Tuple[int, int]:
        """
        Generate a random neighborhood of the current junction.

        :param candidates: Candidate list of placements
        :param current: Current position tested

        :return: Tuple of random neighborhood of current position
        """
        # Get the current coordinate
        r, s = current
        # Find the coordinate whose distance <= 1
        neighbors = [(r1, s1)
                     for r1, s1 in candidates
                     if abs(r - r1) + abs(s - s1) == 1 or (abs((r - r1) + (s - s1)) == 0 and abs(r - r1) == 1)]

        # Pick a random neighbor if possible. Otherwise, use the current value.
        return choice(neighbors) if len(neighbors) > 0 else current

    def decide_new_village(self, board: GameBoard, time_limit: float = None) -> Tuple[int, int]:
        """
        This algorithm search for the best place of placing a new village.

        :param board: Game board to manipulate
        :param time_limit: Timestamp for the deadline of this search.
        :return: Tuple of coordinates
        """
        initial = board.get_state()

        # Get a random choice of placement
        applicable_villages = board.get_applicable_villages()
        current = choice(applicable_villages)

        # Simulate and evaluate current placement
        board.simulate_action(initial, VILLAGE(current))
        current_fitness = board.evaluate_state()

        while time() < time_limit:
            # Get a random neighbor of the current placement
            next_pos = self.get_random_neighborhood(applicable_villages, current)
            # Simulate and evaluate new placement
            board.simulate_action(initial, VILLAGE(next_pos))
            next_fitness = board.evaluate_state()

            if next_fitness < current_fitness:
                current = next_pos
                current_fitness = next_fitness

        return current
