'''
Author: Tyler Gan
Date: 22 May 2020
Purpose: This file contains a function that will convert my matrix of objects into a presentable maze.
'''

from player import Player 
from game_parser import (read_lines, parse)

def grid_to_string(grid, player):
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    string = ''

    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            if i == player.row and j == player.col: 
                string += player.display 
                
            else:
                string += grid[i][j].display 
            
            if j == len(grid[i]) - 1:
                string += '\n'

            j += 1

        i += 1
    
    if player.memory_fragments == 1:
        string += '\nYou have {} memory fragments (💖).\n'.format(player.memory_fragments)
                
    else:
        string += '\nYou have {} memory fragments (💖).\n'.format(player.memory_fragments)
    
    return string