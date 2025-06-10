import pygame

class Text(pygame.sprite.Sprite):
    def __init__(self, text, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.font = pygame.font.Font("FiraCode-Regular.ttf", 16)
        self.text = self.font.render(text, True, "white")
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (x, y)

        self.x = x
        self.y = y

    def update(self, text):
        self.text = self.font.render(text, True, "white")
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x, self.y)
        
    def draw(self, screen):
        screen.blit(self.text, self.text_rect)

    
    