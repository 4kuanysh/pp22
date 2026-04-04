import pygame

class GameEngine:
    def __init__(self, size, fps):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.is_running = True
        self.player = Player()

    def run(self):
        while self.is_running:
            self.screen.fill((255, 255, 255))

            self.event_system()
            self.movement_system()
            self.render_system()

            pygame.display.update()
            self.clock.tick(self.fps)

    def event_system(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            self.player.handle_input(event)

    def movement_system(self):
        self.player.handle_transfrorm()

    def render_system(self):
        self.player.render(self.screen)            


class Player:
    def __init__(self, ):
        self.c_input = InputComponent()
        self.c_transform = TransformComponent(position=[100, 100], speed=[0, 0])
        self.c_surface = SurfaceComponent(surface=pygame.Surface((50, 50)), color=(255, 0, 0))

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.c_input.left = True
            elif event.key == pygame.K_RIGHT:
                self.c_input.right = True
            elif event.key == pygame.K_UP:
                self.c_input.up = True
            elif event.key == pygame.K_DOWN:
                self.c_input.down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.c_input.left = False
            elif event.key == pygame.K_RIGHT:
                self.c_input.right = False
            elif event.key == pygame.K_UP:
                self.c_input.up = False
            elif event.key == pygame.K_DOWN:
                self.c_input.down = False

    def handle_transfrorm(self):
        if self.c_input.up:
            self.c_transform.position[1] -= self.c_transform.speed[1]
        if self.c_input.down:
            self.c_transform.position[1] += self.c_transform.speed[1]
        if self.c_input.left:
            self.c_transform.position[0] -= self.c_transform.speed[0]
        if self.c_input.right:
            self.c_transform.position[0] += self.c_transform.speed[0]

    def render(self, screen: pygame.Surface):
        screen.blit(self.c_surface.surface, self.c_transform.position)

class InputComponent:
    def __init__(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False

class TransformComponent:
    def __init__(self, position, speed):
        self.position = position
        self.speed = speed

class SurfaceComponent:
    def __init__(self, surface, color):
        self.surface = surface
        self.color = color
        self.surface.fill(color)