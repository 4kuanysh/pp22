import pygame
import test.Colors as Colors
import test.Components as Components
from test.Entity import Entity, Enemy, Player, Bullet
from random import randint
from test.EntityManager import EntityManager, T_ENEMY

class GameEngine:

    WHITE = (255, 255, 255)

    def __init__(self, window, fps=60):
        pygame.init()
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.screen = pygame.display.set_mode(window)
        self.FPS = fps
        self.clock = pygame.time.Clock()
        self.running = True
        self.entityManger = EntityManager()
        self.create_player()

    def run(self):
        while self.running:
            self.event_system()
            self.collision_system()
            self.movement_system()
            self.render_system()
            self.clock.tick(self.FPS)
            self.entityManger.clear()

    def event_system(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.USEREVENT:
                self.create_enemy()
            if event.type == pygame.KEYDOWN:
                for entity in self.entityManger.entities:
                    if entity.hasattr("c_input"):
                        if event.key == pygame.K_LEFT:
                            entity.c_input.left = True
                        elif event.key == pygame.K_RIGHT:
                            entity.c_input.right = True
                        elif event.key == pygame.K_UP:
                            entity.c_input.up = True
                        elif event.key == pygame.K_DOWN:
                            entity.c_input.down = True
            if event.type == pygame.KEYUP:
                for entity in self.entityManger.entities:
                    if entity.hasattr("c_input"):
                        if event.key == pygame.K_LEFT:
                            entity.c_input.left = False
                        elif event.key == pygame.K_RIGHT:
                            entity.c_input.right = False
                        elif event.key == pygame.K_UP:
                            entity.c_input.up = False
                        elif event.key == pygame.K_DOWN:
                            entity.c_input.down = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for entity in self.entityManger.entities:
                    if isinstance(entity, Player):
                        player_pos = entity.c_collision.rect.center
                        x = mouse_pos[0] - player_pos[0] 
                        y = mouse_pos[1] - player_pos[1]
                    
                        vec: pygame.Vector2 = pygame.Vector2(x, y)
                        vec.normalize_ip()
                        vec = vec * 5
                        
                        self.create_bullet((vec.x, vec.y), player_pos)

    def movement_system(self):
        for entity in self.entityManger.entities:
            if isinstance(entity, Enemy) or isinstance(entity, Bullet):
                new_pos = (entity.c_movement.position[0] + entity.c_movement.speed[0],
                           entity.c_movement.position[1] + entity.c_movement.speed[1])
                entity.c_movement.position = new_pos
                
            elif isinstance(entity, Player):    
                if entity.c_input.left:
                    entity.c_movement.position = (entity.c_movement.position[0] - entity.c_movement.speed[0], entity.c_movement.position[1])
                if entity.c_input.right:
                    entity.c_movement.position = (entity.c_movement.position[0] + entity.c_movement.speed[0], entity.c_movement.position[1])
                if entity.c_input.up:
                    entity.c_movement.position = (entity.c_movement.position[0], entity.c_movement.position[1] - entity.c_movement.speed[1])
                if entity.c_input.down:
                    entity.c_movement.position = (entity.c_movement.position[0], entity.c_movement.position[1] + entity.c_movement.speed[1])
                    
            if entity.hasattr("c_collision"):
                    entity.c_collision.rect.topleft = entity.c_movement.position
                    

    def collision_system(self):
        screen_rect = self.screen.get_rect()
        for entity in self.entityManger.entities:
            if entity.hasattr("c_collision"):
                if entity.c_collision.rect.right > screen_rect.right or entity.c_collision.rect.left < screen_rect.left:
                    entity.c_movement.speed = (-entity.c_movement.speed[0], entity.c_movement.speed[1])
                elif entity.c_collision.rect.bottom > screen_rect.bottom or entity.c_collision.rect.top < screen_rect.top:
                    entity.c_movement.speed = (entity.c_movement.speed[0], -entity.c_movement.speed[1])
            
            if isinstance(entity, Enemy):
                for other_entity in self.entityManger.entities:
                    if isinstance(other_entity, Bullet) and entity.c_collision.rect.colliderect(other_entity.c_collision.rect):
                        entity.is_alive = False
                        other_entity.is_alive = False
                    elif other_entity != entity and other_entity.hasattr("c_collision"):
                        if entity.c_collision.rect.colliderect(other_entity.c_collision.rect):
                            entity.c_movement.speed = (-entity.c_movement.speed[0], -entity.c_movement.speed[1])

    def render_system(self):
        self.screen.fill(Colors.WHITE)

        for entity in self.entityManger.entities:
            if entity.hasattr("c_render"):
                # entity.c_render.surface.get_rect().topleft = entity.c_render.position
                entity.c_render.surface.fill(entity.c_render.color)
                self.screen.blit(entity.c_render.surface, entity.c_movement.position)
       
        pygame.display.update()

    def create_enemy(self):
        render_component = Components.RenderComponent(pygame.Surface((50, 50)), (50, 50), (randint(0, 255), randint(0, 255), randint(0, 255)))
        entity = Enemy(
            movement_component=Components.MovementComponent((randint(-10, 10), randint(-10, 10)), (randint(0, 800), randint(0, 600))),
            render_component=render_component,
            collision_component=Components.CollisionComponent(render_component.surface.get_rect())
        )
        self.entityManger.addEntity(entity)
    
    def create_player(self):
        render_component = Components.RenderComponent(pygame.Surface((50, 50)), (50, 50), Colors.BLUE)
        entity = Player(
            movement_component=Components.MovementComponent((5, 5), (100, 100)),
            render_component=render_component,
            collision_component=Components.CollisionComponent(render_component.surface.get_rect()),
            input_component=Components.InputComponent()
        )
        self.entityManger.addEntity(entity)

    def create_bullet(self, vec, position):
        render_component = Components.RenderComponent(pygame.Surface((10, 10)), (10, 10), Colors.BLUE)
        bullet = Bullet(
            movement_component=Components.MovementComponent(vec, position),
            render_component=render_component,
            collision_component=Components.CollisionComponent(render_component.surface.get_rect()),
        )
        self.entityManger.addEntity(bullet)