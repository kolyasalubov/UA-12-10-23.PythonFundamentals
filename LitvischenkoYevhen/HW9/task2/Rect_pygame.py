import pygame

FPS = 60

width=200
height=200

COORD_X=50
COORD_Y=50
WIDTH_RECTANGLE=40
HEIGHT_RECTANGLE=60
DELTA_STEP=5

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

pygame.init()


gameDisplay = pygame.display.set_mode((width, height), pygame.RESIZABLE)

pygame.display.set_caption("My first game")


run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
        
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.VIDEORESIZE: # if resize window
            width, height = event.w, event.h

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and (COORD_X >= DELTA_STEP) :
        COORD_X = COORD_X-DELTA_STEP
    if keys[pygame.K_RIGHT] and (COORD_X < width - WIDTH_RECTANGLE):
        COORD_X = COORD_X+DELTA_STEP
    if keys[pygame.K_UP] and (COORD_Y >= DELTA_STEP):
        COORD_Y = COORD_Y-DELTA_STEP
    if keys[pygame.K_DOWN] and (COORD_Y < height - HEIGHT_RECTANGLE):
        COORD_Y = COORD_Y+DELTA_STEP


    gameDisplay.fill(BLACK_COLOR) 

    pygame.draw.rect(gameDisplay, RED_COLOR, [COORD_X, 
                                              COORD_Y, 
                                              WIDTH_RECTANGLE, 
                                              HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)
    

