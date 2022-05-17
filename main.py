import pygame
import sys

pygame.init()

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 64, 64, 255

WIDTH, HEIGHT = 800, 600
ROOT = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
FONT = pygame.font.Font(None, 24)
clock = pygame.time.Clock()


class BallClass:
    def __init__(self, posx, posy, vel, size):
        self.posx = posx
        self.posy = posy
        self.vel = vel
        self.size = size
        self.rect = pygame.Rect(self.posx, self.posy, self.size, self.size)


class BrickClass:
    def __init__(self, posx, posy, size):
        self.posx = posx
        self.posy = posy
        self.size = size
        self.rect = pygame.Rect(self.posx, self.posy, self.size, self.size)


def update_root():
    pygame.draw.circle(ROOT, WHITE, (ball.rect[0], ball.rect[1]), ball.size)
    pygame.display.update()


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


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
    while True:
        main()
