from ursina import *
from random import randint
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
grass_texture = load_texture ('assets/Grass_block.png')
stone_texture = load_texture ('assets/Stone_block.png')
brick_texture = load_texture ('assets/Brick_block.png')
dirt_texture = load_texture ('assets/Dirt_block.png')
sky_texture = load_texture ('assets/Skybox.png')
arm_texture = load_texture ('assets/Arm_texture.png')
block_pick = 1
minecraft_soundtrack = Audio('assets/minecraft_soundtrack',loop = True, autoplay = True)
Terra_soundtrack = Audio('assets/terra',Loop = False, Autoplay = False)
Madeira_soundtrack = Audio('assets/madeira',Loop = False, autoplay = False)
Pedra_soundtrack = Audio('assets/pedra', Loop = False, autoplay = False)

def update():
    global block_pick
   
    if held_keys['left mouse'] or held_keys ['right mouse']:
        hand.active()
    else:
        hand.passive()

            
    
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['f3']:window.fps_counter.enabled = False
    if held_keys['f4']:window.fps_counter.enabled = True
    if held_keys['f3']:window.exit_button.visible = False
    if held_keys['f4']:window.exit_button.visible = True


    




class Voxel(Button):
    def __init__(self, position = (0,0,0),texture = grass_texture):
       super().__init__(
           parent = scene,
           position = position,
           model= 'assets/block',
           origin_y = 0.5,
           texture = texture,
           color = color.color(0,0,0.9),
           highlight_color = color.color(0,0,2),
           scale = 0.5
           )

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture,)
                if block_pick == 1: voxel = Terra_soundtrack.play()
                if block_pick == 2: voxel = Pedra_soundtrack.play()
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                if block_pick == 3: voxel = Madeira_soundtrack.play()
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
                if block_pick == 4: voxel = Terra_soundtrack.play()
           
            if key == 'right mouse down':
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True)

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/arm',
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.4,-0.6))
    
    def active(self):
        self.position = Vec2(0.3,-0.5)
    def passive(self):
        self.position = Vec2(0.4,-0.6)




zaxis = 0
zaxis2 = 0
for i in range(30):
    chance = random.randint(0, 5)
    if chance == 1:
        zaxis += 1
    if chance == 2:
        zaxis -= 1
    for j in range(30):
        zaxis2 = zaxis
        voxel = Voxel(position = (j,zaxis,i))
        for a in range(0,2):
            zaxis2 -= 1
            voxel = Voxel(position = (j,zaxis2,i))

player = FirstPersonController()
print("Tenho prova hoje")
sky = Sky()
hand = Hand()
app.run()

