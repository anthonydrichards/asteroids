# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for updatable_obj in updatable:
            updatable_obj.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                return
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
        for drawable_obj in drawable:
            drawable_obj.draw(screen)        
        pygame.display.flip()

        dt = clock.tick(60)/1000



    
        


if __name__ == "__main__":
    main()
