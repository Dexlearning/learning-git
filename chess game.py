import pygame

pygame.init()
width = 1000
height = 768
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('chess')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60

white_pieces = ['rook','knight','bishop','king','queen','rook','knight','bishop',
                'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']

white_locations = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),
                   (8,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]

black_pieces = ['rook','knight','bishop','king','queen','rook','knight','bishop',
                'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']

black_locations = [(8,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),
                   (8,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]

captured_pieces_white = []
captured_pieces_black = []

turn_step = 0
selection = 100
valid_moves = []


run = True
while run:
   timer.tick(fps)
   screen.fill('dark gray')

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False

   pygame.display.flip()
pygame.quit()