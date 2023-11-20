import GameBoard
from copy import deepcopy
import math
import random

class GameTree:
    
    def __init__(self, depth, randomness, probability):
        self.direction = None
        self.depth = depth
        self.prev_direction = 10
        self.first_direction = None
        self.is_dot = False
        self.randomness = randomness
        self.probability = probability 
    
    def minmax(self, depth, max_or_min, state):
        
        if state.board[state.packman.x_cordinate][state.packman.y_cordinate] == 1:
            state.path_score += 1
        #if terminal
        if depth == 0:
            direct_feature = abs(self.prev_direction - self.first_direction)
            u = state.e_utitliy(self.depth, direct_feature, self.is_dot)
            if state.board[state.packman.x_cordinate][state.packman.y_cordinate] == 1:
                state.path_score -= 1
            return u
        
        right_utility = None
        left_utility = None
        up_utility = None
        down_utility = None
        
        prev_min_or_max = max_or_min
        if max_or_min == 2:
            max_or_min = 0
        else:
            max_or_min += 1
            
        random_num = random.random()
        if self.randomness == False or (self.randomness and random_num <= self.probability):     
            state.go_left()
            if state.board[state.packman.x_cordinate][state.packman.y_cordinate] != 2 or depth == 1:
                if depth == self.depth:
                    self.first_direction = 0
                    if state.board[state.packman.x_cordinate][state.packman.y_cordinate] == 1:
                        self.is_dot = True
                left_utility = self.minmax(depth-1, max_or_min, state)
            state.go_right()

        random_num = random.random()
        if self.randomness == False or (self.randomness and random_num <= self.probability): 
            state.go_right()
            if state.board[state.packman.x_cordinate][state.packman.y_cordinate] != 2 or depth == 1:
                if depth == self.depth:
                    self.first_direction = 1
                    if state.board[state.packman.x_cordinate][state.packman.y_cordinate] == 1:
                        self.is_dot = True
                right_utility = self.minmax(depth-1, max_or_min, state)
            state.go_left()
        
        random_num = random.random()
        if self.randomness == False or (self.randomness and random_num <= self.probability):     
            state.go_up()
            if state.board[state.packman.x_cordinate][state.packman.y_cordinate] != 2 or depth == 1:
                if depth == self.depth:
                    self.first_direction = 3
                    if state.board[state.packman.x_cordinate][state.packman.y_cordinate] == 1:
                        self.is_dot = True
                up_utility = self.minmax(depth-1, max_or_min, state)
            state.go_down()
            
        random_num = random.random()
        if self.randomness == False or (self.randomness and random_num <= self.probability):    
            state.go_down()
            if state.board[state.packman.x_cordinate][state.packman.y_cordinate] != 2 or depth == 1:
                if depth == self.depth:
                    self.first_direction = 4
                    if state.board[state.packman.x_cordinate][state.packman.y_cordinate] == 1:
                        self.is_dot = True
                down_utility = self.minmax(depth-1, max_or_min, state)
            state.go_up()
            
        utility, direction = self.find_utility(prev_min_or_max, right_utility, left_utility, up_utility, down_utility)
        if depth == self.depth:
            self.direction = direction
        
        if state.board[state.packman.x_cordinate][state.packman.y_cordinate] == 1:
            state.path_score -= 1
        return utility
    
    def find_utility(self, max_min, right, left, up, down):
        
        utility = 0
        direction = None
        if max_min == 0:
            utility = -math.inf
            if left != None and left >= utility:
                utility = left
                direction = "left"
            if right != None and right >= utility:
                utility = right
                direction = "right"
            if up != None and up >= utility:
                utility = up
                direction = "up"
            if down != None and down >= utility:
                utility = down
                direction = "down"
            
        else:
            utility = math.inf
            if left != None and left <= utility:
                utility = left
                direction = "left"
            if right != None and right <= utility:
                utility = right
                direction = "right"
            if up != None and up <= utility:
                utility = up
                direction = "up"
            if down != None and down <= utility:
                utility = down
                direction = "down"
        
        return utility, direction
        
        
    
    