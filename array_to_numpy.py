import numpy as np
from PIL import Image

# Create a 3D numpy array of zeroes, then replace zeros with yellow pxls
data = np.zeros((5,4,3), dtype=np.uint8)
data[:] = [255,255,0] # replace with yellow pixels

# Make a red patch rows
# data[1:3] = [255,0,0]

# Make a red patch columns
data[0:3,1:3] = [255,0,0]
print(data)

image = Image.fromarray(data, "RGB")
image.save('canvas.png')

