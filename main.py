from GameBoard import GameBoard
from PackMan import PackMan
from Ghost import Ghost
from State import State
from GameTree import GameTree
from copy import copy
import time
import math
from GameTreeAlphaBeta import GameTreeAlphaBeta
import os
import timeit
import numpy as np
import csv

#Choose number of Run
counter = 10
packMan_score = np.array([0 for j in range(counter)])
packMan_result = np.array([0 for j in range(counter)])  

number_of_wins = 0
start = timeit.default_timer()
for c in range(counter):
    #Enter your properties:
    depth = 20
    # neighbors: Positive score for being dot in neghbor of last state
    # dot: Positive score for being dot in first move
    # path: Positive score for dots in path
    # wall: Negetive score for move to wall
    # loop: Negetive score for moving in previous direction
    # manhatan: Negetive score for be close to Ghosts
    coefficients = {"neighbors":8, "dot":3, "wall":2, "loop":3, "manhatan":5, "path":10}
    panic_dist = 6
    randomness = False
    probability = 0.95
    wall_rate = 0.1
    board_length = 18
    board_width = 9
    
    pack_man = PackMan(0, 0, board_length, board_width)
    ghost_1 = Ghost(8, 8, board_length, board_width)
    ghost_2 = Ghost(7, 15, board_length, board_width)
    game_board = GameBoard(board_length, board_width, [ghost_1, ghost_2], pack_man, wall_rate)
    
    initial_state = State(game_board.board, [ghost_1, ghost_2], pack_man, game_board.length, game_board.width, coefficients, panic_dist)
    
    # First one is regular Tree, second one is with Alpha-Beta pruning
    # game_tree = GameTree(depth, randomness, probability)
    game_tree = GameTreeAlphaBeta(depth, randomness, probability)

    e = 2
    while(e == 2):
        u = game_tree.minmax(depth, 0, initial_state, None, None)
        # u = game_tree.minmax(depth, 0, initial_state)
        e = game_board.play(game_tree.direction)
        if e != 2:
            packMan_result[c] = e
            packMan_score[c] = pack_man.score
            if e == 1:
                number_of_wins += 1
            
        os.system('clear')
        game_board.display()

        if game_tree.direction == "left":
            game_tree.prev_direction = 0
        elif game_tree.direction == "right":
            game_tree.prev_direction = 1
        elif game_tree.direction == "up":
            game_tree.prev_direction = 3
        elif game_tree.direction == "down":
            game_tree.prev_direction = 4
        game_tree.direction = None
        game_tree.is_dot = False
        
        # If you decressing depth, active it:
        # time.sleep(0.5)       
    stop = timeit.default_timer()
#    with open('resultAlpahBeta.csv', 'a', newline='') as file:
#        writer = csv.writer(file)
#        writer.writerow([coefficients["neighbors"], coefficients["dot"], coefficients["wall"], coefficients["loop"], coefficients["manhatan"], coefficients["path"], panic_dist, wall_rate, depth, randomness, probability, np.average(packMan_score), np.amax(packMan_score), np.min(packMan_score), number_of_wins/counter, (stop - start)/counter])
    
