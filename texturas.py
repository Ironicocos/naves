import pygame
import time
pygame.init()
height = pygame.display.Info().current_h
width = pygame.display.Info().current_w
ventana = pygame.display.set_mode((width, height))
gameState = True
platilloVolador = pygame.image.load('C:/Users/Aula/OneDrive/Desktop/python videojuegos/resources/platillo.png')
platilloVolador = pygame.transform.scale(platilloVolador, (100, 80))
posX = 980
posY = 1000
ventana.blit(platilloVolador, (posX, posY))
pygame.display.flip()
while gameState:
    
    keys = pygame.key.get_pressed()
    if keys [pygame.K_LEFT]:
        time.sleep(0.05)
        posX = posX - 30
        ventana.fill((0,0,0))
        ventana.blit(platilloVolador, (posX, posY))
        pygame.display.flip()
    if keys [pygame.K_RIGHT]:
        if posX > 1900:
            pass
        else:
            time.sleep(0.5)
            posX = posX + 30
            ventana.fill((0,0,0))
            ventana.blit(platilloVolador, (posX, posY))
            pygame.display.flip()
    if keys [pygame.K_DOWN]:
        if posY > 980:
            pass
        else:
            time.sleep(0.05)
            posY = posY + 30
            ventana.fill((0,0,0))
            ventana.blit(platilloVolador, (posX, posY))
            pygame.display.flip()
    if keys [pygame.K_UP]:
        if posY < 100:
            pass
        else:
            time.sleep(0.05)
            posY = posY - 30
            ventana.fill((0,0,0))
            ventana.blit(platilloVolador, (posX, posY))
            pygame.display.flip()    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameState = False
        
pygame.quit()