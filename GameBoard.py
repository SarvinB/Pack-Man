import random
import numpy as np
from PackMan import PackMan
from Ghost import Ghost

class GameBoard:
    
    def __init__(self, length, width, ghosts, packman, rate):
        self.packman = packman
        self.ghosts = ghosts
        self.length = length
        self.width = width
        self.number_of_dots = self.length*self.width-1
        self.board = np.array([[1 for i in range(length)] for j in range(width)]) # 0 -> eaten dot & 1 -> remain dot & 2 -> wall & packman -> 3 & ghost -> 4
        self.random_generate_wall(rate)
        self.add_players()
        
    
    def random_generate_wall(self, rate):
        for x in range(self.width):
            for y in range(self.length):
                r = random.random()
                if r <= rate:
                    self.board[x][y] = 2
                    self.number_of_dots -= 1
                    
    def add_players(self):
        self.board[self.packman.x_cordinate][self.packman.y_cordinate] = 3
        for g in self.ghosts:
            self.board[g.x_cordinate][g.y_cordinate] = 4
            
    def play(self, direction):
        
        x_p = self.packman.x_cordinate
        y_p = self.packman.y_cordinate
        
        is_changed = self.packman.move(direction, self.board)
        if is_changed:
            self.board[x_p][y_p] = 0
        
        self.packman.prev_x_cordinate = x_p
        self.packman.prev_y_cordinate = y_p
        
        self.update_board()
        e = self.is_end()
        if e != 2:
            return e
            
        for g in self.ghosts:
            g_x = g.x_cordinate
            g_y = g.y_cordinate
            is_changed = g.move(self.board)
            if is_changed:
                if g.is_dot:
                    self.board[g_x][g_y] = 1
                else:
                    self.board[g_x][g_y] = 0
            
            
        self.update_board()
        return self.is_end()
            
    def is_end(self): # 0: loose 1: win 2: continue
        
        for g in self.ghosts:
            if self.packman.x_cordinate == g.x_cordinate and self.packman.y_cordinate == g.y_cordinate:
                # print("Pack Man lost :(")
                return 0
        
        if self.number_of_dots == 0:
            # print("Pack Man win :)")
            return 1
        
        return 2
            
    def update_board(self):
        
        if self.board[self.packman.x_cordinate][self.packman.y_cordinate] == 1:
            self.packman.score += 10
            self.number_of_dots -= 1
        if self.board[self.packman.x_cordinate][self.packman.y_cordinate] != 2:
            self.packman.score -= 1
        self.board[self.packman.x_cordinate][self.packman.y_cordinate] = 3
            
        for g in self.ghosts:
            if self.board[g.x_cordinate][g.y_cordinate] == 1:
                g.is_dot = True
            if self.board[g.x_cordinate][g.y_cordinate] == 0:
                g.is_dot = False
            self.board[g.x_cordinate][g.y_cordinate] = 4
            
    def display(self):
        print("Pack Man score = ", self.packman.score)
        for i in range(self.width):
            for j in range(self.length):
                if self.board[i][j] == 3:
                    print("P", end=' ')
                elif self.board[i][j] == 4:
                    print("G", end=' ')
                elif self.board[i][j] == 2:
                    print("|", end=' ')
                elif self.board[i][j] == 0:
                    print(" ", end=' ')
                else:
                    print(".", end=' ')
            print()
        print()
            
        

                    
   
                    
                     

        
       