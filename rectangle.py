import pygame

# Base class for game objects
class Rectangle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.obj = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            "white",
            self.obj
        )

    def update(self, dt, game_state):
        # sub-classes must override
        pass

    def collides(self, other):
        return self.obj.colliderect(other.obj)