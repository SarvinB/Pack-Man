from copy import copy
import math

class State:
    
    def __init__(self, board, ghosts, packman, length, width, coefficients, panic_dist):
        
        self.packman = packman
        self.ghosts = ghosts
        self.board = board
        self.width = width
        self.length = length
        self.utility = 0
        self.path_score = 0
        self.coefficients = coefficients
        self.panic_dist = panic_dist
        
    def neighbor_scores(self):

        score = 0
        x = self.packman.x_cordinate
        y = self.packman.y_cordinate
        if x >= 1:
            if self.board[x-1][y] == 1:
                score += 1
        else:
            if self.board[self.width-1][y] == 1:
                score += 1
        if y >= 1:
            if self.board[x][y-1] == 1:
                score += 1
        else:
            if self.board[x][self.length-1] == 1:
                score += 1
        if x < self.width-1:
            if self.board[x+1][y] == 1:
                score += 1
        else:
            if self.board[0][y] == 1:
                score += 1
        if y < self.length-1:
            if self.board[x][y+1] == 1:
                score += 1
        else:
            if self.board[x][0] == 1:
                score += 1
        
        return score*self.coefficients["neighbors"]
    
    def e_utitliy(self, depth, direct_feature, is_dot):
        
        utility = 0
        if is_dot:
            utility += 1*self.coefficients["dot"]
            
        if self.board[self.packman.x_cordinate][self.packman.y_cordinate] == 2:
            utility -= 1*self.coefficients["wall"]
            
        if direct_feature == 1: 
            utility -= 1*self.coefficients["loop"]
        
        for ghost in self.ghosts:
            manh_dis = abs(self.manhatan_dist(ghost)-depth/3)
            if manh_dis <= self.panic_dist:
                utility -= 1*self.coefficients["manhatan"]
                
        utility += self.path_score*self.coefficients["path"]
                
        utility += self.neighbor_scores()
        
        return utility

    
    def manhatan_dist(self, ghost):
        
        x_types = [abs((self.width-ghost.x_cordinate)-self.packman.x_cordinate), abs(ghost.x_cordinate-self.packman.x_cordinate)]
        y_types = [abs((self.length-ghost.y_cordinate)-self.packman.y_cordinate), abs(ghost.y_cordinate-self.packman.y_cordinate)]

        
        min_dist = -math.inf
        
        for i in range(2):
            for j in range(2):
                min_dist = min(min_dist, x_types[i]+y_types[j])
        
        return min_dist
                    
        
        
    def go_up(self):
        if self.packman.x_cordinate <= 0:
            self.packman.x_cordinate = self.width-1
        else:
            self.packman.x_cordinate -= 1
            
    def go_left(self):
        if self.packman.y_cordinate <= 0:
            self.packman.y_cordinate = self.length-1
        else:
            self.packman.y_cordinate -= 1
            
    def go_down(self):
        if self.packman.x_cordinate >= self.width-1:
            self.packman.x_cordinate = 0
        else:
            self.packman.x_cordinate += 1

            
    def go_right(self):
        if self.packman.y_cordinate >= self.length-1:
            self.packman.y_cordinate = 0
        else:
            self.packman.y_cordinate += 1

        