import pygame
from level import Level
from pygame.locals import *
class Game():
    def __init__(self,config,pygame):
        if config['screen']['fullscreen']=='y':
            self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        else:
            self.screen=pygame.display.set_mode((int(config['screen']['width']),int(config['screen']['height'])))
        pygame.display.toggle_fullscreen()
        self.pg=pygame
        self.level=Level(self)
        self.running=True
    def start_level(self,scale):
        self.level.start_level(scale)
    def main_loop(self):
        while self.level.running and self.running:
            self.screen.fill((0, 120, 120))
            self.level.update()
            self.level.render()
            events=self.pg.event.get()
            self.level.loop(events)
            for event in events:
                if event.type == QUIT:
                    self.running=False
            pygame.display.flip()
        #self.pg.quit()
        

        