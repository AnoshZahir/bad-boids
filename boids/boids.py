from matplotlib import pyplot as plt
from matplotlib import animation
import random

class Boids(object):

    def __init__(self): 
        boids_x = self.generate_random_uniform(-450,50.0, 50)
        boids_y = self.generate_random_uniform(300.0,600.0, 50)
        boid_x_velocities = self.generate_random_uniform(0, 10.0, 50)
        boid_y_velocities = self.generate_random_uniform(-20.0, 20.0, 50)
        self.boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)
        
            
    def generate_random_uniform(self, start, end, number):
        return [random.uniform(start, end) for x in range(number)]

    def update_boids(self, boids):
	xs,ys,xvs,yvs=boids
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
         self.scatter = axes.scatter(self.boids[0],self.boids[1])
         anim = animation.FuncAnimation(figure, self.animate, frames=50, interval=50)
         plt.show()

    def animate(self, frame):
        self.update_boids(self.boids)
        self.scatter.set_offsets(zip(self.boids[0],self.boids[1]))



if __name__ == "__main__":
    boids = Boids()
    boids.run_simulation()
   