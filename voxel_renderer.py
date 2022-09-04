import pygame as pg
from numba import njit
import numpy as np
import math


#landscape
height_map_img = pg.image.load('img/height_map.jpg')
height_map = pg.surfarray.array3d(height_map_img)

#color generation
color_map_img = pg.image.load('img/color_map.jpg')
color_map = pg.surfarray.array3d(color_map_img)

map_height = len(height_map[0])
map_width = len(height_map)


#raycasting is resource intensive, which is why the ray casting function is defiend outside the class, allowing great performance increase
@njit(fastmath=True)
def ray_casting(screen_array, player_pos, player_angle, player_height, player_pitch,
                     screen_width, screen_height, delta_angle, ray_distance, h_fov, scale_height):
    screen_array[:] = np.array([0,0,0])
    
    return screen_array

class VoxelRenderer:
    
    def __init__(self, app):
        self.app = app
        self.player = app.player
        self.fov = math.pi / 3
        self.h_fov = self.fov / 2
        self.num_rays = app.width
        #angle between rays
        self.delta_angle = self.fov / self.num_rays
        self.ray_distance = 2000 #ray legnth
        self.scale_height = 620 #scale factor
        #3D array to store rgb values and display images
        self.screen_array = np.full((app.width, app.height, 3), (0,0,0))

    def update(self):
        self.screen_array = ray_casting(self.screen_array, self.player.pos, self.player.angle,
                                        self.player.height, self.player.pitch, self.app.width,
                                        self.app.height, self.delta_angle, self.ray_distance,
                                        self.h_fov, self.scale_height)

    def draw(self):
        self.app.screen.blit(pg.surfarray.make_surface(self.screen_array), (0,0))
