import pygame
import time
import random
import math
import os
from pygame import mixer


pygame.init()

score = 0
font = pygame.font.SysFont(None,38)
textX = 10
textY = 10

def show(x,y):
    scorevalue=font.render("your score is: "+ str(score), True, (255,255,255))
    screen.blit(scorevalue,(x,y))

# here i set my music
mixer.music.load('sounds/background.wav')
mixer.music.play(-1) # -1 for a loop
# here i define the size of the screen (When changing the size, the speed of the object should also be changed)
screen = pygame.display.set_mode((1000, 800))
# here i set the title and the icon
pygame.display.set_caption("vegan meal")
icon = pygame.image.load('pictures/icon.png')
pygame.display.set_icon(icon)
image= pygame.image.load('pictures/Veggie.png')
VeggieX = 450
VeggieY = 700
# here i put the pictures of the enemy
newX = 0
newY = 0
#meat
meatpic = pygame.image.load('pictures/meat.png')
meatX = random.randint(10,900)
meatY = random.randint(10,300)
meatNewX = 0.3
#diary
Diarypic = pygame.image.load('pictures/Diary.png')
DiaryX = random.randint(10,900)
DiaryY = random.randint(10,300)
DiaryNewX = 0.3
#egg
eggpic = pygame.image.load('pictures/egg.png')
eggX = random.randint(10,900)
eggY = random.randint(10,300)
eggNewX = 0.3
# my Backup will be animals objects ready to help
backuppic = []
backupx = []
backupy = []
backupnew = 1 #the speed of them
backuppic.append(pygame.image.load('pictures/bee.png'))
backuppic.append(pygame.image.load('pictures/bird.png'))
backuppic.append(pygame.image.load('pictures/cow.png'))
backuppic.append(pygame.image.load('pictures/hen.png'))
backuppic.append(pygame.image.load('pictures/owl.png'))

# the backup should take random positions
for i in range(0,5):
    backupx.append(random.randint(10, 900))
    backupy.append(random.randint(1000, 5000))

# my Background pic
Background = pygame.image.load('pictures/Tisch.jpg')
#9ertassa
kertassa = pygame.image.load('pictures/9ertassa.png')
kertassaY = VeggieY
kertassaX = 0
kerrtassaNew = 10 #the speed of the orange
kertassastatu = "hey" # hey means ready to be fired

# i fire my orange and change hey to ho
def fire(x,y):
    global kertassastatu
    kertassastatu = "ho"
    screen.blit(kertassa,(x+10,y-20)) # the x and y are the current veggie location

# checking whether there will be a colision
def boom(x1,y1,x2,y2):
    boom=math.sqrt(((x2-x1)**2)+((y2-y1)**2)) # Pythagorean theorem compute the distance between two points
    if boom<60:
        return True
    else:
        return False

# functions that dram the backup
def render_meat(X,Y):
    screen.blit(meatpic, (X,Y))

def render_diary(X,Y):
    screen.blit(Diarypic, (X,Y))

def render_egg(X,Y):
    screen.blit(eggpic, (X,Y))

# the function making backup appear in the screen
def render_backup(i,X,Y):
    if backupy[i]<1200 and backupy[i]>-100: # this coordination makes sure they are in the screen
        screen.blit(backuppic[i], (backupx[i],backupy[i]))

# this function draws the veggie war space
def render_veggie(VeggieX,VeggieY):
    screen.blit(image, (VeggieX, VeggieY))
    
# Text parameters
font=pygame.font.SysFont(None, 90)
color=(255,255,255)

#this function will be used to show the text
def msg(msg, color):
    text = font.render(msg, True, color)
    text_width, text_height = font.size(msg)  # getting the size of the text
    # putting the text in the center
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text, text_rect)

run = True #while run is true, the game goes on

while run:
    for event in pygame.event.get(): #checking what the user does
        if event.type == pygame.QUIT: 
            run = False # end the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: 
                run = False #end the game
            if event.key == pygame.K_LEFT:
                newX = -1 #go left
            if event.key == pygame.K_RIGHT:
                newX = 1 # go right
            if event.key == pygame.K_UP:
                newY = -1 #go up
            if event.key == pygame.K_DOWN:
                newY = 1 #go down

        if event.type == pygame.KEYUP: # stop the movement if the buttom is up because it is a loop
            if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
                newX = 0 
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                newY = 0

            if event.key == pygame.K_SPACE: # firing the oranges
                if kertassastatu == "hey":
                    kertassaY = VeggieY
                    kertassaX = VeggieX
                    fire(kertassaX,kertassaY) # giving the cordination
                    sound = mixer.Sound('sounds/laser.wav')
                    sound.play()

    # the charchter should stay in the screen and not go far away and thereforw it is corrected when it _
    # exceed the boundries
    VeggieX = VeggieX + newX
    if VeggieX < 10 or VeggieX > 922:
        VeggieX = VeggieX - newX
    VeggieY = VeggieY + newY
    if VeggieY < 50 or VeggieY > 700:
        VeggieY = VeggieY - newY

    # i fill the screen with black and then with the background
    screen.fill((0,0,0))
    screen.blit(Background,(0,-100)) #this coordination give the background in the center
    # i render the vegetables
    render_veggie(VeggieX, VeggieY)
    render_diary(DiaryX, DiaryY)
    render_egg(eggX,eggY)
    render_meat(meatX, meatY)

# here i make sure that the vegetables are moving and that they are changing direction at the edge_
# and going down
    DiaryX = DiaryX + DiaryNewX
    if DiaryX <= 0:
        DiaryNewX = 0.35
        DiaryY = DiaryY + 70
    elif DiaryX >= 950:
        DiaryNewX = -0.35
        DiaryY = DiaryY + 250

    eggX = eggX + eggNewX
    if eggX <= 0:
        eggNewX = 0.45
        eggY = eggY + 100
    elif eggX >= 950:
        eggNewX = -0.45
        eggY = eggY + 100

    meatX=meatX+meatNewX
    if meatX <= 0:
        meatNewX = 0.25
        meatY = meatY + 50
    elif meatX >= 950:
        meatNewX = -0.25
        meatY = meatY + 180

    # now i draw the animals and move them
    for i in range(0,5):
        render_backup(i,backupx[i], backupy[i])
        backupy[i] = backupy[i] - backupnew # i can change the speed of animals by changing backunew's value
        if backupy[i] < -6000: # the coordination so they take more time before coming again
            backupx[i] = random.randint(10, 900) # the coordination because i dont want them to start always low
            backupy[i] = random.randint(0, 1000)

    # rendering and moving the orange
    if kertassastatu == "ho": # the orange was fired
        fire(kertassaX,kertassaY) # i render it
        kertassaY = kertassaY - 1 # the orange moves up
        if kertassaY < 0: # the orange is now up and exceeded the screen
            kertassaY = VeggieY #come back to the place of my war veggie space
            kertassastatu = "hey" # the status change

    # i check collisions
    collision=boom(meatX,meatY,kertassaX,kertassaY)
    collision2=boom(DiaryX,DiaryY,kertassaX,kertassaY)
    collision3 = boom(eggX, eggY, kertassaX, kertassaY)

    # if collision the explosion sound goes and i get a score and the veggie war space can shoot again_
    # and the vegetables are once appearing somewhere else
    if collision and kertassastatu=="ho":
        expolision = mixer.Sound('sounds/explosion.wav')
        expolision.play()
        score += 1
        kertassaY = VeggieY
        kertassastatu = "hey"
        print("you did it! now your score is", score)
        meatX = random.randint(10, 900)
        meatY = random.randint(10, 300)

    if collision2 and kertassastatu=="ho":
        expolision = mixer.Sound('sounds/explosion.wav')
        expolision.play()
        score += 2
        kertassaY = VeggieY
        kertassastatu = "hey"
        print("you did it! now your score is", score)
        DiaryX = random.randint(10, 900)
        DiaryY = random.randint(10, 300)

    if collision3 and kertassastatu=="ho":
        expolision = mixer.Sound('sounds/explosion.wav')
        expolision.play()
        score += 3
        kertassaY = VeggieY
        kertassastatu = "hey"
        print("you did it! now your score is", score)
        eggX = random.randint(10, 900)
        eggY = random.randint(10, 300)

    # now i check the collision of my backup
    for i in range(5):
        x = int(backupx[i])
        y = int(backupy[i])
        if boom(meatX,meatY,x,y):
            horse = mixer.Sound('sounds/horse.wav')
            horse.play()
            meatX = random.randint(10, 900)
            meatY = random.randint(10, 300)
            backupx[i] = random.randint(10, 900)
            backupy[i] = random.randint(-1000, 0)
        if boom(DiaryX, DiaryY, x, y):
            horse = mixer.Sound('sounds/horse.wav')
            horse.play()
            DiaryX = random.randint(10, 900)
            DiaryY = random.randint(10, 300)
            backupx[i] = random.randint(10, 900)
            backupy[i] = random.randint(-1000, 0)
        if boom(eggX, eggY, x, y):
            horse = mixer.Sound('sounds/horse.wav')
            horse.play()
            eggX = random.randint(10, 900)
            eggY = random.randint(10, 300)
            backupx[i] = random.randint(10, 900)
            backupy[i] = random.randint(-1000, 0)

    # now i check whether not veggies exceeded the line and i lost 
    # if so i end the game give the score and that was it
    if eggY>800 or DiaryY>800 or meatY>800:
        screen.fill((0,0,0))
        msg("you lost, you ar out", color) #show the text
        pygame.display.update()
        time.sleep(3)
        show(250,200) #show the score
        pygame.display.update()
        time.sleep(4)
        pygame.quit() #quite the game
        quit()

    show(textX,textY) #show the score the whole time
    pygame.display.update()