import pygame,sys, pygame.locals
from engine.scene import *
from engine.actor import *
from engine.component import *
from engine.bouncingmovementcomponent import *
from engine.staticspritecomponent import *
from engine.scenefactory import *
from save_scene import *


s = SaveScene()
s.Save()

pygame.init()

Quit = False

scene = SceneFactory.loadSceneFromFile("example_bk.json")
window = pygame.display.set_mode((scene.windowRect.width, scene.windowRect.height),0,32)
pygame.display.set_caption("I cavalieri dell'apocalisse")
scene.load()

def process_event():
  global Quit
  for event in pygame.event.get():
    if event.type == pygame.locals.QUIT:
      Quit=True
  
def game_logic_update():
  global scene 
  scene.update()
  return
  
def render():
  global scene

  BLACK = (0, 0, 0)
  WHITE = (255, 255, 255)

  window.fill(BLACK)
  scene.render(window)
  pygame.display.update()


#game Loop

while not Quit:
  process_event()
  game_logic_update()
  render()

pygame.quit()
sys.exit()



