# TODO: import pygame
import pygame as pg
import time

pg.init()

black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
# TODO: Create a Display screen
dis_width = 800
dis_height = 600
dis = pg.display.set_mode((dis_width, dis_height))
pg.display.set_caption("Kris-ore Snake Game")

game_over = False

x1 = dis_width / 2
y1 = dis_height / 2

snake_block = 10

x1_change = 0
y1_change = 0

clock = pg.time.Clock()
snake_speed = 30

font_style = pg.font.SysFont(None, 50)

# TODO: get message "You Lost"
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2, dis_height / 2])


# TODO: get user key's Input
while not game_over:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pg.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pg.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pg.K_DOWN:
                y1_change = snake_block
                x1_change = 0
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pg.draw.rect(dis, black, [x1, y1, snake_block, snake_block])

    pg.display.update()

    clock.tick(snake_speed)

message("You lost", red)
pg.display.update()
time.sleep(2)

pg.quit()
quit()
