from sound_funcions.voice import *
import sys, requests, webbrowser, time, openai, pygame, random
import pyautogui as pg
import tkinter as tk



def browser():
	webbrowser.open('https://www.google.com')

def off_bot():
     sys.exit()

def weather(city='Kyiv'):
	my_api='ef2206ff5da67de63306d0b143e20872'
	r=requests.get(
	f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_api}&units=metric'
	)
	res=r.json()
	temp=res['main']['temp']
	feel=res['main']['feels_like']
	litter = res['weather'][0]['description']
	speed=res['wind']['speed']
    
	read(f'Now in {city} {litter}.\n Temperature {round(temp),7} degrees celsium, \n \n It feels like {round(feel)} degrees. \n Window speed {round(speed)} meters per second')


def passive():
    pass

def my_game():
    root = tk.Tk()
    root.title("PING PONG")


    root.geometry("800x600")


    def button1_clicked():
        pvp_game()


    def button2_clicked():
        pve_game()

    button1 = tk.Button(root, text="1 VS 1", width=20, height=5, command=button1_clicked)
    button2 = tk.Button(root, text="VS BOT", width=20, height=5, command=button2_clicked)


    button1.pack(side=tk.LEFT, padx=50, pady=20)
    button2.pack(side=tk.RIGHT, padx=50, pady=20)


    root.mainloop()

def pve_game():
    pygame.init()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0,255,0)

    WIDTH, HEIGHT = 800, 600
    BALL_RADIUS = 10
    PAD_WIDTH, PAD_HEIGHT = 10, 60
    HALF_PAD_HEIGHT = PAD_HEIGHT // 2
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    ball_speed = [0, 0]
    paddle1_pos = [0, HEIGHT // 2 - HALF_PAD_HEIGHT]
    paddle2_pos = [WIDTH - PAD_WIDTH, HEIGHT // 2 - HALF_PAD_HEIGHT]
    l_score = 0
    r_score = 0

    PADDLE_SPEED = 3
    BOT_PADDLE_SPEED = 2

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Ping Pong')

    def update_score():
        score_text = font.render(f"{l_score} : {r_score}", True, WHITE)
        text_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT - 500))
        window.blit(score_text, text_rect)

    def update_game():
        nonlocal ball_pos, ball_speed
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        horz = random.randrange(2, 3)
        vert = random.randrange(1, 3)

        if ball_speed[0] > 0:
            horz = -horz

        ball_speed = [horz, -vert]

    def check_goal():
        nonlocal l_score, r_score
        if ball_pos[0] < BALL_RADIUS:
            r_score += 1
            update_game()
        elif ball_pos[0] > WIDTH - BALL_RADIUS:
            l_score += 1
            update_game()

    def update_bot():
        nonlocal paddle1_pos, ball_pos
        blind_zone = 600

        bot_center = paddle1_pos[1] + HALF_PAD_HEIGHT
        ball_center = ball_pos[1]

        if ball_pos[0] < blind_zone and ball_pos[0] < blind_zone + PAD_WIDTH and ball_center < bot_center:
            if paddle1_pos[1] > 0:
                paddle1_pos[1] -= BOT_PADDLE_SPEED
        elif ball_pos[0] < blind_zone and ball_pos[0] < blind_zone + PAD_WIDTH and ball_center > bot_center:
            if paddle1_pos[1] < HEIGHT - PAD_HEIGHT:
                paddle1_pos[1] += BOT_PADDLE_SPEED
        elif ball_pos[0] < WIDTH / 2 and ball_pos[0] < WIDTH / 2 - PAD_WIDTH:
            pass

    update_game()

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 48)  

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and paddle2_pos[1] > 0:
            paddle2_pos[1] -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddle2_pos[1] < HEIGHT - PAD_HEIGHT:
            paddle2_pos[1] += PADDLE_SPEED

        update_bot() 

        ball_pos[0] += int(ball_speed[0])
        ball_pos[1] += int(ball_speed[1])

        if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
            ball_speed[1] = -ball_speed[1]

        if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH and ball_pos[1] in range(paddle1_pos[1] - BALL_RADIUS, paddle1_pos[1] + PAD_HEIGHT + BALL_RADIUS):
            ball_speed[0] = -ball_speed[0]
            if ball_speed[0] < 0:  
                ball_speed[1] -= BOT_PADDLE_SPEED
            else:  
                ball_speed[1] += BOT_PADDLE_SPEED

        elif ball_pos[0] <= BALL_RADIUS:
            check_goal()

        if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH and ball_pos[1] in range(paddle2_pos[1] - BALL_RADIUS, paddle2_pos[1] + PAD_HEIGHT + BALL_RADIUS):
            ball_speed[0] = -ball_speed[0]
            if ball_speed[0] > 0:
                ball_speed[1] -= PADDLE_SPEED
            else:
                ball_speed[1] += PADDLE_SPEED
        elif ball_pos[0] >= WIDTH - BALL_RADIUS:
            check_goal()
        
        window.fill(BLACK)
        pygame.draw.circle(window, WHITE, ball_pos, BALL_RADIUS)
        pygame.draw.rect(window, WHITE, [paddle1_pos[0], paddle1_pos[1], PAD_WIDTH, PAD_HEIGHT])
        pygame.draw.rect(window, WHITE, [paddle2_pos[0], paddle2_pos[1], PAD_WIDTH, PAD_HEIGHT])

        update_score()

        if l_score >= 7 or r_score >= 7:
            winner_text = font.render(f"Winner: {'BOT' if l_score >= 7 else 'Right Player'}", True, GREEN)
            text_rect = winner_text.get_rect(center=(WIDTH // 2, HEIGHT - 400 ))
            window.blit(winner_text, text_rect)
            pygame.display.update()
            pygame.time.wait(5000)  
            running = False

        pygame.display.update()
        
        clock.tick(130)

    pygame.quit()


def pvp_game():
    pygame.init()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0,255,0)

    WIDTH, HEIGHT = 800, 600
    BALL_RADIUS = 10
    PAD_WIDTH, PAD_HEIGHT = 10, 60
    HALF_PAD_HEIGHT = PAD_HEIGHT // 2
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    ball_speed = [0, 0]
    paddle1_pos = [0, HEIGHT // 2 - HALF_PAD_HEIGHT]
    paddle2_pos = [WIDTH - PAD_WIDTH, HEIGHT // 2 - HALF_PAD_HEIGHT]
    l_score = 0
    r_score = 0

    PADDLE_SPEED = 3
    BOT_PADDLE_SPEED = 2

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Ping Pong')

    def update_score():
        score_text = font.render(f"{l_score} : {r_score}", True, WHITE)
        text_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT - 500))
        window.blit(score_text, text_rect)

    def update_game():
        nonlocal ball_pos, ball_speed
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        horz = random.randrange(2, 3)
        vert = random.randrange(1, 3)

        if ball_speed[0] > 0:
            horz = -horz

        ball_speed = [horz, -vert]

    def check_goal():
        nonlocal l_score, r_score
        if ball_pos[0] < BALL_RADIUS:
            r_score += 1
            update_game()
        elif ball_pos[0] > WIDTH - BALL_RADIUS:
            l_score += 1
            update_game()


    update_game()

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 48)  

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and paddle2_pos[1] > 0:
            paddle2_pos[1] -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddle2_pos[1] < HEIGHT - PAD_HEIGHT:
            paddle2_pos[1] += PADDLE_SPEED
        if keys[pygame.K_w] and paddle1_pos[1] > 0:
            paddle1_pos[1] -= PADDLE_SPEED
        if keys[pygame.K_s] and paddle1_pos[1] < HEIGHT - PAD_HEIGHT:
            paddle1_pos[1] += PADDLE_SPEED
 

        ball_pos[0] += int(ball_speed[0])
        ball_pos[1] += int(ball_speed[1])

        if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
            ball_speed[1] = -ball_speed[1]

        if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH and ball_pos[1] in range(paddle1_pos[1] - BALL_RADIUS, paddle1_pos[1] + PAD_HEIGHT + BALL_RADIUS):
            ball_speed[0] = -ball_speed[0]
            if ball_speed[0] < 0:  
                ball_speed[1] -= BOT_PADDLE_SPEED
            else:  
                ball_speed[1] += BOT_PADDLE_SPEED

        elif ball_pos[0] <= BALL_RADIUS:
            check_goal()

        if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH and ball_pos[1] in range(paddle2_pos[1] - BALL_RADIUS, paddle2_pos[1] + PAD_HEIGHT + BALL_RADIUS):
            ball_speed[0] = -ball_speed[0]
            if ball_speed[0] > 0:
                ball_speed[1] -= PADDLE_SPEED
            else:
                ball_speed[1] += PADDLE_SPEED
        elif ball_pos[0] >= WIDTH - BALL_RADIUS:
            check_goal()
        
        window.fill(BLACK)
        pygame.draw.circle(window, WHITE, ball_pos, BALL_RADIUS)
        pygame.draw.rect(window, WHITE, [paddle1_pos[0], paddle1_pos[1], PAD_WIDTH, PAD_HEIGHT])
        pygame.draw.rect(window, WHITE, [paddle2_pos[0], paddle2_pos[1], PAD_WIDTH, PAD_HEIGHT])

        update_score()

        if l_score >= 7 or r_score >= 7:
            winner_text = font.render(f"Winner: {'Left Player' if l_score >= 7 else 'Right Player'}", True, GREEN)
            text_rect = winner_text.get_rect(center=(WIDTH // 2, HEIGHT - 400 ))
            window.blit(winner_text, text_rect)
            pygame.display.update()
            pygame.time.wait(5000)  
            running = False

        pygame.display.update()
        
        clock.tick(130)

    pygame.quit()


