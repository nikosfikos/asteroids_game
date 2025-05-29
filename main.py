import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers =(shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroids = AsteroidField()

    while(True):
        for event in pygame.event.get():
            clock.tick(60)
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)
        for obj in asteroid:
            if obj.collides_with(player):
                sys.exit("Game Over!")
            for shot in shots:
                if obj.collides_with(shot):
                    obj.split()
                    shot.kill()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        #limit the framerate to 60 FPS
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
