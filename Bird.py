import pygame
import random
from sys import exit

class Bird:
    def __init__(self):
        self.color = (255, 0, 0)
        self.fighterchosen = False
        self.running = False
        self.started = False
        self.finished = False
        self.gravity = True
        self.screen = None
        self.clock = None
        self.sound = True
        self.fighter = None
        self.jumpstartpos = None
        self.fallstartpos = 400
        self.position = 400
        self.walls = []
    def run(self):
        self.initWithQuestion()
        while self.running:
            self.events()
            if self.fighterchosen:
                self.update()
                self.render()
                pygame.display.update()
        if self.finished:
            self.displayendscreen()
            self.displaycounter()

    def initWithQuestion(self):
        birdbackimg = pygame.image.load("imgsrc/birdback.png")
        birdoptions = pygame.image.load("imgsrc/choosefighter.png")
        pygame.display.set_caption("Flappy Bird PLS")
        self.createWall()
        self.screen = pygame.display.set_mode((1200, 700))
        self.screen.blit(birdbackimg, (0, 0))
        self.screen.blit(birdoptions, (0, 0))
        pygame.display.update()
        self.clock = pygame.time.Clock()
        self.running = True

    def init(self):
        birdbackimg = pygame.image.load("imgsrc/birdback.png")
        pygame.display.set_caption("Flappy Bird")
        self.screen = pygame.display.set_mode((1200, 700))
        self.screen.blit(birdbackimg, (0, 0))
        self.screen.blit(self.fighter, (300,400))
        pygame.display.update()
        self.clock = pygame.time.Clock()
        self.running = True

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                exit()
            if not self.fighterchosen and event.type == pygame.MOUSEBUTTONDOWN:
                if 90 <= pygame.mouse.get_pos()[0] <= 370 and 325 <= pygame.mouse.get_pos()[1] <= 600:
                    countdown = 3
                    last_count = pygame.time.get_ticks()
                    while countdown > 0:
                        backimg = pygame.image.load("imgsrc/birdback.png")
                        difficultybuttons = pygame.image.load("imgsrc/choosefighter.png")
                        self.screen.blit(backimg, (0, 0))
                        self.screen.blit(difficultybuttons, (0, 0))
                        font = pygame.font.Font('freesansbold.ttf', 100)
                        text = font.render(str(countdown), True, (255, 255, 255))
                        self.screen.blit(text, (20, 20))
                        pygame.display.update()
                        count_timer = pygame.time.get_ticks()
                        if count_timer - last_count > 1000:
                            countdown -= 1
                            last_count = count_timer
                    self.fighter = pygame.image.load("imgsrc/irakla.png")
                    self.fighterchosen = True
                    self.init()
                elif 460 <= pygame.mouse.get_pos()[0] <= 740 and 325 <= pygame.mouse.get_pos()[1] <= 600:
                    countdown = 3
                    last_count = pygame.time.get_ticks()
                    while countdown > 0:
                        backimg = pygame.image.load("imgsrc/birdback.png")
                        difficultybuttons = pygame.image.load("imgsrc/choosefighter.png")
                        self.screen.blit(backimg, (0, 0))
                        self.screen.blit(difficultybuttons, (0, 0))
                        font = pygame.font.Font('freesansbold.ttf', 100)
                        text = font.render(str(countdown), True, (255, 255, 255))
                        self.screen.blit(text, (20, 20))
                        pygame.display.update()
                        count_timer = pygame.time.get_ticks()
                        if count_timer - last_count > 1000:
                            countdown -= 1
                            last_count = count_timer
                    self.fighter = pygame.image.load("imgsrc/nugsona.png")
                    self.fighterchosen = True
                    self.init()
                elif 830 <= pygame.mouse.get_pos()[0] <= 1110 and 325 <= pygame.mouse.get_pos()[1] <= 600:
                    countdown = 3
                    last_count = pygame.time.get_ticks()
                    while countdown > 0:
                        backimg = pygame.image.load("imgsrc/birdback.png")
                        difficultybuttons = pygame.image.load("imgsrc/choosefighter.png")
                        self.screen.blit(backimg, (0, 0))
                        self.screen.blit(difficultybuttons, (0, 0))
                        font = pygame.font.Font('freesansbold.ttf', 100)
                        text = font.render(str(countdown), True, (255, 255, 255))
                        self.screen.blit(text, (20, 20))
                        pygame.display.update()
                        count_timer = pygame.time.get_ticks()
                        if count_timer - last_count > 1000:
                            countdown -= 1
                            last_count = count_timer
                    self.fighter = pygame.image.load("imgsrc/suxuna.png")
                    self.fighterchosen = True
                    self.init()
        if self.fighterchosen:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_m]:
                if self.sound:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            if keys[pygame.K_SPACE]:
                self.jumpstartpos = self.position
                self.jump()

    def jump(self):
        self.gravity = False
        countdown = 20
        last_count = pygame.time.get_ticks()
        while countdown > 0:
            if self.position >= self.jumpstartpos - 25:
                self.position -= 9
                self.movewalls()
                self.render()
                self.events()
            if self.position >= self.jumpstartpos - 50:
                self.position -= 5
                self.movewalls()
                self.render()
                self.events()
            if self.position >= self.jumpstartpos - 70:
                self.position -= 2
                self.movewalls()
                self.render()
                self.events()
            else:
                self.gravity = True
                self.fallstartpos = self.position
                break
            count_timer = pygame.time.get_ticks()
            if count_timer - last_count > 25:
                countdown -= 1
                last_count = count_timer

    def createWall(self):
        height1 = random.randint(50, 310)
        height2 = 700 - 95 - 250 - height1
        self.walls.append([[1300,95,100,height1],[1300,700 - height2, 100, height2]])

    def removeWall(self):
        self.walls = self.walls[1:]

    def movewalls(self):
        for x in self.walls:
            x[0][0] -= 3
            x[1][0] -= 3

    def displayendscreen(self):
        img = pygame.image.load("imgsrc/died.png")
        self.screen.blit(img, (0,0))
        pygame.display.update()

    def displaycounter(self):
        countdown = 3
        last_count = pygame.time.get_ticks()
        while countdown > 0:
            self.render()
            img = pygame.image.load("imgsrc/died.png")
            self.screen.blit(img, (0, 0))
            font = pygame.font.Font('freesansbold.ttf', 100)
            text = font.render(str(countdown), True, (255, 255, 255))
            self.screen.blit(text, (20, 20))
            pygame.display.update()
            count_timer = pygame.time.get_ticks()
            if count_timer - last_count > 1000:
                countdown -= 1
                last_count = count_timer
        self.returnMainMenu()

    def update(self):
        self.events()
        if self.checkColides():
            self.running = False
            self.finished = True
        if self.gravity:
            if self.fallstartpos >= self.position - 3:
                self.position += 0.2
            if self.fallstartpos >= self.position - 10:
                self.position += 1
            if self.fallstartpos >= self.position - 25:
                self.position += 4
            else:
                self.position += 7
        if self.walls[0][0][0] <= -100:
            self.removeWall()
            if self.walls[len(self.walls) - 1][0][0] <= 700 and len(self.walls) < 4:
                self.createWall()
        if self.walls[len(self.walls) - 1][0][0] <= 700 and len(self.walls) < 4:
            self.createWall()
        self.movewalls()

    def listToTuple(self, lst):
        return (lst[0],lst[1],lst[2],lst[3])

    def checkColides(self):
        left = 300
        right = 420
        up = self.position
        down = self.position + 110
        for x in self.walls:
            if x[0][0] >= left and x[0][0] <= right and x[0][1] + x[0][3] >= up:
                return True
            if x[1][0] >= left and x[1][0] <= right and x[1][1] <= down:
                return True
        return False



    def render(self):
        pygame.display.flip()
        birdbackimg = pygame.image.load("imgsrc/birdback.png")
        self.screen.blit(birdbackimg, (0, 0))
        for x in self.walls:
            pygame.draw.rect(self.screen, (255, 0, 0), self.listToTuple(x[0]))
            pygame.draw.rect(self.screen, (255, 0, 0), self.listToTuple(x[1]))
        if self.fighterchosen:
            self.screen.blit(self.fighter, (300, self.position))


    def returnMainMenu(self):
        app = Snake()
        app.returnMainMenu()

from Snake import Snake

