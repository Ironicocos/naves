import pygame
pygame.init()
height = pygame.display.Info().current_h
width = pygame.display.Info().current_w
ventana = pygame.display.set_mode((width, height))
gameState = True
pygame.mixer.music.load('C:/Users/Aula.DESKTOP-CTQAC9H/Desktop/python/resources/The Last Mariachi.mp3')
uh = pygame.mixer.Sound('C:/Users/Aula.DESKTOP-CTQAC9H/Desktop/python/resources/oof.wav')
volumen = pygame.mixer.music.get_volume()
pygame.mixer.music.set_volume(0.5)
while gameState:
    volumeCount = volumen
    print(volumen)
    print(pygame.mixer.music.get_busy())
    print(volumeCount)
    keys = pygame.key.get_pressed()
    if keys [pygame.K_SPACE]:
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.unpause()
        elif pygame.mixer.music.get_busy() == True:
            pygame.mixer.music.pause()
    if keys [pygame.K_1]:
        pygame.mixer.music.play()
    if keys [pygame.K_0]:
        uh.play()
    if keys [pygame.K_UP]:
        volumeCount += 0.1
        pygame.mixer.music.set_volume(volumen)
        """
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
        """
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameState = False
        
pygame.quit()