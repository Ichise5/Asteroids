import pygame
from constants import *
from player import *
from asteroidfield import *
from shot import *

def main():
    print("Starting asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0


    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        dt = clock.tick(60) / 1000

        print(drawable)


        for object in updatable:
            object.update(dt)

        for object in drawable:
            object.draw(screen)

        for object in asteroids:
            if object.check_collision(player):
                print("Game over!")
                return
            for bullet in shots:
                if object.check_collision(bullet):
                    object.split()
                    bullet.kill()

        pygame.display.flip()

if __name__ == "__main__":
    main()