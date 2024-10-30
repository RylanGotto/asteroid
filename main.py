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
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    updatable.add(player)
    drawable.add(player)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    asteroid_field = AsteroidField()
    


    dt = 0

    print(Player.containers)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        for i in drawable:
            i.draw(screen)

        for i in updatable:
            i.update(dt)

        for i in asteroids:
            if player.check_for_collisions(i):
                print('Game Over!')
                return
        
        for i in asteroids:
            for k in shots:
                if k.check_for_collisions(i):
                    i.split()

        pygame.display.flip()


        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
