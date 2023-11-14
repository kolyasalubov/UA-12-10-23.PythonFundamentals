import pygame

# визначаємо константу затримки кадрів
# та інші константи
FPS = 60

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500

WHITE_COLOR = (255, 255, 255)	
ORANGE_COLOR = (255, 150, 100)

COORD_X = WIDTH_DISPLAY/2 - 20
COORD_Y = HEIGHT_DISPLAY/2 - 30
WIDTH_RECTANGLE = 40
HEIGHT_RECTANGLE = 60
DELTA_STEP = 15
 
# ініціалізація та створення об'єктів
pygame.init()
pygame.display.set_mode((600, 400))

gameDisplay=pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)

pygame.display.set_caption("My first game")

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and COORD_X > DELTA_STEP:
        COORD_X = COORD_X - DELTA_STEP
    if keys[pygame.K_RIGHT] and COORD_X < WIDTH_DISPLAY - 3*DELTA_STEP : 
        COORD_X = COORD_X + DELTA_STEP
    # if COORD_X >= WIDTH_DISPLAY:
    #     COORD_X = WIDTH_DISPLAY-40
    if keys[pygame.K_UP] and COORD_Y > DELTA_STEP:
        COORD_Y = COORD_Y - DELTA_STEP
    if keys[pygame.K_DOWN] and COORD_Y < HEIGHT_DISPLAY - 4*DELTA_STEP:
        COORD_Y = COORD_Y + DELTA_STEP
    # if COORD_Y >= HEIGHT_DISPLAY:
    #     COORD_Y = HEIGHT_DISPLAY-60
    if keys[pygame.K_ESCAPE]:
        run = False


    gameDisplay.fill((25,0,25)) 

    pygame.draw.rect(gameDisplay, (255,0,0), [COORD_X, 
                                        COORD_Y, 
                                        WIDTH_RECTANGLE, 
                                        HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)
    
