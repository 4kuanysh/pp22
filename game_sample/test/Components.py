import pygame

class LifeComponent:
    def __init__(self, health):
        self.health = health

class MovementComponent:
    def __init__(self, speed, position):
        self.position = position
        self.speed = speed

class RenderComponent:
    def __init__(self, surface, size, color):
        self.surface = surface
        self.size = size
        self.color = color
        
class CollisionComponent:
    def __init__(self, rect: pygame.Rect):
        self.rect = rect

class InputComponent:
    def __init__(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False