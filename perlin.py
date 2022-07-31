from perlin_noise import PerlinNoise

class Perlin:
    def __init__(self):
        self.seed = 123
        self.octaves = 2
        self.freq = 64
        self.amp = 12
        self.perlin_noise = PerlinNoise(seed=self.seed, octaves=self.octaves)

    def get_height(self, x, z):
        y = self.perlin_noise([x/self.freq, z/self.freq]) * self.amp
        return y
