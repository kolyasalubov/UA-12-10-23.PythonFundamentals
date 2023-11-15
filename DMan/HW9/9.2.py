import pygame

# визначаємо константу затримки кадрів
# та інші константи
FPS = 60

WIDTH_DISPLAY=600
HEIGHT_DISPLAY=400

WHITE_COLOR = (255, 255, 255)	
ORANGE_COLOR = (255, 150, 100)

WIDTH_RECTANGLE = 40
HEIGHT_RECTANGLE = 60
COORD_X = WIDTH_DISPLAY/2 - WIDTH_RECTANGLE/2     # змістив початкову точку до центру
COORD_Y = HEIGHT_DISPLAY/2 - HEIGHT_RECTANGLE/2
DELTA_STEP = 15                                   # збільшив крок
 
pygame.init()
pygame.display.set_mode((600, 400))

# убрав повноекранний режим:
gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE) 

pygame.display.set_caption("My first game")

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and COORD_X > 10:
        COORD_X = COORD_X - DELTA_STEP
    if keys[pygame.K_RIGHT] and COORD_X < WIDTH_DISPLAY - 3*DELTA_STEP : 
        COORD_X = COORD_X + DELTA_STEP
    if keys[pygame.K_UP] and COORD_Y > 0:
        COORD_Y = COORD_Y - DELTA_STEP
    if keys[pygame.K_DOWN] and COORD_Y < HEIGHT_DISPLAY - 4*DELTA_STEP:
        COORD_Y = COORD_Y + DELTA_STEP
         # або ж таким чином, тільки тоді прямокутник буде виходити
         # за межі екрану, но потім одразу ж вертатись: 
    # if COORD_X >= WIDTH_DISPLAY:
    #     COORD_X = WIDTH_DISPLAY-40
    # if COORD_Y >= HEIGHT_DISPLAY:
    #     COORD_Y = HEIGHT_DISPLAY-60

    if keys[pygame.K_ESCAPE]:  # добавив вихід через кнопку "ESCAPE"
        run = False


    gameDisplay.fill((0, 0, 0)) 

    pygame.draw.rect(gameDisplay, (0, 250, 0), [COORD_X,   #змінив на зелений
                                        COORD_Y, 
                                        WIDTH_RECTANGLE, 
                                        HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)
    
