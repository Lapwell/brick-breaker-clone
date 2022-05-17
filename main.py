import pygame
import sys

pygame.init()

# Colours
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 64, 64, 255
GREEN = 0, 128, 255

# Pygame related
WIDTH, HEIGHT = 800, 600
ROOT = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 30
FONT = pygame.font.Font(None, 24)
clock = pygame.time.Clock()


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
    def __init__(self, posx, posy, vel, size):
        self.posx = posx
        self.posy = posy
        self.vel = vel
        self.size = size
        self.rect = pygame.Rect(self.posx, self.posy, self.size, self.size)

    def update_pos(self):
        self.rect.x += self.vel
        self.rect.y += self.vel


# This is the template to spawn the bricks
class BrickClass:
    def __init__(self, posx, posy, size):
        self.posx = posx
        self.posy = posy
        self.size = size
        self.rect = pygame.Rect(self.posx, self.posy, self.size, self.size)


def check_events():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.rect.x > 4:
        player.rect.x -= player.vel
    if keys[pygame.K_RIGHT] and player.rect.x < WIDTH - player.length - 4:
        player.rect.x += player.vel
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def update_root():
    if ball.rect.colliderect(player.rect):
        ball.vel *= -1
    ball.update_pos()
    ROOT.fill(BLACK)
    pygame.draw.circle(ROOT, GREEN, (ball.rect[0], ball.rect[1]), ball.size)
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
    ball = BallClass(WIDTH // 2, HEIGHT // 2, 4, 15)
    player = PlayerClass(WIDTH - WIDTH / 2, HEIGHT - 50, 4, 164, 12)
    while True:
        main()
