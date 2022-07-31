from ursina import *
from perlin import Perlin

class MeshTerrain:
    def __init__(self):
        self.subsets = []
        self.block = load_model('assets/models/block.obj')
        self.texture_atlas = 'assets/textures/texture_atlas_3.png'
        self.total_subsets = 1
        self.sub_width = 64
        self.terrain_dict = {}
        self.perlin = Perlin()

        for i in range(self.total_subsets):
            e = Entity(model=Mesh(), texture=self.texture_atlas)
            e.texture_scale *= 64/e.texture.width
            self.subsets.append(e)

    def generate_terrain(self):
        x = 0
        z = 0
        for k in range(-self.sub_width//2, self.sub_width//2):
            for j in range(-self.sub_width//2, self.sub_width//2):
                y = floor(self.perlin.get_height(x+k, z+j))
                self.create_block(x+k, y, z+j)
        self.subsets[0].model.generate()

    def create_block(self, x, y, z):
        # triangle + triangle = cube
        # 36 vertices
        model = self.subsets[0].model
        model.vertices.extend([Vec3(x, y, z) + v for v in self.block.vertices])
        self.terrain_dict[(x, y, z)] = True
        tile_x = 8
        tile_y = 7
        if y > 2:
            tile_x = 8
            tile_y = 6
        model.uvs.extend([Vec2(tile_x, tile_y) + u for u in self.block.uvs])
        # model.generate()

