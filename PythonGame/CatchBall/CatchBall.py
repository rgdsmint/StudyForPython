import pygame as pg
import random
import time
pg.init()
game_window = pg.display.set_mode((600, 500))
pg.display.set_caption('接球')
window_color = (0, 0, 255)
ball_color = (255, 165, 0)
rect_color = (255, 0, 0)
ball_x = random.randint(20, 580)
ball_y = 20
move_x = 1
move_y = 1
score = 0
point = 1
font = pg.font.SysFont('SimHei', 20)
interval = 0.005
conut = 0
grade = 1
state = False
while True:
    game_window.fill(window_color)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            pressed_array = pg.mouse.get_pressed()
            for index in range(len(pressed_array)):
                if pressed_array[index]:
                    if index == 2:
                        while not state:
                            for event in pg.event.get():
                                if event.type == pg.MOUSEBUTTONDOWN:
                                    pressed_array = pg.mouse.get_pressed()
                                    for index in range(len(pressed_array)):
                                        if pressed_array[index]:
                                            if index == 2:
                                                state = not state
                        state = not state
    mouse_x, mouse_y = pg.mouse.get_pos()
    pg.draw.circle(game_window, ball_color, (ball_x, ball_y), 20)
    pg.draw.rect(game_window, rect_color, (mouse_x, 490, 100, 10))
    text_str = '得分: ' + str(score) + '||' + '等级: ' + str(grade)
    text = font.render(text_str, False, (255, 255, 255))
    game_window.blit(text, (420, 30))
    ball_x += move_x
    ball_y += move_y
    if ball_x <= 20 or ball_x >= 580:
        move_x = -move_x
    if ball_y <= 20:
        move_y = -move_y
    elif mouse_x - 20 < ball_x < mouse_x + 100 + 20 and ball_y >= 470:
        move_y = -move_y
        score += point
        conut += 1
        if conut % 5 == 0:
            grade += 1
            point += point
            if move_x > 0:
                move_x += 1
            else:
                move_x -= 1
            move_y -= 1
        interval += 0.00005
    elif ball_y >= 480 and (ball_x <= mouse_x - 20
                            or ball_x >= mouse_x + 100 + 20):
        break
    pg.display.update()
    time.sleep(interval)