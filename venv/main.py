import pygame

pygame.init()
screen = pygame.display.set_mode((1080, 920))        # flags=pygame.NOFRAME
pygame.display.set_caption("Pygame igra")
icon = pygame.image.load("icon/icon.png")
pygame.display.set_icon(icon)

square = pygame.Surface((50, 170))
square.fill('Blue')

myfont = pygame.font.Font('fonts/fonts.ttf', 35)
text_surface = myfont.render('itProger', True, 'Red')

player = pygame.image.load("icon/icon.png")

running = True
while True:

    pygame.draw.circle(square, 'Red', (10, 5), 20)

    screen.blit(square, (100, 0))
    screen.blit(text_surface, (300, 100))
    screen.blit(player, (100, 50))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
