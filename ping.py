from pygame import * 
import time
pygame.init()


win = pygame.display.set_mode((500,500))
clck = pygame.time.Clock()
game = True





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
    #метод, отрисовывающий героя на окне

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

font.init()
font1 = font.Font(None, 80)
winn = font1.render("YYYEEEPIIII, YAPI<3!! ,YEPI,YEPI!!!! >-<", True ,(()))
lose = font1.rander('Ohh nooo!!!', True, (()))


mixer.init()
mixser.music.loud("")
mixser.music.play()

sound1 = pg.mixer.Sound('')
sound2 = pg.mixer.Sound('')


  class Player(GameSprite):
     def update(self):
        keys = key.get_pressed()
        if keys[K_GREATER]

        if keys[K_L]

        if keys[K_z]

        if keys[K_s]

rar = GameSprite('hfr ktdsq.png', 30, 300, 20, 30, 20)
ral = GameSprite( 'ракетка.png', 30, 300, 20, 30, 20)
ball = GameSprite('rjn.png', 30, 300, 20, 30, 10)

live = 3
       
while game:

    if not srite.collide_rect( rar, ball):
        live -= 1
        if live == 0:    
            sound1.play()
            display.update()
            lose.blit()
            time.delay(2000)
            break
    



    for e in pygame.event.get():
        if e.type == QUIT:
            game = False
    
    rar.update()      

    win.fill(225,0,55)
    clck.tick(60)
    win.blit()
    display.update()
