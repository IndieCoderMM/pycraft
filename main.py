from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

game = Ursina()
sky_texture = load_texture('assets/skybox.png')
grass_texture = load_texture('assets/grass_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
stone_texture = load_texture('assets/stone_block.png')
arm_texture = load_texture('assets/arm_texture.png')
punch_sound = Audio('assets/assets_punch_sound.wav', loop=False, autoplay=False)

block_textures = [grass_texture, dirt_texture, stone_texture, brick_texture]
block_selection = 0

window.exit_button.visible = False

def update():
    global block_selection
    if held_keys['1']:
        block_selection = 0
    if held_keys['2']:
        block_selection = 1
    if held_keys['3']:
        block_selection = 2
    if held_keys['4']:
        block_selection = 3
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture,
            scale=150,
            double_sided=True
        )

class Voxel(Button):
    def __init__(self, pos=(0, 0, 0), tex=grass_texture):
        super().__init__(
            parent=scene,
            position=pos,
            model='assets/block',
            origin_y=0.5,
            texture=tex,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color=color.lime,
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                block_texture = block_textures[block_selection]
                voxel = Voxel(pos=self.position+mouse.normal, tex=block_texture)
            elif key == 'right mouse down':
                punch_sound.play()
                destroy(self)


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='assets/arm',
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6)
        )

    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)


for z in range(8):
    for x in range(8):
        voxel = Voxel((x, 0, z))

player = FirstPersonController()
sky = Sky()
hand = Hand()
game.run()
