import pygame
from constants import *
if __name__ == "__main__":
    def main():
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        print("Starting Asteroids!")
        print(f'Screen width: {SCREEN_WIDTH}')
        print(f'Screen height: {SCREEN_HEIGHT}')
        while(True):
           for event in pygame.event.get():
               screen.fill((0,0,0))
               pygame.display.flip()
               if event.type == pygame.QUIT:
                   return
    main()
