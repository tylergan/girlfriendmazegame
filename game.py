'''
Author: Tyler Gan
Date: 22 May 2020
Purpose: This file contains my entire game class which stores all information about the state of the game; this is necessary for my run and solver.

Information stored here include:
    • The player state.
    • The grid state

Instance methods here are either used for the run file or the solver file.
    • game_move(), gridstr(), and IsValid() is for the run file
    • solver_move(), validTest(), and validSolver() is for the solver file
'''

from game_parser import (parse, read_lines)
from grid import grid_to_string
from player import Player
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Memory,
    Teleport
)

class Game:
    def __init__(self, filename, level):
        self.filename = filename
        self.level = level
        self.moves = []

        self.grid = parse(read_lines(self.filename))
        self.player = Player()
        self.conditions = ['w', 'a', 's', 'd', 'e', 'q', 'c']

    #game instance methods
    def game_move(self, move):
        self.player.move(move)
        self.moves.append(move)

    def gridstr(self):
        return grid_to_string(self.grid, self.player)

    def IsValid(self):
        if not (0 <= self.player.row <= len(self.grid) - 1):
            return False
        
        elif not (0 <= self.player.col <= len(self.grid[self.player.row]) - 1):
            return False
        
        return True