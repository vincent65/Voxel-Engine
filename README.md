# Voxel-Engine
This project was created to learn more about voxels and graphics rendering using PyGame

Traditional graphics rendering methods use triangles to create shapes and 3d objects because most traditional gpus are trained to handle trianlges and trianlges are also the simplest polygon that any other polygon can be divided into. Triangles are by far the easiest shape to compute (three dots in a single plane) and as a result are able to be made into many different complex shapes, making them extremely efficient. The math necessary to project a 2D triangle onto a screen is extremely straightforward. 

On the other hand, voxels, volumetric pixels, are essentially a 3-D pixel. Objects in voxel engines have actual volume because each voxel is a tiny point in 3D space. This makes voxels more similar to the real world as in the real world many different 3D particles make up more complex shapes. This makes voxel graphics good for modeling terrain. However unlike triangles, voxels are more difficult to compute as they are 3D and most graphics cards were designed to render triangles extremely efficiently leaving voxel development behind and lacking. 

This project utilizes Python and the Pygame, numba, and numpy libraries to implement ray casting. Ray casting is capable of transforming a limited form of data into a three-dimensional projection with the help of tracing rays from the view point into the viewing volume. The main principle behind ray casting is that rays can be cast and traced in groups based on certain geometric constraints. In ray casting, a ray from the pixel through the camera is obtained and the intersection of all objects in the picture is computed. Next, the pixel value from the closest intersection is obtained and is further set as the base for the projection. 

To run this project, simply clone or downlad this repositiory and run main.py

To interact with the environment, use the wasd keys to move around, q and e to adjust your height, and the arrow keys to adjust your view. 
![Screen Shot 2022-09-04 at 4 52 41 PM](https://user-images.githubusercontent.com/64037087/188333225-1284f5d2-afb3-4cc9-928f-ead4fef42f4c.jpg)
