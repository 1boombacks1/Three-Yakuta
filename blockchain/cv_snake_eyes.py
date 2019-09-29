import pygame
import random
import os

pygame.init()

current_path = os.path.dirname(r"C:\Users\boomb\Desktop\work\python\bitcoin_notification\blockchain\cv_snake_eyes.py")
resource_path = os.path.join(current_path, "rashodniki")
image_path = os.path.join(resource_path, "Objects")
char_image_path = os.path.join(resource_path, "charachters")



#дисплей
display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Three Yakuta")

icon = pygame.image.load(os.path.join(current_path, "icon.png"))
pygame.display.set_icon(icon)

music_path = os.path.join(resource_path, "Sounds")
button_sound = pygame.mixer.Sound(os.path.join(music_path, 'button.wav'))
jump_sound = pygame.mixer.Sound(os.path.join(music_path, '8bit-synth-bounce-short (online-audio-converter.com).wav'))
fall_sound = pygame.mixer.Sound(os.path.join(music_path, 'Bdish.wav'))
loss_sound = pygame.mixer.Sound(os.path.join(music_path, 'loss.wav'))
heart_plus_sound = pygame.mixer.Sound(os.path.join(music_path, 'hp+.wav'))

jump_sound.set_volume(0.05)
heart_plus_sound.set_volume(0.1)
fall_sound.set_volume(0.1)



cactus_images = [pygame.image.load(os.path.join(image_path, 'Cactus0.png')),
                 pygame.image.load(os.path.join(image_path, 'Cactus1.png')),
                 pygame.image.load(os.path.join(image_path, 'Cactus2.png'))]
cactus_options = [69, 449, 37, 410, 40, 420]

stone_image = [pygame.image.load(os.path.join(image_path, 'Stone0.png')),
               pygame.image.load(os.path.join(image_path, 'Stone1.png'))]

cloud_image = [pygame.image.load(os.path.join(image_path, 'Cloud0.png')),
               pygame.image.load(os.path.join(image_path, 'Cloud1.png'))]

yasha_image = [pygame.image.load(os.path.join(char_image_path, 'yasha1.png')),
              pygame.image.load(os.path.join(char_image_path, 'yasha2.png')),
              pygame.image.load(os.path.join(char_image_path, 'yasha3.png')),
              pygame.image.load(os.path.join(char_image_path, 'yasha4.png')),
              pygame.image.load(os.path.join(char_image_path, 'yasha5.png')),
              pygame.image.load(os.path.join(char_image_path, 'yasha6.png')),
              pygame.image.load(os.path.join(char_image_path, 'yasha7.png')),
              pygame.image.load(os.path.join(char_image_path, 'yasha8.png')),
              pygame.image.load(os.path.join(char_image_path, 'yasha9.png')),
              pygame.image.load(os.path.join(char_image_path, 'yasha10.png')),
              pygame.image.load(os.path.join(char_image_path, 'yasha11.png')),
              pygame.image.load(os.path.join(char_image_path, 'yasha12.png'))]

nikich_image = [pygame.image.load(os.path.join(char_image_path, 'Dino0.png')),
                pygame.image.load(os.path.join(char_image_path, 'Dino1.png')),
                pygame.image.load(os.path.join(char_image_path, 'Dino2.png')),
                pygame.image.load(os.path.join(char_image_path, 'Dino3.png')),
                pygame.image.load(os.path.join(char_image_path, 'Dino4.png')),]

dunis_image = [ pygame.image.load(os.path.join(char_image_path, 'Dino2_0.png')),
                pygame.image.load(os.path.join(char_image_path, 'Dino2_1.png')),
                pygame.image.load(os.path.join(char_image_path, 'Dino2_2.png')),
                pygame.image.load(os.path.join(char_image_path, 'Dino2_3.png')),
                pygame.image.load(os.path.join(char_image_path, 'Dino2_4.png'))]

chars = [yasha_image, nikich_image, dunis_image]

effect_path = os.path.join(resource_path, 'Effects')
health_image = pygame.image.load(os.path.join(effect_path, 'heart.png'))
health_image = pygame.transform.scale(health_image, (30, 30))

img_counter = 0
health = 3
num_char = 10


class Object:
    def __init__(self, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.speed = speed

    def move(self):
        if self.x >= -self.width:
            display.blit(self.image, (self.x, self.y,))
            self.x -= self.speed
            return True
        else:
            return False

    def return_object(self, radius, y, width, image,):
        self.x = radius
        self.y = y
        self.width = width
        self.image = image
        display.blit(self.image, (self.x, self.y,))

class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (238, 130, 238)
        self.active_color = (221, 160, 221)

    def draw(self, x, y, message = None, action=None, font_size=30, frame=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #если есть рамка
        if frame is not None:
            if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
                pygame.draw.rect(
                display,
                self.active_color,
                (x, y, self.width, self.height),
                frame)
            if click[0] == 1 and action is not None:
                    pygame.mixer.Sound.play(button_sound)
                    pygame.time.delay(300)
                    if action == quit:
                        pygame.quit()
                        quit()
                    else:
                        action()
                    action()
            else:
                pygame.draw.rect(
                    display,
                    self.inactive_color,
                    (x,y, self.width, self.height),
                    frame)
        else:
        #если нет рамки
            if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
                pygame.draw.rect(display,self.active_color, (x, y, self.width, self.height))

                if click[0] == 1 and action is not None:
                    pygame.mixer.Sound.play(button_sound)
                    pygame.time.delay(300)
                    if action == quit:
                        pygame.quit()
                        quit()
                    else:
                        action()

                    action()
            else:
                pygame.draw.rect(display, self.inactive_color, (x, y, self.width, self.height))

            print_text(message=message, x=x+10, y=y+10, font_size=font_size)

#персонаж
usr_width = 60
usr_height = 100
usr_x = display_width // 3
usr_y = display_height - usr_height - 100

#кактус
cactus_width = 20
cactus_height = 70
cactus_x = display_width - 50
cactus_y = display_height - cactus_height - 100

clock = pygame.time.Clock()

#переменные прыжка
make_jump = False
jump_counter = 30

#счетчик
scores = 0
max_scores = 0
max_above = 0


def show_menu():
    background_path = os.path.join(resource_path, 'Backgrounds')
    menu_background = pygame.image.load(os.path.join(background_path, 'menuTY.jpg'))

    #Музыка
    pygame.mixer.music.load(os.path.join(music_path, 'Reeree - B34CHPAKKETBOY.mp3'))
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    start_button = Button(115, 40)
    quit_button = Button(80, 50)


    show = True

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            display.blit(menu_background, (0,0))
            start_button.draw(635,320,'Start game!', select_person, 18)
            quit_button.draw(650, 380, 'Quit', quit)

            pygame.display.update()
            clock.tick(60)

def select_person():
    global num_char

    background_path = os.path.join(resource_path, 'Backgrounds')
    select_background = pygame.image.load(os.path.join(background_path, 'select.jpg'))
    hero_icon = [pygame.image.load(os.path.join(background_path, "hero1.jpg")),
                 pygame.image.load(os.path.join(background_path, "hero2.jpg")),
                 pygame.image.load(os.path.join(background_path, "hero3.jpg"))]

    first_pers = Button(200, 450)
    second_pers = Button(200, 450)
    third_pers = Button(200, 450)

    show = True

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.blit(select_background, (0,0))

        keys = pygame.key.get_pressed()
        one = first_pers.draw(50,75, frame=8)
        two = second_pers.draw(300,75,frame=8)
        three = third_pers.draw(550,75, frame=8)

        display.blit(hero_icon[0],(58,83))
        display.blit(hero_icon[1],(308,83))
        display.blit(hero_icon[2],(558,83))

        if keys[pygame.K_1]:
            num_char = 2
            start_game()
        if keys[pygame.K_2]:
            num_char = 0
            start_game()
        if keys[pygame.K_3]:
            num_char = 1
            start_game()

        pygame.display.update()
        clock.tick(60)

def start_game():
    global scores, make_jump, jump_counter, usr_y, health

    #Музыка
    pygame.mixer.music.load(os.path.join(music_path, 'Big_Slinker.mp3'))
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    while game_loop():
        scores = 0
        make_jump = False
        jump_counter = 30
        usr_y = display_height - usr_height - 100
        health = 3

#основа
def game_loop():
    global make_jump, num_char

    game = True
    cactus_arr = []
    create_cactus_arr(cactus_arr)

    heart = Object(display_width, 280, 30, health_image, 4)

    stone, cloud = open_random_objects()

    current_path = os.path.dirname(r"C:\Users\boomb\Desktop\work\python\bitcoin_notification\blockchain\cv_snake_eyes.py")
    resource_path = os.path.join(current_path, "rashodniki")
    image_path = os.path.join(resource_path, "Backgrounds")

    lands = ['Land.jpg', 'Land2.jpg', 'LandLevel.jpg', 'neon2.jpg']
    rdm = random.randrange(0,4)
    land = pygame.image.load(os.path.join(image_path,lands[rdm]))

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            make_jump = True
        if keys[pygame.K_ESCAPE]:
            pause()

        if make_jump:
            jump()

        count_scores(cactus_arr)

        display.blit(land, (0, 0))

        print_text('Scores: ' + str(scores), 600, 10)

        draw_arr(cactus_arr)

        move_objects(stone, cloud)

        draw_dino(num_char)
        heart.move()
        hearts_plus(heart)

        if check_collision(cactus_arr):
            pygame.mixer.music.stop()
            game = False

        show_health()

        pygame.display.update()
        clock.tick(80)
    return game_over()

#функция прыжка
def jump():
    global usr_y, jump_counter, make_jump

    if jump_counter >= -30:
        if jump_counter == 30:
            pygame.mixer.Sound.play(jump_sound)
        if jump_counter == -10:
            pygame.mixer.Sound.play(fall_sound)

        usr_y -= jump_counter / 3
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False

def create_cactus_arr(array):
    choice = random.randrange(0, 3)
    image = cactus_images[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 20, height, width, image, 4))

    choice = random.randrange(0, 3)
    image = cactus_images[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 300, height, width, image, 4))

    choice = random.randrange(0, 3)
    image = cactus_images[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 600, height, width, image, 4))


def find_radius(array):
    maximum = max(array[0].x, array[1].x, array[2].x)

    if maximum < display_width:
        radius = display_width
        if radius - maximum < 50:
            radius += 280
    else:
        radius = maximum

    choice = random.randrange(0, 5)
    if choice == 0:
        radius += random.randrange(10,15)
    else:
        radius += random.randrange(250, 400)

    return radius


def draw_arr(array):
    for cactus in array:
        check = cactus.move()
        if not check:
            object_return(array, cactus)

def draw_dino(char):
    global img_counter
    if img_counter == 60:
        img_counter = 0

    display.blit(chars[char][img_counter // 5], (usr_x, usr_y))
    img_counter += 1


def object_return(objects, obj):
        radius = find_radius(objects)

        choice = random.randrange(0, 3)
        image = cactus_images[choice]
        width = cactus_options[choice * 2]
        height = cactus_options[choice * 2 + 1]

        obj.return_object(radius, height, width, image)


def open_random_objects():
    choice = random.randrange(0, 2)
    img_of_stone = stone_image[choice]

    choice = random.randrange(0, 2)
    img_of_cloud = cloud_image[choice]

    stone = Object(display_width, display_height - 80, 10, img_of_stone, 4)
    cloud = Object(display_width, 80, 70, img_of_cloud, 2)

    return stone, cloud

def move_objects(stone, cloud):
    check = stone.move()
    if not check:
        choice = random.randrange(0, 2)
        img_of_stone = stone_image[choice]
        stone.return_object(display_width, 500 + random.randrange(10, 80), stone.width, img_of_stone)

    check = cloud.move()
    if not check:
        choice = random.randrange(0, 2)
        img_of_cloud = cloud_image[choice]
        cloud.return_object(display_width, random.randrange(10, 200), stone.width, img_of_cloud)

def print_text(message, x, y, font_color = (255, 255, 255), font_size = 30):
    font_type = pygame.font.Font(os.path.join(current_path, 'PingPong.ttf'), font_size)
    text = font_type.render(message, True, font_color)

    display.blit(text, (x, y))

def pause():
    paused = True

    pygame.mixer.music.pause()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text("Paused. Press enter to continue.", 160, 300)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        clock.tick(15)
    pygame.mixer.music.unpause()


def check_collision(barriers):
    for barrier in barriers:
        if barrier.y == 449: # little cactus
            if not make_jump:
                if barrier.x <= usr_x + usr_width - 35 <= barrier.x + barrier.width:
                    if cheak_health():
                        object_return(barriers, barrier)
                        return False
                    else:
                        return True

            elif jump_counter >= 0:
                if usr_y + usr_height - 5 >= barrier.y:
                    if barrier.x <= usr_x + usr_width - 30 <= barrier.x + barrier.width:
                        if cheak_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True
            else:
                if usr_y + usr_height - 10 >= barrier.y:
                    if barrier.x <= usr_x <= barrier.x + barrier.width:
                        if cheak_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True
        else:
            if not make_jump:
                if barrier.x <= usr_x + usr_width - 5 <= barrier.x + barrier.width:
                    if cheak_health():
                        object_return(barriers, barrier)
                        return False
                    else:
                        return True
            elif jump_counter == 10:
                if usr_y + usr_height - 5 >= barrier.y:
                    if barrier.x <= usr_x + usr_width - 5 <= barrier.x + barrier.width:
                        if cheak_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True
            elif jump_counter == 1:
                if usr_y + usr_height - 5 >= barrier.y:
                    if barrier.x <= usr_x + usr_width - 30 <= barrier.x + barrier.width:
                        if cheak_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True
            else:
                if usr_y + usr_height - 10 >= barrier.y:
                     if barrier.x <= usr_x + 5 <= barrier.x + barrier.width:
                        if cheak_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True
    return False


def count_scores(barriers):
    global scores, max_above
    above_cactus = 0

    if -20 <= jump_counter <= 25:
        for barrier in barriers:
            if usr_y + usr_height - 5 <= barrier.y:
                if barrier.x <= usr_x <= barrier.x + barrier.width:
                    above_cactus += 1
                elif barrier.x <= usr_x + usr_width <= barrier.x + barrier.width:
                    above_cactus += 1

        max_above = max(max_above, above_cactus)
    else:
        if jump_counter == -30:
            scores += max_above
            max_above = 0

def show_health():
    global health
    show = 0
    x = 20
    while show != health:
        display.blit(health_image, (x,20))
        x += 40
        show += 1

def cheak_health():
    global health
    health -= 1
    if health == 0:
        pygame.mixer.Sound.play(loss_sound)
        return False
    else:
        pygame.mixer.Sound.play(fall_sound)
        return True

def hearts_plus(heart):
    global health, usr_x, usr_y, usr_width, usr_height

    if heart.x <= -heart.width:
        radius = display_width + random.randrange(2000, 5000)
        new_height = display_height - 200 - random.randrange(-75, 200)
        heart.return_object(radius, new_height, heart.width, heart.image)

    if usr_x <= heart.x <= usr_x + usr_width:
        if usr_y <= heart.y <= usr_y + usr_height:
            pygame.mixer.Sound.play(heart_plus_sound)
            if health < 3:
                health += 1

            radius = display_width + random.randrange(2000, 5000)
            new_height = display_height - 200 - random.randrange(-75, 200)
            heart.return_object(radius, new_height, heart.width, heart.image)

def game_over():
    global scores, max_scores

    if scores > max_scores:
        max_scores = scores

    stoped = True
    while stoped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text("Game Over Dude! =((", 255, 200)
        print_text("Press Enter to game again, or Esc to exit.", 90, 250)
        print_text("Max scores: " + str(max_scores), 285, 300)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return  True
        if keys[pygame.K_ESCAPE]:
            return False

        pygame.display.update()
        clock.tick(15)


show_menu()
pygame.quit()
quit()
