from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

class Boids(object):

    def __init__(self, no_of_boids = 50):
        self.no_of_boids = no_of_boids
        self.positions = self.new_flock(self.no_of_boids, np.array([-450, 300]), np.array([50,600]))
        self.velocities = self.new_flock(self.no_of_boids, np.array([0, -20]), np.array([10,20]))
                
    def new_flock(self, no_of_boids, lower_limits, upper_limits):
        width = upper_limits - lower_limits
        return (lower_limits[:, np.newaxis] + np.random.rand(2,no_of_boids)*width[:, np.newaxis])
        
    def update_boids(self, positions, velocities):
	xs,ys = positions
	xvs,yvs= velocities
	# Fly towards the middle
	for i in range(len(xs)):
		for j in range(len(xs)):
			xvs[i]=xvs[i]+(xs[j]-xs[i])*0.01/len(xs)
	for i in range(len(xs)):
		for j in range(len(xs)):
			yvs[i]=yvs[i]+(ys[j]-ys[i])*0.01/len(xs)
	# Fly away from nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100:
				xvs[i]=xvs[i]+(xs[i]-xs[j])
				yvs[i]=yvs[i]+(ys[i]-ys[j])
	# Try to match speed with nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
				xvs[i]=xvs[i]+(xvs[j]-xvs[i])*0.125/len(xs)
				yvs[i]=yvs[i]+(yvs[j]-yvs[i])*0.125/len(xs)
	# Move according to velocities
	for i in range(len(xs)):
		xs[i]=xs[i]+xvs[i]
		ys[i]=ys[i]+yvs[i]

    def run_simulation(self):
         figure = plt.figure()
         axes = plt.axes(xlim=(-500,1500), ylim=(-500,1500))
         self.scatter = axes.scatter(self.positions[0,:], self.positions[1, :])
         anim = animation.FuncAnimation(figure, self.animate, frames=50, interval=50)
         plt.show()

    def animate(self, frame):
        self.update_boids(self.positions, self.velocities)
        self.scatter.set_offsets(zip(self.positions.transpose()))

if __name__ == "__main__":
    boids = Boids()
    boids.run_simulation()