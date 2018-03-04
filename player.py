from block import Block
class Player(Block):
    def __init__(self,game,grid_x,grid_y,grid_x_max,grid_y_max):
        Block.__init__(self,game,grid_x,grid_y,grid_x_max,grid_y_max,2)
    def move(self,motion):
        if self.grid['y']+motion>=self.grid['y_max'] or self.grid['y']+motion<0:
            return
        self.grid['y']+=motion
        self.update_state(self.grid['x'],self.grid['y'],self.grid['x_max'],self.grid['y_max'])
        print(self.grid['y_max'])
    
