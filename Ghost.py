import random

class Ghost:
    
    def __init__(self, x_cordinate, y_cordinate, length, width):
        self.x_cordinate = x_cordinate
        self.y_cordinate = y_cordinate
        self.width = width
        self.length = length
        self.is_dot = True
        
    def move(self, board):
        d = random.randint(1, 4)
        is_changed = False
        if d == 1:
            if self.x_cordinate <= 0 and board[self.width-1][self.y_cordinate] != 2:
                self.x_cordinate = self.width-1
                is_changed = True
            elif self.x_cordinate > 0 and board[self.x_cordinate-1][self.y_cordinate] != 2:   
                self.x_cordinate -= 1
                is_changed = True
        
        elif d == 2:
            if self.x_cordinate >= self.width-1 and board[0][self.y_cordinate] != 2:
                self.x_cordinate = 0
                is_changed = True
            elif self.x_cordinate < self.width-1 and board[self.x_cordinate+1][self.y_cordinate] != 2:  
                self.x_cordinate += 1
                is_changed = True
          
        elif d == 3:
            if self.y_cordinate >= self.length-1 and board[self.x_cordinate][0] != 2:
                self.y_cordinate = 0
                is_changed =  True
            elif self.y_cordinate < self.length-1 and board[self.x_cordinate][self.y_cordinate+1] != 2:  
                self.y_cordinate += 1
                is_changed = True
          
        elif d == 4:
            if self.y_cordinate <= 0 and board[self.x_cordinate][self.length-1] != 2:
                self.y_cordinate = self.length-1
                is_changed = True
            elif self.y_cordinate > 0 and board[self.x_cordinate][self.y_cordinate-1] != 2: 
                self.y_cordinate -= 1
                is_changed = True
            
        return is_changed
        
        
    