import pygame

pygame.init()
screen = pygame.display.set_mode([800,600])
timer = pygame.time.Clock()

run = True
while run:
   timer.tick(60)
   screen.fill('black')

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False

   pygame.display.flip()
pygame.quit()