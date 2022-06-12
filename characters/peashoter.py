class PeaShooter(Plant):

    def __init__(self):
        super().__init__(health=100, cost=100)
        self.texture = arcade.load_texture("./pea1.png")
        for i in range(2):
            self.textures.append(arcade.load_texture("./pea1.png"))
        for i in range(2):
            self.textures.append(arcade.load_texture("./pea2.png"))
        for i in range(2):
            self.textures.append(arcade.load_texture("./pea3.png"))

        self.pea_spawn = time.time()


    def update(self):
        super().update()
        zombie_on_line = False
        for zombie in window.zombies:
            if(zombie.line == self.line):
                zombie_on_line = True
        if(time.time() - self.pea_spawn >= 2 and zombie_on_line):
            pea = Pea(self.center_x + 10, self.center_y + 10)
            window.peas.append(pea)
            self.pea_spawn = time.time()
