import random
class Block():
    def __init__(self,game,grid_x,grid_y,grid_x_max,grid_y_max,state=0):
        self.game=game
        self.state=state
        self.update_state(grid_x,grid_y,grid_x_max,grid_y_max)
    def render(self):
        self.game.pg.draw.rect(self.game.screen,self.get_color(),self.rect)
    def update_state(self,grid_x,grid_y,grid_x_max,grid_y_max):
        s_height=self.game.screen.get_height()
        self.size=s_height/grid_y_max
        self.grid={
            "x":grid_x,
            "y":grid_y,
            "x_max":grid_x_max,
            "y_max":grid_y_max
            }
        self.x=self.grid["x"]*self.size
        self.y=self.grid["y"]*self.size
        self.rect=self.game.pg.Rect((self.x,self.y),(self.size-2,self.size-2))
    def get_color(self):
        return [(255,255,255),(0,0,0),(0,255,255)][self.state]
       
