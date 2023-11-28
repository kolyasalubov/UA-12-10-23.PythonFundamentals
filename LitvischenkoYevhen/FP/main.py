import pygame
import math
from random import randint

pygame.init()
spider_img = [pygame.image.load(f'/images/sprite/spider_{i}.png').convert_alpha() for i in range(1, 5)]
spit_img = [pygame.image.load(f'images/sprite/spit_{i}.png').convert_alpha() for i in range(1, 6)]
spit_bat_img = [pygame.image.load(f'images/sprite/spit_bat_{i}.png').convert_alpha() for i in range(1, 6)]
bat_img = [pygame.image.load(f'images/sprite/bat_{i}.png').convert_alpha() for i in range(1, 7)]
stoun_img = [pygame.image.load(f'images/sprite/stoun_{i}.png').convert_alpha()  for i in range(1, 6)]
bonus_img = [pygame.image.load(f'images/sprite/bonus_{i}.png').convert_alpha()  for i in range(1, 4)]
bang_img = [pygame.image.load(f'images/sprite/bang_{i}.png').convert_alpha()  for i in range(1, 8)]

game = pygame.image.load("images/icon/logo1.png")

background_image = pygame.image.load("images/bg/bg3.jpg").convert_alpha()
background_rect = background_image.get_rect()

# background_sound = pygame.mixer.Sound("sounds/4.wav")
# background_sound.play(-1)
spit_sound = pygame.mixer.Sound("sounds/plevok.mp3")
bang_sound = pygame.mixer.Sound("sounds/bang.wav")
game_over_sound = pygame.mixer.Sound("sounds/game.wav")
bonus_sound = pygame.mixer.Sound("sounds/bonus.wav")

clock = pygame.time.Clock()
bat_timer = pygame.USEREVENT + 1 # timet event create bat
bonus_timer = pygame.USEREVENT + 2 #timer event bonus
bonus_timer_delay = 7000 # delay between bonus create
pygame.time.set_timer(bat_timer, 5000)

pygame.time.set_timer(bonus_timer, bonus_timer_delay)

FPS = 20
WIDTH = 720
HEIGHT = 720
WIDTH_SPIDER = 32
HEIGHT_SPIDER = 32
TILE = 45

window = pygame.display.set_mode((WIDTH, HEIGHT))


direction_move = [[-1, 0, 90],[1, 0, 270],[0, -1, 0],[0, 1, 180]]
class Spider():
    """Create Spider"""
    # append to array of objectswhen create
    spider_score = 0
    def __init__(self, px, py, pr, keyList):
        objects.append(self)
        self.px = px
        self.py = py
        self.pr = pr
        self.pr_shot = 0
        self.rect = pygame.Rect(px, py, 40, 40)
        self.direction = 2
        self.move_speed = 2
        self.spit_timer = 0
        self.spit_delay = 30 #delay between spit
        self.spit_speed = 5

        self.hp = 20
        self.damage = 10

        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]
        self.keySHOT = keyList[4]

    def update(self):
        """change position and spit, chech intersection with other objects"""
        old_px, old_py = self.rect.x, self.rect.y

        if keys[self.keyLEFT]:
            self.rect.x -= self.move_speed
            self.direction = 0
        elif keys[self.keyRIGHT]:
            self.rect.x += self.move_speed
            self.direction = 1
        if keys[self.keyUP]:
            self.rect.y -= self.move_speed
            self.direction = 2
        elif keys[self.keyDOWN]:
            self.rect.y += self.move_speed
            self.direction = 3


        for obj in objects:
            if obj != self and not isinstance(obj, Bonus) and self.rect.colliderect(obj.rect):
                self.rect.x, self.rect.y = old_px, old_py

        (self.px, self.py) = self.rect.center

        if (keys[self.keySHOT] or mouse_press[0]) and self.spit_timer == 0:
            Spit(self, self.px, self.py, self.pr, self.direction, self.damage, self.spit_speed)
            self.spit_timer = self.spit_delay
            spit_sound.play()

        if self.spit_timer > 0 :
            self.spit_timer -= 1



    def draw(self):
       """draw spider and rotate to mouse position"""
       spider_spit_rect = spider_img[0].get_rect(center=(self.px, self.py))
       spider_rotate = pygame.transform.rotozoom(spider_img[spider_tik], self.pr, 1.0)
       rotated_spider_rect = spider_rotate.get_rect(center=spider_spit_rect.center)
       window.blit(spider_rotate, rotated_spider_rect.topleft)

    def damages(self, value):
        """change HP when shuted"""
        self.hp -= value
        if self.hp <= 0 :
           objects.remove(self)
    def __del__(self):
        """when spider killed"""
        bang_obj.append(Bang(self.px, self.py))
        game_over()

class Spit():
    """objects spider spit and bat spit"""
    def __init__(self, parent, px, py, pr, direction, damage, speed):
        spit_obj.append(self)
        self.parent = parent #who's spiting
        self.px = px
        self.py = py
        self.pr = pr # angle spit to point on map
        self.direction = direction
        self.move_speed = speed
        self.damage = damage
    def update(self):
        """change spit position , chech intersection with other objects"""
        rad = math.radians(self.pr)
        self.py -= self.move_speed * math.cos(rad)
        self.px -= self.move_speed * math.sin(rad)
        if self.py < 0 or self.py > HEIGHT or self.px < 0 or self.px > WIDTH:
            spit_obj.remove(self)
        else:
            for obj in objects:
                if obj != self.parent and obj.rect.collidepoint(self.px, self.py):
                    if isinstance(self.parent, Spider) and isinstance(obj, Bat):
                        if obj.hp <= self.damage:
                            Spider.spider_score += 5
                            if Spider.spider_score%20 == 0: # if 20 score then LvlUp
                                self.parent.hp += 5
                                self.parent.damage += 5
                                self.parent.move_speed += 3
                                self.parent.spit_speed += 2
                                if self.parent.spit_delay >= 10:
                                    self.parent.spit_delay -= 5
                                info_obj.append(Info(self.px, self.py, 'yellow', "Lvl.UP"))
                    obj.damages(self.damage)
                    info_obj.append(Info(self.px, self.py, 'darkred', f"-{self.damage} HP"))
                    spit_obj.remove(self)
                    bang_sound.play()

    def draw(self):
        #change image spit depending whos spit
        if isinstance(self.parent, Bat):
            spit_images = spit_bat_img
        else:
            spit_images = spit_img

        spit_rect = spit_images[0].get_rect(center=(self.px, self.py))
        spit_rotate = pygame.transform.rotozoom(spit_images[spit_tik], self.pr, 1.0)
        rotated_spit_rect = spit_rotate.get_rect(center=spit_rect.center)
        window.blit(spit_rotate, rotated_spit_rect.topleft)


class Bat():
    def __init__(self, px, py):
        # append to array of objectswhen create
        objects.append(self)
        self.px = px
        self.py = py
        self.rect = pygame.Rect(px, py, 50, 40)
        self.move_speed = 3
        self.spit_timer = 0
        self.spit_delay = 60
        self.direction = 0
        self.spit_timer = 0
        self.spit_delay = 100
        self.spit_speed = 5

        self.correct = 0
        self.correct_timer = 0

        self.hp = 10
        self.damage = 10


    def update(self):
        """change position and spit, chech intersection with other objects"""
        #move bat to spider
        (old_px, old_py) = self.rect.topleft
        if self.correct_timer <= 0 :
            if objects[0].rect.x < self.rect.x :
                self.rect.x -= self.move_speed
                self.direction = 0
            elif objects[0].rect.x > self.rect.x:
                self.rect.x += self.move_speed
                self.direction = 1
            if objects[0].rect.y < self.rect.y :
                self.rect.y -= self.move_speed
                self.direction = 2
            elif objects[0].rect.y > self.rect.y :
                self.rect.y += self.move_speed
                self.direction = 3
        else: # correct move if intersection with blocks of other bat
            self.rect.x += self.move_speed * direction_move[self.direction][0]
            self.rect.y += self.move_speed * direction_move[self.direction][1]
            self.correct_timer -= 1

        # check intersection other objects
        for obj in objects:
            if obj != self and self.rect.colliderect(obj.rect):
                if isinstance(obj, Spider): # if intersection with spider. game over
                    game_over()
                #correct move when intersection
                self.rect.x, self.rect.y = old_px, old_py
                self.correct_timer = 10
                self.direction += 1
                if self.direction == 4 :
                    self.direction = 0
        (self.px, self.py) = self.rect.topleft
        # spit
        if self.spit_timer > 0:
            self.spit_timer -= 1
        else:
            self.spit_timer = self.spit_delay
            angel = calculate_angle(self.px, self.py, objects[0].px, objects[0].py) - 180
            Spit(self, self.px, self.py, angel, self.direction, self.damage, self.spit_speed)
        self.rect = pygame.Rect(self.px, self.py, 32, 32)

    def draw(self):
        window.blit(bat_img[bat_tik], self.rect.topleft)
    def damages(self, value):
        #change HP when spitted and check for die
        self.hp -= value
        if self.hp <= 0 :
           objects.remove(self)
    def __del__(self):
        # when destroyed create animation bang and info
        info_obj.append(Info(self.px, self.py, 'darkblue', "+5 score"))
        bang_obj.append(Bang(self.px, self.py))

class Block():
    def __init__(self, px, py, size, img):
        #append to array of objectswhen create
        objects.append(self)
        self.px = px
        self.py = py
        self.rect = pygame.Rect(px, py, size, size)
        self.img = img
        self.hp = 20
    def update(self):
        pass
    def draw(self):
        window.blit(stoun_img[self.img], self.rect.topleft)
    def damages(self, value):
        self.hp -= value
        if self.hp <= 0:
            objects.remove(self)
    def __del__(self):
        #when destroyed create animation bang
        bang_obj.append(Bang(self.px, self.py))

class Bonus():
    """object bonus"""
    def __init__(self, px, py, size, type, img):
        objects.append(self)
        self.px = px
        self.py = py
        self.rect = pygame.Rect(px, py, size, size)
        self.img = img
        self.type = type # type of bonus
        self.time_to_live = 600 # time to live

    def update(self):
        #check live bonus
        if self.time_to_live > 0 :
            self.time_to_live -= 1
        else:
            objects.remove(self) #remove bonus when time
        #check objects get bonus
        for obj in objects:
            if obj != self and obj.rect.colliderect(self.rect):
                if isinstance(obj, Spider) or isinstance(obj, Bat):
                    if self.type == 0: # bonus + HP
                        obj.hp += 10
                        info_obj.append(Info(self.px, self.py, 'red', "+10 HP"))
                    elif self.type == 1: # bonus LvlUP
                        obj.hp += 10
                        obj.damage += 5
                        obj.move_speed += 3
                        obj.spit_speed += 2
                        if obj.spit_delay >= 10:
                            obj.spit_delay -= 5
                        info_obj.append(Info(self.px, self.py, 'yellow', "Lvl.UP"))
                    elif self.type == 2: # bonus - HP
                        obj.hp -= 10
                        info_obj.append(Info(self.px, self.py, 'darkblue', "-10 HP"))
                        if obj.hp <= 0:
                            objects.remove(obj)
                    bonus_sound.play()
                objects.remove(self) #remove bonus when get it
    def draw(self):
        if self.time_to_live % 30 < 15 :
            window.blit(self.img, self.rect.topleft)
    def damages(self, value):
        objects.remove(self)

class UI():
    """show UI. HP Spider and score"""
    def __init__(self):
        self.px = 20
        self.py = 10


    def draw(self):
        rect_ui = pygame.Rect(self.px + 50, self.py, objects[0].hp*5, 25)
        pygame.draw.rect(window, 'darkred', rect_ui)
        font = pygame.font.Font('fonts/Zhizn.otf', 36)

        text = font.render(str(objects[0].hp), True, 'darkred')
        window.blit(text, (self.px, self.py))

        text = font.render(f'SCORE: {Spider.spider_score}', True, 'darkBlue')
        window.blit(text, (WIDTH - 180, 10))

class Info():
    """show info about event(HP + -, lvl_UP, add score)"""
    def __init__(self, px, py, color, str):
        self.px = px
        self.py = py
        self.color = color
        self.str = str
        self.time = 0


    def draw(self):
        self.time += 2
        if self.time == 30:
            info_obj.remove(self)
        font = pygame.font.Font('fonts/Zhizn.otf', 20)

        text = font.render(self.str, True, self.color)
        window.blit(text, (self.px + 5, self.py - 5 - self.time))

class Bang():
    """class show animation destroy object"""
    def __init__(self, px, py):
        self.px = px
        self.py = py
        self.rect = pygame.Rect(px, py, 45, 45)
        self.count = 0

    def draw(self):
        window.blit(bang_img[self.count], self.rect.topleft)
        self.count += 1
        if self.count == 7:
            bang_obj.remove(self)




def calculate_angle(x1, y1, x2, y2):
    """calculate angle between two points"""
    angle_rad = math.atan2(x2 - x1, y2 - y1)
    angle_deg = math.degrees(angle_rad)
    return angle_deg

def bat_create():
    """ create bat out of map in random place"""
    bat_r = randint(0, 360)
    bat_angle_rad = math.radians(bat_r)
    long_distance = round(((HEIGHT / 2) ** 2 + (WIDTH / 2) ** 2) ** 0.5)
    bat_y = HEIGHT / 2 - long_distance * math.cos(bat_angle_rad)
    bat_x = WIDTH / 2 - long_distance * math.sin(bat_angle_rad)
    Bat(bat_x, bat_y)

def bonus_create():
    while True:
        """create random bonus objects"""
        x = randint(0, WIDTH // TILE) * TILE
        y = randint(0, HEIGHT // TILE) * TILE
        rect = pygame.Rect(x, y, TILE, TILE)
        img = randint(0, 4)
        finded_cros = False
        for obj in objects:
            if rect.colliderect(obj):
                finded_cros = True
        if not finded_cros:
            break
    bonus_type = randint(0, 2)
    Bonus(x, y, 40, bonus_type, bonus_img[bonus_type])

def game_over():
    """screen of game over with total score in game"""
    window.blit(game, (100, 0))
    font = pygame.font.Font('fonts/beer_money.ttf', 100)
    text = font.render('GAME OVER', True, 'darkred')
    window.blit(text, (150, 300))
    font = pygame.font.Font('fonts/Zhizn.otf', 60)
    text = font.render(f'Total Score: {Spider.spider_score}', True, 'darkred')
    window.blit(text, (160, 450))
    global play_game_flag
    global game_over_flag
    play_game_flag = False
    game_over_flag = True
    game_over_sound.play()


# array of objects
#spider, bat, stoun, bonus
objects = []
#spit spider and spit bat
spit_obj = []
#info messeges
info_obj = []
#bang, destroy object
bang_obj = []

#create spider
Spider(100, 100, 0,(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_f))

#instats UI
ui_scren = UI()

#function for create stoun on map
for _ in range(25):
    while True:
        x = randint(0, WIDTH // TILE) * TILE
        y = randint(0, HEIGHT // TILE) * TILE
        rect = pygame.Rect(x, y, TILE, TILE)
        img = randint(0, 4)
        finded_cros = False
        for obj in objects:
            if rect.colliderect(obj):
                finded_cros = True
        if  rect.colliderect(objects[0].rect):
            finded_cros = True
        if not finded_cros:
            break
    Block(x, y, TILE, img)



# spider_img = [pygame.image.load(f'images/sprite/spider_{i}.png').convert_alpha() for i in range(1, 5)]
# spit_img = [pygame.image.load(f'images/sprite/spit_{i}.png').convert_alpha() for i in range(1, 6)]
# spit_bat_img = [pygame.image.load(f'images/sprite/spit_bat_{i}.png').convert_alpha() for i in range(1, 6)]
# bat_img = [pygame.image.load(f'images/sprite/bat_{i}.png').convert_alpha() for i in range(1, 7)]
# stoun_img = [pygame.image.load(f'images/sprite/stoun_{i}.png').convert_alpha()  for i in range(1, 6)]
# bonus_img = [pygame.image.load(f'images/sprite/bonus_{i}.png').convert_alpha()  for i in range(1, 4)]
# bang_img = [pygame.image.load(f'images/sprite/bang_{i}.png').convert_alpha()  for i in range(1, 8)]

# game = pygame.image.load("images/icon/logo1.png")

# background_image = pygame.image.load("images/bg/bg3.jpg").convert_alpha()
# background_rect = background_image.get_rect()

# # background_sound = pygame.mixer.Sound("sounds/4.wav")
# # background_sound.play(-1)
# spit_sound = pygame.mixer.Sound("sounds/plevok.mp3")
# bang_sound = pygame.mixer.Sound("sounds/bang.wav")
# game_over_sound = pygame.mixer.Sound("sounds/game.wav")
# bonus_sound = pygame.mixer.Sound("sounds/bonus.wav")

#sprits counres
spider_tik = 0
bat_tik = 0
spit_tik = 0

play_game_flag = False
game_over_flag = False
start = True

while True:
    clock.tick(FPS)
    pygame.display.update()
    window.blit(background_image, background_rect)


    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if play_game_flag:
                play_game_flag = False
            else:
                play_game_flag = True
                start = False

        if event.type == bat_timer and play_game_flag:
            #event create bat
            bat_create()
        if event.type == bonus_timer and play_game_flag:
            # event create bonus
            bonus_create()
            bonus_timer_delay = randint(40000, 60000)

    keys = pygame.key.get_pressed()
    mouse_position = pygame.mouse.get_pos()
    mouse_press = pygame.mouse.get_pressed()

    if play_game_flag:
        #spider face angle
        spider_r = calculate_angle(mouse_position[0], mouse_position[1], objects[0].px, objects[0].py)
        objects[0].pr = spider_r

        #update and draw objects
        for obj in objects:
            obj.update()
            obj.draw()
        for spit in spit_obj:
            spit.update()
            spit.draw()
        for i in info_obj:
            i.draw()
        for b in bang_obj:
            b.draw()
        ui_scren.draw()

        # animation sprits
        spider_tik += 1
        bat_tik += 1
        spit_tik += 1
        if spider_tik == 4: spider_tik = 0
        if bat_tik == 6: bat_tik = 0
        if spit_tik == 5: spit_tik = 0
    else:
        if game_over_flag:
            game_over()
        else:
            window.blit(game, (120, 30))
            if start:
                font = pygame.font.Font('fonts/beer_money.ttf', 50)
                text = font.render('press SPACE', True, 'black')
                window.blit(text, (250, 600))
            else:
                font = pygame.font.Font('fonts/beer_money.ttf', 100)
                text = font.render('PAUSE', True, 'darkred')
                window.blit(text, (220, 550))

