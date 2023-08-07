import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))        # flags=pygame.NOFRAME
pygame.display.set_caption("Pygame igra")
icon = pygame.image.load("icon/icon.png")
pygame.display.set_icon(icon)


running = True
while True:

    # screen.fill((219, 218, 213, 255))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                screen.fill((190, 38, 170))
