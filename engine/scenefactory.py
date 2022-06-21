import json
from engine.scene import *
from engine.component import *
from engine.actor import *
from engine.staticspritecomponent import *
from engine.bouncingmovementcomponent import *
from engine.circlemovementcomponent import *
from engine.sinusoidalmovementcomponent import *
from pygame import rect

class SceneFactory:

  def loadSceneFromFile(fileName):
    with open(fileName, "r") as f:
      try:
        sceneDescriptor = json.load(f)

        scene = Scene()
        windowDescriptor = sceneDescriptor["window"]
        scene.windowRect.height = windowDescriptor["height"]
        scene.windowRect.width = windowDescriptor["width"]

        for actorDescriptor in sceneDescriptor["actors"]:
          actor = Actor()
          actor.name = actorDescriptor["name"]
          actor.x = actorDescriptor["x"]
          actor.y = actorDescriptor["y"]

          for componentDescriptor in actorDescriptor["components"]:
            component = None
            if componentDescriptor["type"] == StaticSpriteComponent.__name__:
              component = StaticSpriteComponent(componentDescriptor["fileName"])
            elif componentDescriptor["type"] == BouncingMovementComponent.__name__:
              rectDescriptor = componentDescriptor["boundingRect"]
              r = rect.Rect(rectDescriptor["x"], rectDescriptor["y"], rectDescriptor["width"], rectDescriptor["height"])
              component = BouncingMovementComponent(r)
              component.vx = componentDescriptor["vx"] # <----------------------------
              component.vy = componentDescriptor["vy"] # <----------------------------
            elif componentDescriptor["type"] == CircleMovementComponent.__name__:
              radius = componentDescriptor["radius"]
              center_x = componentDescriptor["center_x"]
              center_y = componentDescriptor["center_y"]
              component = CircleMovementComponent(radius,center_x, center_y)
            elif componentDescriptor["type"] == SinusoidalMovementComponent.__name__:
              component = SinusoidalMovementComponent()
              component.amp = componentDescriptor["amp"]
              component.vx = componentDescriptor["vx"]
              component.angle = componentDescriptor["angle"]
            else:
              raise Exception(f"Wrong component type: {componentDescriptor['type']}")
            actor.addComponent(component)

          scene.actors.append(actor)
          
        return scene
        
      except Exception as e:
          print(f"Error on filename: {fileName}")
          print(str(e))

  


  def saveSceneFromFileJson(self,scene,fileName):

    with open(fileName, "w") as file:
      try:
        json.dump(scene.getDisctionary(), file, indent = 4)
      except Exception as e:
        print(f"Error on filename: {fileName}")
        print(str(e))