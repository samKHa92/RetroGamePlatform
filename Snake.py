import random
import pygame
from sys import exit

class Snake():
    def __init__(self):
        self.color = (255,0,0)
        self.difficultySet = False
        self.running = False
        self.started = False
        self.finished = False
        self.scoreboardChanged = False
        self.explosionDisplayed = False
        self.sound = True
        self.screen = None
        self.clock = None
        self.radius = 20
        self.speed = 3
        self.points = 0
        self.criticalPointsCount = 0
        self.body = [[180,330,"R",0],[160, 350,"R",0],[120, 350,"R",0],[80, 350,"R",0],[40, 350,"R",0]]
        self.food = [780, 540, 5, 1]
        self.criticalPoints = []
        self.scoreboard = []



    def run(self):
        self.initWithQuestion()
        self.readScoreboard()
        while self.running:
            self.events()
            if self.started:
                self.checkBackButton()
                self.update()
                self.render()
            if self.finished:
                if not self.explosionDisplayed:
                    self.displayExplosion()
                    self.explosionDisplayed = True
                if not self.scoreboardChanged:
                    self.changeScoreboard()
                    self.readScoreboard()
                    self.scoreboardChanged = True
                self.displayEndScreen()
                pygame.display.update()
                self.endScreenButtonsCheck()

    def readScoreboard(self):
        f = open("snakescoreboard.txt", "r")
        line = f.read()
        self.scoreboard = []
        for x in line.split(" "):
            self.scoreboard.append(x)

    def initWithQuestion(self):
        snakebackimg = pygame.image.load("imgsrc/snakeback.png")
        difficultybuttons = pygame.image.load("imgsrc/difficulty.png")
        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode((1200, 700))
        self.screen.blit(snakebackimg, (0, 0))
        self.screen.blit(difficultybuttons, (0, 0))
        pygame.display.update()
        self.clock = pygame.time.Clock()
        self.running = True

    def init(self):
        snakebackimg = pygame.image.load("imgsrc/snakeback.png")
        snakehead = pygame.image.load("imgsrc/snakeheadright.png")
        firstfood = pygame.image.load("imgsrc/food1.png")
        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode((1200, 700))
        self.screen.blit(snakebackimg, (0, 0))
        pygame.draw.circle(self.screen, self.color, (40, 350), 20)
        pygame.draw.circle(self.screen, self.color, (80, 350), 20)
        pygame.draw.circle(self.screen, self.color, (120, 350), 20)
        pygame.draw.circle(self.screen, self.color, (160, 350), 20)
        self.screen.blit(snakehead, (180, 330))
        self.screen.blit(firstfood, (780, 540))
        pygame.display.update()
        self.clock = pygame.time.Clock()
        self.running = True

    def checkBackButton(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0 <= pygame.mouse.get_pos()[0] <= 50 and 0 <= pygame.mouse.get_pos()[1] <= 20:
                    self.returnMainMenu()
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                self.running = False
            if not self.difficultySet and event.type == pygame.MOUSEBUTTONDOWN:
                if 95 <= pygame.mouse.get_pos()[0] <= 345 and 225 <= pygame.mouse.get_pos()[1] <= 475:
                    countdown = 3
                    last_count = pygame.time.get_ticks()
                    while countdown > 0:
                        backimg = pygame.image.load("imgsrc/snakeback.png")
                        difficultybuttons = pygame.image.load("imgsrc/difficulty.png")
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
                    self.speed = 5
                    self.difficultySet = True
                    self.init()
                elif 475 <= pygame.mouse.get_pos()[0] <= 725 and 225 <= pygame.mouse.get_pos()[1] <= 475:
                    countdown = 3
                    last_count = pygame.time.get_ticks()
                    while countdown > 0:
                        backimg = pygame.image.load("imgsrc/snakeback.png")
                        difficultybuttons = pygame.image.load("imgsrc/difficulty.png")
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
                    self.speed = 10
                    self.difficultySet = True
                    self.init()
                elif 875 <= pygame.mouse.get_pos()[0] <= 1125 and 225 <= pygame.mouse.get_pos()[1] <= 475:
                    countdown = 3
                    last_count = pygame.time.get_ticks()
                    while countdown > 0:
                        backimg = pygame.image.load("imgsrc/snakeback.png")
                        difficultybuttons = pygame.image.load("imgsrc/difficulty.png")
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
                    self.speed = 20
                    self.difficultySet = True
                    self.init()
                elif 0 <= pygame.mouse.get_pos()[0] <= 50 and 0 <= pygame.mouse.get_pos()[1] <= 20:
                    self.returnMainMenu()
        if self.difficultySet:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_m]:
                if self.sound:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            if keys[pygame.K_SPACE] and not self.started:
                self.started = True
                self.start()
            if self.started:
                if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.body[0][2] != "L":
                    self.body[0][2] = "R"
                    self.criticalPointsCount += 1
                    criticalPoint = [self.body[0][0] + self.radius, self.body[0][1] + self.radius, "R", 0,
                                     len(self.body) - 1, self.criticalPointsCount]
                    self.criticalPoints.append(criticalPoint)
                elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.body[0][2] != "R":
                    self.body[0][2] = "L"
                    self.criticalPointsCount += 1
                    criticalPoint = [self.body[0][0] + self.radius, self.body[0][1] + self.radius, "L", 0,
                                     len(self.body) - 1, self.criticalPointsCount]
                    self.criticalPoints.append(criticalPoint)
                elif (keys[pygame.K_w] or keys[pygame.K_UP]) and self.body[0][2] != "D":
                    self.body[0][2] = "U"
                    self.criticalPointsCount += 1
                    criticalPoint = [self.body[0][0] + self.radius, self.body[0][1] + self.radius, "U", 0,
                                     len(self.body) - 1, self.criticalPointsCount]
                    self.criticalPoints.append(criticalPoint)
                elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.body[0][2] != "U":
                    self.body[0][2] = "D"
                    self.criticalPointsCount += 1
                    criticalPoint = [self.body[0][0] + self.radius, self.body[0][1] + self.radius, "D", 0,
                                     len(self.body) - 1, self.criticalPointsCount]
                    self.criticalPoints.append(criticalPoint)


    def eatFood(self):
        headMidX = self.body[0][0] + self.radius
        headMidY = self.body[0][1] + self.radius
        foodMidX = self.food[0] + self.radius
        foodMidY = self.food[1] + self.radius
        headDir = self.body[0][2]
        if -35 <= headMidX - foodMidX <= 35 and -35 <= headMidY - foodMidY <= 35 and self.food[2] == len(self.body):
            self.createFood()
            if self.food[3] != 1:
                self.food[2] += 1
                newBorn = [0,0,"X",0]
                lastChild = self.body[len(self.body)-1]
                if lastChild[2] == "R":
                    newBorn[0] = lastChild[0] - 40
                    newBorn[1] = lastChild[1]
                    newBorn[2] = "R"
                    newBorn[3] = lastChild[3]
                elif lastChild[2] == "L":
                    newBorn[0] = lastChild[0] + 40
                    newBorn[1] = lastChild[1]
                    newBorn[2] = "L"
                    newBorn[3] = lastChild[3]
                elif lastChild[2] == "U":
                    newBorn[0] = lastChild[0]
                    newBorn[1] = lastChild[1] + 40
                    newBorn[2] = "U"
                    newBorn[3] = lastChild[3]
                elif lastChild[2] == "D":
                    newBorn[0] = lastChild[0]
                    newBorn[1] = lastChild[1] - 40
                    newBorn[2] = "D"
                    newBorn[3] = lastChild[3]
                self.points += self.speed
                self.body.append(newBorn)
            else:
                self.points += (3 * self.speed)
            return True
        return False


    def createFood(self):
        if self.food[3] == 1:
            food = pygame.image.load("imgsrc/food2.png")
            self.food[3] = 2
        elif self.food[3] == 2:
            food = pygame.image.load("imgsrc/food3.png")
            self.food[3] = 3
        elif self.food[3] == 3:
            food = pygame.image.load("imgsrc/superfood.png")
            self.food[3] = 4
        else:
            food = pygame.image.load("imgsrc/food1.png")
            self.food[3] = 1
        while True:
            checked = True
            x = random.randint(60, 1140)
            y = random.randint(120, 640)
            for e in self.body[1:]:
                if -40 <= e[0] - x <= 40 and -40 <= e[1] - y <= 40:
                    checked = False
            if checked:
                break
        self.food[0] = x
        self.food[1] = y

    def crashes(self):
        headMidX = self.body[0][0] + self.radius
        headMidY = self.body[0][1] + self.radius
        if headMidY < 100 or headMidY > 664 or headMidX < 36 or headMidX > 1164:
            return True
        for e in self.body[1:]:
            if -10 <= e[0]-headMidX <= 10 and -10 <= e[1] - headMidY <= 10:
                return True
        return False


    def foodImage(self):
        if self.food[3] == 1:
            food = pygame.image.load("imgsrc/food1.png")
        elif self.food[3] == 2:
            food = pygame.image.load("imgsrc/food2.png")
        elif self.food[3] == 3:
            food = pygame.image.load("imgsrc/food3.png")
        else:
            food = pygame.image.load("imgsrc/superfood.png")
        return food

    def start(self):
        for i in self.body:
            i[0] += self.speed

    def update(self):
        if self.crashes():
            self.finished = True
            self.started = False
        if self.eatFood():
            for e in self.criticalPoints:
                e[4] += 1

        if len(self.criticalPoints) > 0:
            for p in self.criticalPoints:
                for e in self.body[1:]:
                    if e[0] == p[0] and e[1] == p[1] and p[5] - 1 == e[3]:
                        e[2] = p[2]
                        p[3] += 1
                        e[3] += 1
                templst = list(filter(lambda x: x[3] < x[4], self.criticalPoints))
                self.criticalPoints = templst
        for e in self.body:
            if e[2] == "R":
                e[0] += self.speed
            if e[2] == "L":
                e[0] -= self.speed
            if e[2] == "U":
                e[1] -= self.speed
            if e[2] == "D":
                e[1] += self.speed
    def render(self):
        pygame.display.flip()
        snakebackimg = pygame.image.load("imgsrc/snakeback.png")
        self.screen.blit(snakebackimg, (0, 0))
        if self.body[0][2] == "R":
            snakehead = pygame.image.load("imgsrc/snakeheadright.png")
        else:
            snakehead = pygame.image.load("imgsrc/snakeheadleft.png")
        self.screen.blit(snakehead, (self.body[0][0], self.body[0][1]))
        self.screen.blit(self.foodImage(), (self.food[0], self.food[1]))
        font = pygame.font.Font('freesansbold.ttf', 35)
        points = font.render(str(self.points), True, (255, 255, 255))
        highscore = font.render(str(self.scoreboard[0]), True, (255, 255, 255))
        self.screen.blit(points, (1000, 25))
        self.screen.blit(highscore, (670, 25))
        for e in self.body[1:]:
            pygame.draw.circle(self.screen, self.color, (e[0], e[1]), 20)
        self.clock.tick(60)

    def displayExplosion(self):
        headMidX = self.body[0][0] + self.radius
        headMidY = self.body[0][1] + self.radius
        images = []
        for num in range(1, 6):
            img = pygame.image.load(f"imgsrc/exp{num}.png")
            img = pygame.transform.scale(img, (35, 35))
            # add the image to the list
            images.append(img)
        explosion_fx = pygame.mixer.Sound("mp3src/explosion.wav")
        explosion_fx.set_volume(0.25)

        countdown = 15
        last_count = pygame.time.get_ticks()
        while countdown > 0:
            self.screen.blit(images[(5 - countdown) % 5], (headMidX-self.radius, headMidY-self.radius))
            explosion_fx.play()
            pygame.display.update()
            count_timer = pygame.time.get_ticks()
            if count_timer - last_count > 100:
                countdown -= 1
                last_count = count_timer

    def changeScoreboard(self):
        f = open("snakescoreboard.txt", "w")
        stri = ""
        self.scoreboard.append(self.points)
        lst = []
        for x in self.scoreboard:
            lst.append(int(x))
        lst.sort()
        lst.reverse()
        for x in lst[:len(self.scoreboard) - 1]:
            stri += str(str(x) + " ")
        stri = stri[:len(stri) - 1]
        f.write(stri)
        f.close()

    def displayEndScreen(self):
        endscreen = pygame.image.load("imgsrc/snakeendscreen.png")
        self.screen.blit(endscreen, (0, 0))
        font = pygame.font.Font('freesansbold.ttf', 50)
        alreadyFound = False
        y = 260
        for x in self.scoreboard:
            if self.points == int(x) and not alreadyFound:
                score = font.render(str(x), True, (255, 0, 0))
                alreadyFound = True
            else:
                score = font.render(str(x), True, (0, 0, 0))
            self.screen.blit(score, (120, y))
            y += 40


    def endScreenButtonsCheck(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 785 <= pygame.mouse.get_pos()[0] <= 1080 and 350 <= pygame.mouse.get_pos()[1] <= 463:
                    countdown = 3
                    last_count = pygame.time.get_ticks()
                    while countdown > 0:
                        font = pygame.font.Font('freesansbold.ttf', 100)
                        text = font.render(str(countdown), True, (255, 255, 255))
                        self.displayEndScreen()
                        self.screen.blit(text, (20, 20))
                        pygame.display.update()
                        count_timer = pygame.time.get_ticks()
                        if count_timer - last_count > 1000:
                            countdown -= 1
                            last_count = count_timer
                    snake = Snake()
                    snake.run()
                elif 785 <= pygame.mouse.get_pos()[0] <= 1080 and 500 <= pygame.mouse.get_pos()[1] <= 620:
                    self.returnMainMenu()

    def returnMainMenu(self):
        app = App()
        app.run()

from App import App