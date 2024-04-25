from pygame import* 

from random import*


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



font.init()
font1 = font.Font(None, 80)
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






rar = Player('hfr ktdsq.png', 450, 300, 20, 30, 20)
ral = Player( 'ракетка.png', 30, 300, 80, 30, 20)
ball = GameSprite("r.png", 90, 200, 60, 30, 10)

while game:

    for i in range(len(text)-1):
        let = font1.render(text[i], True, (colors[1]))

    for i in range(len(text1)-1):
        lett = font1.render(text1[i], True, (colors[1]))

    
    if finish != True:
        ball.rect.x += speedX
        ball.rect.y += speedY

        if ball.rect.y >= 450-50  or ball.rect.y <= 0:
            speedY *= -1



        if sprite.collide_rect(rar, ball) or sprite.collide_rect(ral, ball):
            speedX *= -1


    for e in event.get():
        if e.type == QUIT:
            game = False


    if ball.rect.x >= 500 or ball.rect.x >= 0:
        ball.reset(50,50)
        live -= 1  
        if live == 0:    
            lett.blit()
            time.delay(2000)
            break


    win.blit(let, (200, 200))
    win.fill((255, 192, 203))
    ball.reset()
    rar.update()      
    rar.reset()
    ral.update1()
    ral.reset()
    clck.tick(60)
        # win.blit()
    display.update()
