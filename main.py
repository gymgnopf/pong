import pygame
from constants import *
from paddle import Paddle
from ball import Ball
from text import Text

def main():
    pygame.init()
    
    #screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong")
    surface = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))

    # Groups 
    draw_group = pygame.sprite.Group()
    update_group = pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()
    text_group = pygame.sprite.Group()

    # Containers
    Paddle.containers = (paddle_group, draw_group, update_group)
    Ball.containers = (draw_group, update_group)
    Text.containers = (draw_group, text_group)

    # Frames / Times
    clock = pygame.time.Clock()
    dt = 0

    # Game objects
    player_paddle = Paddle(10, VIRTUAL_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    cpu_paddle = Paddle(VIRTUAL_WIDTH - 10, VIRTUAL_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(VIRTUAL_WIDTH / 2 - 2, VIRTUAL_HEIGHT / 2 - 2, BALL_WIDTH, BALL_HEIGHT) 
    score_text = Text("Pong", VIRTUAL_WIDTH / 2, 20)

    # Game state
    game_state = "start"
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_SPACE:
                    if game_state == "start":
                        game_state = "play"
                    else:
                        game_state = "start"
                        ball.reset()

        surface.fill((0, 0, 0))

        for obj in update_group:
            obj.update(dt, game_state)
        
        for obj in text_group:
            obj.update("Test")
        
        for obj in paddle_group: 
            if obj.collides(ball):
                ball.bounceOff(obj)
 
        for obj in draw_group:
            obj.draw(surface)

        scaled_surface = pygame.transform.scale(surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        # pygame.Surface.blit(scaled_surface,screen)
        screen.blit(scaled_surface, (0, 0))

        pygame.display.flip()
        dt = clock.tick(FPS) / 1000



if __name__ == "__main__":
    main()

