from engine.scenefactory import *

class SaveScene:

    def Save(self):

        scene = Scene()
        scene.windowRect.width = 500
        scene.windowRect.height = 700

        ssc_act1 = StaticSpriteComponent("assets/ghost1.png")
        ssc_act1.name = "sprite"
        r1 = rect.Rect(100,100,400,500)
        bmc_act1 = BouncingMovementComponent(r1)
        bmc_act1.name = "bouncing"

        act1 = Actor()
        act1.name = "Blinky"
        act1.x = 0
        act1.y = 0
        act1.addComponent(ssc_act1)
        act1.addComponent(bmc_act1)

        ssc_act2 = StaticSpriteComponent("assets/ghost2.png")
        ssc_act2.name = "sprite"
        cmc_act2 = CircleMovementComponent(250,500,300)
        cmc_act2.name = "circle1"
        
        act2 = Actor()
        act2.name = "Clyde_vulnerable"
        act2.x = 0
        act2.y = 0
        act2.addComponent(ssc_act2)
        act2.addComponent(cmc_act2)



        ssc_act3 = StaticSpriteComponent("assets/ghost3.png")
        ssc_act3.name = "sprite"
        smc_act3 = SinusoidalMovementComponent()
        smc_act3.name = "sinusoidal1"
        smc_act3.amp = 100
        smc_act3.vx = 0.01
        smc_act3.angle = 250

        act3 = Actor()
        act3.name = "Inky_vulnerable"
        act3.x = 0
        act3.y = 0
        act3.addComponent(ssc_act3)
        act3.addComponent(smc_act3)


        scene.actors.append(act1)
        scene.actors.append(act2)
        scene.actors.append(act3)


        # save to file json
        scenefact = SceneFactory()
        scenefact.saveSceneFromFileJson(scene,"save_example.json")
        print("SAVE TO FILE save_example.json")
                  