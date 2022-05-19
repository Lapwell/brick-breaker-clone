import pygame
import time
import sys

pygame.init()

# Colours
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 32, 32
GREEN = 64, 255, 64
BLUE = 0, 128, 255

# Pygame related
WIDTH, HEIGHT = 800, 600
ROOT = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
VEL = 8
clock = pygame.time.Clock()

FONT = pygame.font.Font(None, 24)
win_text = FONT.render('YOU WIN', False, GREEN)
win_screen = win_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
game_over_text = FONT.render('GAME OVER', False, RED)
game_over_screen = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))


brick_list = []
border_list = []


# This class handles the player's platform
class PlayerClass:
    def __init__(self, posx, posy, vel, length, width):
        self.posx = posx
        self.posy = posy
        self.vel = vel
        self.length = length
        self.width = width
        self.rect = pygame.Rect(self.posx, self.posy, self.length, self.width)


# This class handles the ball
class BallClass:
    def __init__(self, posx, posy, x_vel, y_vel, size):
        self.posx = posx
        self.posy = posy
        self.y_vel = y_vel
        self.x_vel = x_vel
        self.size = size
        self.rect = pygame.Rect(self.posx, self.posy, self.size, self.size)

    def update_pos(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel


# This class is for the borders so the ball bounces off the egdes of the screen
class BorderClass:
    def __init__(self, posx, posy, width, height):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.posx, self.posy, self.width, self.height)


# This is the template to spawn the bricks
class BrickClass:
    def __init__(self, posx, posy, size):
        self.posx = posx
        self.posy = posy
        self.size = size
        self.rect = pygame.Rect(self.posx, self.posy, self.size, self.size)


def win():
    while True:
        ROOT.fill(BLACK)
        ROOT.blit(win_text, win_screen)
        pygame.display.update()
        time.sleep(4)
        pygame.quit()
        sys.exit()


def game_over():
    while True:
        ROOT.fill(BLACK)
        ROOT.blit(game_over_text, game_over_screen)
        pygame.display.update()
        time.sleep(4)
        pygame.quit()
        sys.exit()


def check_events():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.rect.x > 8:
        player.rect.x -= player.vel
    if keys[pygame.K_RIGHT] and player.rect.x < WIDTH - player.length - 4:
        player.rect.x += player.vel
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def update_root():
    if ball.rect.y > HEIGHT:
        print('game over')
        game_over()
    if ball.rect.colliderect(player.rect):
        ball.y_vel *= -1
    for item in brick_list:
        if ball.rect.colliderect(item.rect):
            print('brick hit true')
    for item in border_list:
        if ball.rect.colliderect(item.rect):
            if item == border_list[0]:
                ball.x_vel *= -1
                ball.y_vel *= -1
            ball.x_vel *= -1
    ball.update_pos()
    ROOT.fill(BLACK)
    pygame.draw.circle(ROOT, BLUE, (ball.rect[0], ball.rect[1]), ball.size)
    pygame.draw.rect(ROOT, WHITE, player.rect)
    pygame.display.update()


def fps_counter():
    count = str(int(clock.get_fps()))
    fps_txt = FONT.render(count, True, WHITE)
    ROOT.blit(fps_txt, (fps_txt.get_width() - fps_txt.get_width()//2, fps_txt.get_height() - fps_txt.get_height()//2))


def main():
    check_events()
    update_root()
    clock.tick(FPS)


if __name__ == '__main__':
    ball = BallClass(WIDTH // 2, HEIGHT // 2, 4, 4, 15)
    player = PlayerClass(WIDTH - WIDTH / 2, HEIGHT - 50, VEL, 164, 12)
    top_border = BorderClass(0, 0, WIDTH, 20)
    right_border = BorderClass(WIDTH, 0, 20, HEIGHT)
    left_border = BorderClass(0, 0, 20, HEIGHT)
    border_list = [top_border, right_border, left_border]
    while True:
        main()
