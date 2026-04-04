import pygame
from Components import MovementComponent, RenderComponent, CollisionComponent, InputComponent

class Entity(pygame.sprite.Sprite):

    def __init__(self, is_alive):
        self.is_alive = is_alive
        super().__init__()

    def hasattr(self, attr):
        return hasattr(self, attr)

class Enemy(Entity):
    def __init__(self, movement_component: MovementComponent, render_component: RenderComponent, collision_component: CollisionComponent):
        super().__init__(is_alive=True)
        self.c_movement = movement_component
        self.c_render = render_component
        self.c_collision: CollisionComponent = collision_component

    # def update(self):
    #     self.c_render.position[0] += self.c_movement.speed[0]
    #     self.c_render.position[1] += self.c_movement.speed[1]
    #     pass

    # def render(self, screen):
    #     pygame.draw.rect(screen, self.c_render.color, (*self.c_render.position, *self.c_render.size))
    #     pass
class Player(Entity):
    def __init__(self, movement_component: MovementComponent, 
                 render_component: RenderComponent, 
                 collision_component: CollisionComponent,
                 input_component: InputComponent,
                 ):
        super().__init__(is_alive=True)
        self.c_movement = movement_component
        self.c_render = render_component
        self.c_collision: CollisionComponent = collision_component
        self.c_input: InputComponent = input_component

class Bullet(Entity):
    def __init__(self, 
                 movement_component: MovementComponent, 
                 render_component: RenderComponent, 
                 collision_component: CollisionComponent,
                 ):
        super().__init__(is_alive=True)
        self.c_movement = movement_component
        self.c_render = render_component
        self.c_collision: CollisionComponent = collision_component