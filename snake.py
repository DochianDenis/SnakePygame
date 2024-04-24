import random
import time
import pygame

def show_score(choice, color, font, size, score, ecran):
    score_font=pygame.font.SysFont(font, size)
    score_surface=score_font.render(str(score), True, color)
    score_rect=score_surface.get_rect()
    ecran.blit(score_surface, score_rect)

def game_over(score, color, keystroke, window_x, window_y, ecran):
    game_over_font = pygame.font.SysFont('times new roman', 22)
    game_over_surface = game_over_font.render('Score - ' +str(score)+ '   KeyStrokes - ' + 
    str(keystroke), True, color)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop=(window_x/2, window_y/2-15)
    ecran.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_r:
                    Play_Game()

def Play_Game():                
    snake_speed = 20
    window_x = 500
    window_y = 500
    keystroke = 0

    white = pygame.Color(255, 255, 255)
    black = pygame.Color(0, 0, 0)
    green = pygame.Color(0, 255, 0)

    pygame.init()
    ecran = pygame.display.set_mode((window_x, window_y))
    pygame.display.set_caption('Snake')
    fps = pygame.time.Clock()

    snake_position = [50, 120]
    snake_body = [           
        [50, 120],
        [40, 120],
        [30, 120],
        [20, 120]
    ]
    direction = 'RIGHT' 
    change_to = direction
    fruit_position = [
        random.randrange(1, (window_x//10)) * 10,
        random.randrange(1, (window_y//10)) * 10
    ]
    fruit_spawn = True
    score = 0    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    time.sleep(5)
                if event.key == pygame.K_r:
                    Play_Game()
                if event.key == pygame.K_2:
                    snake_speed += 2
                if event.key == pygame.K_1 and snake_speed >= 3:
                    snake_speed -= 2
                if event.key == pygame.K_UP:
                    change_to ='UP'
                    keystroke += 1
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                    keystroke += 1
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                    keystroke += 1
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                    keystroke += 1
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        snake_body.insert(0, list(snake_position))

        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 1
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [
                random.randrange(10, (window_x // 10)) * 10,
                random.randrange(10, (window_y // 10)) * 10
                ]
        fruit_spawn = True
        ecran.fill(black)

        if (snake_position[0] < 0 or snake_position[0] == window_x  
        or snake_position[1] < 0 or snake_position[1] == window_y):
            game_over(score, white, keystroke, window_x, window_y, ecran)

        for pos in snake_body:
            pygame.draw.rect(ecran, green, [pos[0], pos[1], 10, 10])
    
        pygame.draw.rect(ecran, white, [fruit_position[0], fruit_position[1], 10, 10])

        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over(score, white, keystroke, window_x, window_y, ecran)
    
        show_score(1, white, 'times new roman', 30, score, ecran)

        pygame.display.update()
        fps.tick(snake_speed)

Play_Game()
