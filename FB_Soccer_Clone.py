import pygame
import math
import random
import colours
pygame.init()
screenSize = (480, 720)
screenRect = pygame.Rect(0,0,screenSize[0],screenSize[1])
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("FB Soccer Clone")

def distBetween(pos1,pos2):
    xDist = math.fabs(pos1[0] - pos2[0])
    yDist = math.fabs(pos1[1] - pos2[1])
    if xDist == 0:
        return yDist
    elif yDist == 0:
        return xDist
    return math.hypot(xDist,yDist)

def drawText(txt, font, colour, rect, align="center"):
    label = font.render(txt, 1, colour)
    if align == "center":
        labelRect = label.get_rect()
        labelX = rect.x + (rect.w - labelRect.w)/2
        labelY = rect.y + (rect.h - labelRect.h)/2
        screen.blit(label, [labelX, labelY])
    elif align == "left":
        screen.blit(label, [rect.x, rect.y])
    elif align == "right":
        labelRect = label.get_rect()
        labelRect.topright = rect.topright
        screen.blit(label, [labelRect.x, labelRect.y])
        
class ball:
    def __init__(self):
        self.r = 60
        self.reset()
        self.img = pygame.image.load("ball.png")
        self.img = pygame.transform.scale(self.img,(2*self.r, 2*self.r))
    def render(self):
        imageCopy = pygame.transform.rotate(self.img, -self.rotate)
        imgRect = imageCopy.get_rect()
        imgRect.center = [self.x, self.y]
        screen.blit(imageCopy, imgRect.topleft)
    def updateBall(self):
        self.velY += self.gravity * 1000 * deltaTime     # Apply Gravity
        self.x += self.velX * deltaTime
        self.y += self.velY * deltaTime

        # Test collision
        if self.y - self.r > screenRect.bottom:     # Bottom of game
            self.reset()
        else:
            if self.x - self.r <= screenRect.left:
                self.x = screenRect.left + self.r
                self.velX *= -1
            elif self.x + self.r >= screenRect.right:
                self.x = screenRect.right - self.r
                self.velX *= -1
        self.rotate += self.velX * deltaTime
    def mouseInSelf(self):
        if distBetween(mousePos, [self.x, self.y]) < self.r:
            return True
        return False
    def jump(self):
        global currentScore
        currentScore += 1
        self.gravity *= 1.01
        self.jumpHeight *= 1.01
        self.velY = self.jumpHeight
        distX = self.x - mousePos[0]
        self.velX = 700 * (distX / self.r)
    def reset(self):
        global currentScore
        global recordScore
        if currentScore > recordScore:
            recordScore = currentScore
            recordSave = open("bestScore.txt", "w")
            recordSave.write(str(recordScore))
            recordSave.close()
        currentScore = 0
        self.x = screenRect.centerx
        self.y = screenRect.bottom - self.r
        self.rotate = 0
        self.velX = 0
        self.velY = 0
        self.jumpHeight = -1000
        self.inGame = False
        self.gravity = 2

recordSave = open("bestScore.txt", "r")
recordScore = int(recordSave.read())
currentScore = 0
mainBall = ball()

font36 = pygame.font.Font(None, 36)
font48 = pygame.font.Font(None, 48)
font128 = pygame.font.Font(None, 128)

clock = pygame.time.Clock()
deltaTime = 0
done = False
 
# -------- Main Program Loop -----------
while not done:
    # --- FPS STUFF --- #
    deltaTime = clock.get_time() / 1000
    clock.tick()
    mousePos = pygame.mouse.get_pos()

    for event in pygame.event.get():    # User did something
        if event.type == pygame.QUIT:   # If user clicked close
            print("User tried to quit")
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mainBall.mouseInSelf():
                mainBall.jump()
                if not mainBall.inGame:
                    mainBall.inGame = True
            
    if mainBall.inGame:
        mainBall.updateBall()

    # Rendering
    screen.fill(colours.LIGHT_PAPER)

    #drawText("FPS: " + str(round(clock.get_fps())), font36, colours.DARK_PAPER, pygame.Rect(0,0,0,0), "left")  # Print FPS in top left

    scoreRect = screenRect.copy()
    scoreRect.h /= 2
    drawText(str(currentScore), font128, colours.DARK_PAPER, scoreRect, "center")

    recordRect = screenRect.inflate(-20, -10)
    drawText("Best: " + str(recordScore), font48, colours.DARK_PAPER, recordRect, "right")

    mainBall.render()
    
    pygame.display.update()
    
pygame.quit()
print("User Quit")
