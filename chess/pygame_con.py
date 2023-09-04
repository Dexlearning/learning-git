import pygame

pygame.init()
screen = pygame.display.set_mode([1000,600])
screen_rect = screen.get_rect()
timer = pygame.time.Clock()

#ตัวแปรต่างๆ
green = (0,255,0)

#ภาพ




#run control
clicked = False
screen_obj_start = True
run = True
run2 = False

# class click image
class Click_image:
   def __init__(self):
      self.clicked = False
      king = pygame.image.load('images/black king.png')
      self.king = pygame.transform.scale(king, (80,80))
      self.king_rect = self.king.get_rect()
      rook = pygame.image.load('images/black rook.png')
      self.rook = pygame.transform.scale(rook, (80,80))
      self.rook_rect = self.rook.get_rect()
      pawn = pygame.image.load('images/black pawn.png')
      self.pawn = pygame.transform.scale(pawn, (80,80))
      self.pawn_rect = self.pawn.get_rect()
      white_locations = [(50, 50), (200, 50), (300, 50), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
      self.king_rect.center = white_locations[0]
      self.rook_rect.center = white_locations[1]
      self.pawn_rect.center = white_locations[2]

   def click(self, event):  # เพิ่มพารามิเตอร์ event
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if self.king_rect.collidepoint(event.pos):
               self.clicked = not self.clicked               

            if self.clicked:
               self.king_rect.center = event.pos
               pygame.draw.rect(screen, green,self.king_rect,2)

   def update(self):
      
      screen.blit(self.king, self.king_rect)
      screen.blit(self.rook, self.rook_rect)
      screen.blit(self.pawn, self.pawn_rect)

#class ประกาศ
cimage = Click_image()

while run:
   timer.tick(60)
   screen.fill('black')
   
   #control
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False
      

      cimage.click(event)
   # อัพเดทรูปวาด
   cimage.update()      


   pygame.display.flip()
pygame.quit()