import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullet = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()

    Shot.containers = (bullet, updatable, drawable) 

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    current_time = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for obj in updatable:
            obj.update(dt)
        for obj in asteroids:
            # O(n^2) operation really bad
            bounce_group = []
            for astr in asteroids:
                if obj.collision(astr) and obj != astr:
                    if (obj, astr) not in bounce_group:
                        bounce_group.append(obj)
                        bounce_group.append(astr)
                        obj.bounce(astr)
            if obj.collision(player):
                print("Game over!")
                sys.exit()
            for bul in bullet:
                if bul.collision(obj):
                    bul.kill()
                    obj.split()

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = current_time.tick(60)/1000
    
    


if __name__ == "__main__":
    main()
