from block import Block
import random
OBSTICAL_MODE_MAP={
    'random_path_easy':{
        'variation':[-1,1],
        'interval':0,
        'gap':3
    }
}
class ObsticleGenerator:
    def __init__(self,game,height,width,mode='random_path_easy'):
        self.game=game
        self.mode=OBSTICAL_MODE_MAP[mode]
        self.variation=self.mode['variation']
        self.interval=self.mode['interval']
        self.gap=self.mode['gap']
        self.next_interval=self.interval
        self.height=height
        self.pointer=random.randint(0,height) #Start gap on random block
        self.width=width
        self.score=0
    def get_column(self):
        
        if self.next_interval>0:
            self.next_interval-=1
            return [Block(self.game,self.width,y,self.width,self.height) for y in range(0,self.height)]
        column=[Block(self.game,self.width,y,self.width,self.height,1) for y in range(0,self.height)]
        self.next_interval=self.get_value(self.interval)
        gap=self.get_value(self.gap)
        variation=self.get_value(self.variation)
        self.pointer+=variation
        if self.pointer>self.height:
            self.pointer-=abs(variation)#Force down by variation to bump
        if self.pointer<0:
            self.pointer+=abs(variation)
        if self.pointer>self.height or self.pointer<0:
            self.pointer=random.randint(0,self.height)#Give up if pointer still off grid
        if self.pointer+gap>self.height:
            self.pointer-=(self.pointer+gap-self.height)
        for y in range(self.pointer,self.pointer+gap):
            column[y]=Block(self.game,self.width,y,self.width,self.height,0) 
        self.score+=1
        return column

        
    def get_value(self,item):
        if isinstance(item,int):
            return item
        if isinstance(item,list) and len(item)==2:
            return random.randint(item[0],item[1])
        raise Exception("Could not get value for %r" % item)
        
