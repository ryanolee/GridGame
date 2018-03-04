import pygame,configparser
from game import Game
def main():
    parser=configparser.ConfigParser()
    parser.read('game.ini')
    pygame.init()
    while True:
        game=Game(parser,pygame)
        game.start_level(30)
        game.main_loop()
    
if __name__=='__main__':
    main()