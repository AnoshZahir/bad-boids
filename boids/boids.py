from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

class Boids(object):

    def __init__(self, no_of_boids = 50):
        self.no_of_boids = no_of_boids
        self.positions = self.new_flock(self.no_of_boids, np.array([-450, 300]), np.array([50,600]))
        self.velocities = self.new_flock(self.no_of_boids, np.array([0, -20]), np.array([10,20]))
        #self.boids = (self.positions, self.velocities)    
    
    def new_flock(self, no_of_boids, lower_limits, upper_limits):
        width = upper_limits - lower_limits
        return (lower_limits[:, np.newaxis] + np.random.rand(2,no_of_boids)*width[:, np.newaxis])
      
    def update_boids(self, positions, velocities):
        separations, square_distances = self.squared_distance(positions)
        self.fly_towards_the_middle(positions, velocities)
        self.fly_away_from_nearby_boids(positions, velocities, separations, square_distances)
        self.match_speed_with_nearby_boids(positions, velocities, square_distances)
	# Move according to velocities
        positions += velocities
        
    # Fly towards the middle
    def fly_towards_the_middle(self, positions, velocities, move_to_middle_strength = 0.01):
        middle = np.mean(positions, 1)
        direction_to_middle = positions - middle[:, np.newaxis]
        velocities -= direction_to_middle * move_to_middle_strength


    #determine squared distance from nearby boids
    def squared_distance(self, positions):
        separations = positions[:, np.newaxis, :] - positions[:, :, np.newaxis]
        squared_displacements = separations * separations
        square_distances = np.sum(squared_displacements, 0)
        return separations, square_distances
        
    # Fly away from nearby boids
    def fly_away_from_nearby_boids(self, positions, velocities, separations, square_distances, alert_distance = 100):
        far_away = square_distances > alert_distance
        separations_if_close = np.copy(separations)
        separations_if_close[0,:,:][far_away] = 0
        separations_if_close[1,:,:][far_away] = 0
        velocities += np.sum(separations_if_close,1)
        
	# Try to match speed with nearby boids
    def match_speed_with_nearby_boids(self, positions, velocities, square_distances, formation_flying_distance = 10000, formation_flying_strength = 0.125):
        velocity_differences = velocities[:,np.newaxis,:] - velocities[:,:,np.newaxis]
        very_far=square_distances > formation_flying_distance
        velocity_differences_if_close = np.copy(velocity_differences)
        velocity_differences_if_close[0,:,:][very_far] = 0
        velocity_differences_if_close[1,:,:][very_far] = 0
        velocities -= np.mean(velocity_differences_if_close, 1) * formation_flying_strength

    def run_simulation(self,xlim=(-500,1500), ylim=(-500,1500), frames=50, interval=50):
         figure = plt.figure()
         axes = plt.axes(xlim, ylim)
         self.scatter = axes.scatter(self.positions[0,:], self.positions[1, :])
         anim = animation.FuncAnimation(figure, self.animate, frames, interval)
         plt.show()

    def animate(self, frame):
        self.update_boids(self.positions, self.velocities)
        self.scatter.set_offsets(zip(self.positions.transpose()))

if __name__ == "__main__":
    boids = Boids()
    boids.run_simulation()
   