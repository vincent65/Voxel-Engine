
#The overall game loop

import pygame as pg
from player import Player
from voxel_renderer import VoxelRenderer



class App:
    def __init__(self):
        self.res = self.width, self.height = (800, 450)
        #we can double the ressolution with pg.SCALED but at the hardware level; this will save us resources in further calculations
        self.screen = pg.display.set_mode(self.res, pg.SCALED)
        self.clock = pg.time.Clock()
        self.player = Player()
        self.voxelRenderer = VoxelRenderer(self)

    def update(self):
        self.player.update();
        self.voxelRenderer.update();
        
    
    def draw(self):
        self.voxelRenderer.draw();
        pg.display.flip();
        
    
    def run(self):
        while True:
            self.update()
            self.draw()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick(60)
            pg.display.set_caption(f'FPS: {self.clock.get_fps()}')



if __name__ == '__main__':
    app = App();
    app.run();