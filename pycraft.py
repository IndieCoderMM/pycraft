from mesh_terrain import MeshTerrain

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
window.color = color.rgb(20, 100, 200)
indra = Sky()
indra.color = color.rgb(20, 100, 200)
subject = FirstPersonController()
subject.gravity = 0.0

terrain = MeshTerrain()

arm_texture = load_texture('assets/arm_texture.png')

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


hand = Hand()

def update():
    block_collide = False
    step = 2
    height = 1.5
    x = floor(subject.x+0.5)
    y = floor(subject.y+0.5)
    z = floor(subject.z+0.5)
    target = y + height
    for i in range(-step, step):
        if (x, y+i, z) in terrain.terrain_dict:
            target = y+i+height
            block_collide = True
            break
    if block_collide:
        subject.y = lerp(subject.y, target, 6*time.dt)
    else:
        subject.y -= 9.8 * time.dt


terrain.generate_terrain()
app.run()
