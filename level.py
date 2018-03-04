from block import Block
from player import Player
from obsticle_genarator import ObsticleGenerator
import pygame
import math
class Level():
    def __init__(self,game):
        self.screen=game.screen
        self.game=game
        self.state=[]
        self.clock=self.game.pg.time.Clock()
        self.frames=0
        self.speed=4
    def start_level(self,height):
        s_width,s_height=self.screen.get_size()
        width=math.ceil(height*(s_width/s_height)) #blocks per collumn*(screen ratio)
        print('Starting new level with width %d and height %d' % (height,width))
        self.state=[[Block(self.game,x,y,width,height) for y in  range(0,height)] for x in range(0,width)]
        self.height=height
        self.width=width
        self.obsticle_generator=ObsticleGenerator(self.game,self.height,self.width)
        self.state.append(self.obsticle_generator.get_column())
        self.player=Player(self.game,int(width/2),int(height/2),width,height)
        self.running=True
        self.frames=0
    def update(self):
        self.frames+=1
        self.clock.tick()
        if self.frames%self.speed==0:
            self.shift_blocks()
    def render(self):
        for column in self.state:
            for block in column:
                block.render()
        self.player.render()
    def shift_blocks(self):
        self.state.pop(0)
        for column in self.state:
            for block in column:
                block.update_state(block.grid['x']-1,block.grid['y'],self.width,self.height)
        self.state.append(self.obsticle_generator.get_column())
    def loop(self,events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print('up')
                    self.player.move(-1)
                if event.key == pygame.K_DOWN:
                    print('down')
                    self.player.move(1)
        x=self.player.grid['x']
        y=self.player.grid['y']
        if self.state[x][y].state==1:
            print('Ded! Score %d' % self.obsticle_generator.score)
            self.running=False