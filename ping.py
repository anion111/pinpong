import pygame 
pygame.init()


win = display_mode((500,500))
clck = pygame.time.clock()
game = True

while game:
    for e in pygame.event.get():
        if e.type == QUIT:
            game = False
            
    win.fill(225,0,55)
    clck.tick(60)
    pygame.display.update()