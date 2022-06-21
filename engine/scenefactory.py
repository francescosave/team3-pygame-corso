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
            else:
              raise Exception(f"Wrong component type: {componentDescriptor['type']}")
        
            actor.addComponent(component)

          scene.actors.append(actor)
          
        return scene
        
      except Exception as e:
          print(f"Error on filename: {fileName}")
          print(str(e))

  
  def saveSceneToFile(scene, fileName):
        with open(fileName, "w") as fileName:            
            scene_dict = dict()
            scene_dict["window"] = {"width":scene.windowRect.width, "height":scene.windowRect.height}
            scene_dict["actors"] = []
            for act in scene.actors:
                comp_list = []
                for comp in act.components:
                    if isinstance(comp,StaticSpriteComponent):
                        comp_list.append({"name":comp.name,"type":"StaticSpriteComponent","fileName":comp.assetFileName})
                    elif isinstance(comp,BouncingMovementComponent):
                        boundingRect_dict = {"x":comp.boundingRect.x, "y":comp.boundingRect.y,
                                            "width":comp.boundingRect.width,"height":comp.boundingRect.height}
                        comp_list.append({"name":comp.name,"type":"BouncingMovementComponent","vx":comp.vx, "vy":comp.vy, "boundingRect":boundingRect_dict})
                    elif isinstance(comp,CircleMovementComponent):
                        comp_list.append({"name":comp.name,"type":"CircleMovementComponent",
                                         "center_x":comp.center_x, "center_y":comp.center_y, "radius":comp.radius})
                    elif isinstance(comp, SinusoidalMovementComponent):
                        comp_list.append({"name":comp.name,"type":"SinusoidalMovementComponent","amp":comp.amp, "vx":comp.vx})
                    else:
                        raise Exception(f"Wrong component: {comp.name}")
                scene_dict["actors"].append({"name":act.name, "x":act.x, "y": act.y, "components":comp_list})
        
            json.dump(scene_dict, fileName, indent=4)