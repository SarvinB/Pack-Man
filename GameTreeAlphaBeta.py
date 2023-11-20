import GameBoard
from copy import deepcopy
import math
import random

class GameTreeAlphaBeta:
    
    def __init__(self, depth, randomness, probability):
        self.direction = None
        self.depth = depth
        self.prev_direction = 10
        self.first_direction = None
        self.is_dot = False
        self.randomness = randomness
        self.probability = probability   
    
    def minmax(self, depth, max_or_min, state, min_value, max_value):
        
        if state.board[state.packman.x_cordinate][state.packman.y_cordinate] == 1:
            state.path_score += 1
        #if terminal
        if depth == 0:
            direct_feature = abs(self.prev_direction - self.first_direction)
            u = state.e_utitliy(self.depth, direct_feature, self.is_dot)
            if state.board[state.packman.x_cordinate][state.packman.y_cordinate] == 1:
                state.path_score -= 1
            return u
        
        utility = 0
        if max_or_min == 0:
            utility, direction = self.max_level(depth, state, max_or_min, min_value, max_value)
        else:
            utility, direction = self.min_level(depth, state, max_or_min, min_value, max_value)
                      
        if depth == self.depth and direction is not None:
            self.direction = direction
        
        if state.board[state.packman.x_cordinate][state.packman.y_cordinate] == 1:
            state.path_score -= 1
        return utility
    
    def max_level(self, depth, state, max_or_min, min_value, max_value):
        max_or_min = 1
            
        utility = -math.inf
        direction = None
        random_num = random.random()
        if self.randomness == False or (self.randomness and random_num <= self.probability):     
            state.go_left()
            if state.board[state.packman.x_cordinate][state.packman.y_cordinate] != 2 or depth == 1:
                if depth == self.depth:
                    self.first_direction = 0
                    if state.board[state.packman.x_cordinate][state.packman.y_cordinate] == 1:
                        self.is_dot = True
                v = self.minmax(depth-1, max_or_min, state, min_value, max_value)
                if utility < v:
                    utility = v
                    direction = "left"
                if min_value != None and utility >= min_value:
                    state.go_right()
                    return utility, None
                if max_value == None or utility > max_value:
                    max_value = utility
            state.go_right()

        random_num = random.random()
        if self.randomness == False or (self.randomness and random_num <= self.probability): 
            state.go_right()
            if state.board[state.packman.x_cordinate][state.packman.y_cordinate] != 2 or depth == 1:
                if depth == self.depth:
                    self.first_direction = 1
                    if state.board[state.packman.x_cordinate][state.packman.y_cordinate] == 1:
                        self.is_dot = True
                v = self.minmax(depth-1, max_or_min, state, min_value, max_value)
                if utility < v:
                    utility = v
                    direction = "right"
                if min_value != None and utility >= min_value:
                    state.go_left()
                    return utility, None
                if max_value == None or utility > max_value :
                    max_value = utility
            state.go_left()
        
        random_num = random.random()
        if self.randomness == False or (self.randomness and random_num <= self.probability):     
            state.go_up()
            if state.board[state.packman.x_cordinate][state.packman.y_cordinate] != 2 or depth == 1:
                if depth == self.depth:
                    self.first_direction = 3
                    if state.board[state.packman.x_cordinate][state.packman.y_cordinate] == 1:
                        self.is_dot = True
                v = self.minmax(depth-1, max_or_min, state, min_value, max_value)
                if utility < v:
                    utility = v
                    direction = "up"
                if min_value != None and utility >= min_value:
                    state.go_down()
                    return utility, None
                if max_value == None or utility > max_value:
                    max_value = utility
            state.go_down()
            
        random_num = random.random()
        if self.randomness == False or (self.randomness and random_num <= self.probability):    
            state.go_down()
            if state.board[state.packman.x_cordinate][state.packman.y_cordinate] != 2 or depth == 1:
                if depth == self.depth:
                    self.first_direction = 4
                    if state.board[state.packman.x_cordinate][state.packman.y_cordinate] == 1:
                        self.is_dot = True
                v = self.minmax(depth-1, max_or_min, state, min_value, max_value)
                if utility < v:
                    utility = v
                    direction = "down"
                if min_value != None and utility >= min_value:
                    state.go_up()
                    return utility, None
                if max_value == None or utility > max_value:
                    max_value = utility
            state.go_up()

        return utility, direction
            
        
        
    def min_level(self, depth, state, max_or_min, min_value, max_value):
        if max_or_min == 2:
            max_or_min = 0
        else:
            max_or_min = 2
        
        utility = math.inf
        direction = None
        random_num = random.random()
        if self.randomness == False or (self.randomness and random_num <= self.probability):     
            state.go_left()
            if state.board[state.packman.x_cordinate][state.packman.y_cordinate] != 2 or depth == 1:
                if depth == self.depth:
                    self.first_direction = 0
                    if state.board[state.packman.x_cordinate][state.packman.y_cordinate] == 1:
                        self.is_dot = True
                v = self.minmax(depth-1, max_or_min, state, min_value, max_value)
                if utility > v:
                    utility = v
                    direction = "left"
                if max_value != None and utility <= max_value:
                    state.go_right()
                    return utility, None
                if min_value == None or utility < min_value:
                    max_value = utility
            state.go_right()

        random_num = random.random()
        if self.randomness == False or (self.randomness and random_num <= self.probability): 
            state.go_right()
            if state.board[state.packman.x_cordinate][state.packman.y_cordinate] != 2 or depth == 1:
                if depth == self.depth:
                    self.first_direction = 1
                    if state.board[state.packman.x_cordinate][state.packman.y_cordinate] == 1:
                        self.is_dot = True
                v = self.minmax(depth-1, max_or_min, state, min_value, max_value)
                if utility > v:
                    utility = v
                    direction = "right"
                if max_value != None and utility <= max_value:
                    state.go_left()
                    return utility, None
                if min_value == None or utility < min_value:
                    max_value = utility
            state.go_left()
        
        random_num = random.random()
        if self.randomness == False or (self.randomness and random_num <= self.probability):     
            state.go_up()
            if state.board[state.packman.x_cordinate][state.packman.y_cordinate] != 2 or depth == 1:
                if depth == self.depth:
                    self.first_direction = 3
                    if state.board[state.packman.x_cordinate][state.packman.y_cordinate] == 1:
                        self.is_dot = True
                v = self.minmax(depth-1, max_or_min, state, min_value, max_value)
                if utility > v:
                    utility = v
                    direction = "up"
                if max_value != None and utility <= max_value:
                    state.go_down()
                    return utility, None
                if min_value == None or utility < min_value:
                    max_value = utility
            state.go_down()
            
        random_num = random.random()
        if self.randomness == False or (self.randomness and random_num <= self.probability):    
            state.go_down()
            if state.board[state.packman.x_cordinate][state.packman.y_cordinate] != 2 or depth == 1:
                if depth == self.depth:
                    self.first_direction = 4
                    if state.board[state.packman.x_cordinate][state.packman.y_cordinate] == 1:
                        self.is_dot = True
                v = self.minmax(depth-1, max_or_min, state, min_value, max_value)
                if utility > v:
                    utility = v
                    direction = "down"
                if max_value != None and utility <= max_value:
                    state.go_up()
                    return utility, None
                if min_value == None or utility < min_value:
                    max_value = utility
            state.go_up()
            
        return utility, direction
  
        
        
    
    