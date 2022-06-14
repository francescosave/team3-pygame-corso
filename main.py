import pygame,sys
from pygame.locals import *
from engine.Scene import *
from engine.Actor import *
from engine.Component import *

pygame.init()

scene = Scene()
scene.render()

Quit = False


height = 500
width = 1200
window = pygame.display.set_mode((height,width))

def process_event():
  global Quit
  for event in pygame.event.get():
    if event.type == QUIT:
      Quit=True
  
def game_logic_update():
  pass

def render():
  pass  


#game Loop

while not Quit:
  process_event()
  game_logic_update()
  render()

pygame.quit()
sys.exit()


