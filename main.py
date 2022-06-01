import pygame, sys
from pygame.locals import *

import engine
import menu

def main():
    pygame.init()
    ALTURA = 400
    LARGURA = 300

    DISPLAYSURF = pygame.display.set_mode((ALTURA, LARGURA))

    menu.menu(DISPLAYSURF)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    
if __name__ == '__main__':
    main()
