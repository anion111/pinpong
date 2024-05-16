from pygame import* 
from PIL import Image
from random import*
import pygame.gfxdraw
from pygame_animatedgif import AnimatedGifSprite

win = display.set_mode((500,500))
clck = time.Clock()
game = True


finish = False
live = 3
speedX = 3
speedY = 3     


class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)


        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed


        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.size = size_x
    #метод, отрисовывающий героя на окне

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

colors = [(245, 171, 234), (228, 174, 242), (98, 137, 245), (168, 225, 240) ,(134, 227, 193) ,(134, 227, 193)]

# class GIFImage(object):
#     def __init__(self, filename):
#         self.filename = filename
#         self.image = Image.open(filename)
#         self.frames = []
#         # self.get_frames()
 
#         self.cur = 0
#         self.ptime = time.time()
 
#         self.running = True
#         self.breakpoint = len(self.frames)-1
#         self.startpoint = 0
#         self.reversed = False
# gif = AnimatedGifSprite.GIFImage("gif.gif")

# width = 500
# height = 500
# image = pygame.Surface([width, height])
# gif.render(self.image, (0, 0))


font.init()
font1 = font.Font(None, 40)
# winn = font1.render(, True , random.choice(colors))
# lose = font1.rander('Ohh nooo!!!', True, random.choice(colors))


text = "YYYEEEPIIII, YAPI<3!! ,YEPI,YEPI!!!! >-<"

text1 = "Ohh nooo!!!"


# mixer.init()
# mixer.music.loud("")
# mixer.music.play()

# sound1 = pg.mixer.Sound('')
# sound2 = pg.mixer.Sound('')


class Player(GameSprite):

        def update(self):
            keys = key.get_pressed()
            if keys[K_j] and self.rect.y <= 450 :
                self.rect.y += self.speed
                

            if keys[K_l] and self.rect.y >= 3:
                self.rect.y -= self.speed

        def update1(self):
            keys = key.get_pressed()
            if keys[K_d] and self.rect.y >= 3 :
                self.rect.y -= self.speed
            if keys[K_a] and self.rect.y <= 450 :
                self.rect.y += self.speed




empty_surface = Surface((500, 500))
sprite_group = sprite.Group()

rar = Player('photo1715712483 (1).png', 450, 300, 20, 30, 20)
ral = Player( 'photo1715712483 (3).png', 30, 300, 80, 30, 20)
ball = GameSprite("r.png", 90, 200, 60, 30, 10)
textes = []
texters = []
d = 190
for i in range(len(text)-1):
    

    let = font1.render(text[i], True, choice(colors))
    texters.append(let)

for i in range(len(text1)-1):
    shuffle(colors)
    lett = font1.render(text1[i], True, choice(colors))
    textes.append(lett)
while game:

    
    
    if finish != True:
        ball.rect.x += speedX
        ball.rect.y += speedY

        if ball.rect.y >= 450-50  or ball.rect.y <= 0:
            speedY *= -1



        if sprite.collide_rect(rar, ball) or sprite.collide_rect(ral, ball):
            speedX *= -1
        win.blit(let, (200, 200))
        win.fill((255, 255, 255))
        ball.reset()
        rar.update()      
        rar.reset()
        ral.update()
        ral.reset()
        if ball.rect.x >= 500 or ball.rect.x <= 0:
            ball.reset()
            live -= 1  
            if live == 0: 
           

                for text in textes:
                   win.blit(text, (d,200))
                   d= d + 16
                  


                finish = True
            #     time.delay(2000)
            #     break

        dog = AnimatedGifSprite((50, 50), "gif.gif")
        sprite_group.add(dog)
        # sprite_group.blit(empty_surface, (50, 50))
        sprite_group.update()

        # dog.scale(0.5)
    for e in event.get():
        if e.type == QUIT:
            game = False


    

   
    clck.tick(60)
        # win.blit()
    display.update()
