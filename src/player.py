from circleshape import *
import pygame
from constants import *
from time import sleep

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        #self.position = pygame.Vector2(x,y)
        self.rotation = 0
        self.time = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.time - dt > 0:
            self.time -= dt
        else:
            self.time = 0

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.time == 0:
                self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        front_vec = pygame.Vector2(0,1).rotate(self.rotation)
        spawn_loc = self.position + front_vec * self.radius * 1.4
        bullet = Shot(spawn_loc[0], spawn_loc[1])
        bullet.velocity = PLAYER_SHOOT_SPEED*front_vec
        self.time = PLAYER_SHOOT_COOLDOWN

class Shot(CircleShape):
    def __init__(self, x ,y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position,self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
