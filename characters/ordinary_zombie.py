import sys
sys.path.append("..")

import settings
from .zombie import Zombie
from arcade import load_texture

IMAGES = settings.IMAGES

class OrdinaryZombie(Zombie):
    def __init__(self, line, position):
        super().__init__(health=12, line=line, center_x=position)
        self.texture = load_texture(IMAGES + "zom1.png")
        for i in range(5):
            self.textures.append(load_texture(IMAGES + "zom1.png"))
        self.textures.append(load_texture(IMAGES + "zom2.png"))
