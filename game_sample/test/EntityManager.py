import Entity 
import pygame

T_ENEMY = "enemy"

class EntityManager:

    def __init__(self):
        self.entities = pygame.sprite.Group()

    def addEntity(self, entity):
        self.entities.add(entity)
    
    def clear(self):
        for entity in self.entities:
            if not entity.is_alive:
                entity.kill()
            