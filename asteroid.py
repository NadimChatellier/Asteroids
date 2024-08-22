import pygame
from circleshape import CircleShape 
from pygame import Vector2
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)  # Pass x, y, and radius if all are needed by CircleShape
        self.centre = Vector2(x, y)
        self.velocity = velocity
        pygame.sprite.Sprite.__init__(self, self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.centre, self.radius, 2)

    def update(self, dt):
        self.centre += self.velocity * dt