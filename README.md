# Voxel-Engine
This project was created to learn more about voxels and graphics rendering using PyGame

Traditional graphics rendering methods use triangles to create shapes and 3d objects because most traditional gpus are trained to handle trianlges and trianlges are also the simplest polygon that any other polygon can be divided into. Triangles are by far the easiest shape to compute (three dots in a single plane) and as a result are able to be made into many different complex shapes, making them extremely efficient. The math necessary to project a 2D triangle onto a screen is extremely straightforward. 

On the other hand, voxels, volumetric pixels, are essentially a 3-D pixel. Objects in voxel engines have actual volume because each voxel is a tiny point in 3D space. This makes voxels more similar to the real world as in the real world many different 3D particles make up more complex shapes. This makes voxel graphics good for modeling terrain. However unlike triangles, voxels are more difficult to compute as they are 3D and most graphics cards were designed to render triangles extremely efficiently leaving voxel development behind and lacking. 
