import pygame
from Snake import Snake
from Bird import Bird
from sys import exit
pygame.init()

class App:

    def __init__(self):
        self.running = False
        self.clock = None
        self.screen = None
        self.sound = True

    def run(self):
        self.init()
        while self.running:
            self.events()


    def init(self):
        backimg = pygame.image.load("imgsrc/appback.png")
        snakebutton = pygame.image.load("imgsrc/snake.png")
        birdbutton = pygame.image.load("imgsrc/bird.png")
        appIcon = pygame.image.load('imgsrc/icon.png')
        pygame.display.set_caption("samKHa Game Platform")
        pygame.display.set_icon(appIcon)
        self.screen = pygame.display.set_mode((1200, 700))
        self.screen.blit(backimg, (0, 0))
        self.screen.blit(snakebutton, (200, 300))
        self.screen.blit(birdbutton, (700, 300))
        pygame.display.update()
        self.clock = pygame.time.Clock()
        self.running = True
        pygame.mixer.music.load("mp3src/frankschoice.mp3")
        pygame.mixer.music.play(-1, 0.0)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 200 <= pygame.mouse.get_pos()[0] <= 500 and 300 <= pygame.mouse.get_pos()[1] <= 600:
                    countdown = 3
                    last_count = pygame.time.get_ticks()
                    while countdown > 0:
                        backimg = pygame.image.load("imgsrc/appback.png")
                        snakebutton = pygame.image.load("imgsrc/snakeinvert.png")
                        birdbutton = pygame.image.load("imgsrc/bird.png")
                        self.screen.blit(backimg, (0, 0))
                        self.screen.blit(snakebutton, (200, 300))
                        self.screen.blit(birdbutton, (700, 300))
                        font = pygame.font.Font('freesansbold.ttf', 100)
                        text = font.render(str(countdown), True, (255,255,255))
                        self.screen.blit(text, (20, 20))
                        pygame.display.update()
                        count_timer = pygame.time.get_ticks()
                        if count_timer - last_count > 1000:
                            countdown -= 1
                            last_count = count_timer
                    pygame.mixer.music.load("mp3src/comeasyouare.mp3")
                    pygame.mixer.music.play(-1, 0.0)
                    snakeGame = Snake()
                    snakeGame.run()


                if 700 <= pygame.mouse.get_pos()[0] <= 1000 and 300 <= pygame.mouse.get_pos()[1] <= 600:
                    countdown = 3
                    last_count = pygame.time.get_ticks()
                    while countdown > 0:
                        backimg = pygame.image.load("imgsrc/appback.png")
                        snakebutton = pygame.image.load("imgsrc/snake.png")
                        birdbutton = pygame.image.load("imgsrc/birdinvert.png")
                        self.screen.blit(backimg, (0, 0))
                        self.screen.blit(snakebutton, (200, 300))
                        self.screen.blit(birdbutton, (700, 300))
                        font = pygame.font.Font('freesansbold.ttf', 100)
                        text = font.render(str(countdown), True, (255, 255, 255))
                        self.screen.blit(text, (20, 20))
                        pygame.display.update()
                        count_timer = pygame.time.get_ticks()
                        if count_timer - last_count > 1000:
                            countdown -= 1
                            last_count = count_timer
                    pygame.mixer.music.load("mp3src/comeasyouare.mp3")
                    pygame.mixer.music.play(-1, 0.0)
                    birdGame = Bird()
                    birdGame.run()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_m]:
            if self.sound:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()


if __name__ == "__main__":
    app = App()
    app.run()