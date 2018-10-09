import numpy as np
import matplotlib.pyplot as plt
from perlin import *

colors = np.array([[156, 212, 226], [138, 181, 73], [95, 126, 48], [186, 140, 93]], dtype=np.uint8)

def plot(grid):
    image = colors[grid.reshape(-1)].reshape(grid.shape + (3,))
    plt.imshow(image)

if __name__ == '__main__':
	# Grid    
	n = 64
	grid = np.ones((n, n), dtype=np.int32)

	# Noise
	noise = generate_fractal_noise_2d((n, n), (1, 1), 6)
	noise = (noise - noise.min()) / (noise.max() - noise.min())

	# Water
	threshold = 0.3
	grid[noise < threshold] = 0

	# Trees
	potential = ((noise - threshold) / (1 - threshold))**4 * 0.7
	mask = (noise > threshold) * (np.random.rand(n, n) < potential)
	grid[mask] = 2

	# Dirt
	mask = (grid == 1) * (np.random.rand(n, n) < 0.05)
	grid[mask] = 3

	# Plot
	plt.subplot(131)
	plt.imshow(noise, cmap='gray')
	plt.subplot(132)
	plt.imshow((noise > threshold) * (((noise - threshold) / (1 - threshold))**4 * 0.7), cmap='jet')
	plt.subplot(133)
	plot(grid)
	plt.show()

