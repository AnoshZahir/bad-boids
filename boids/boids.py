from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

class Boids(object):

    def __init__(self, no_of_boids = 50, position_limits = [-450, 300, 50, 600],
        velocity_limits = [0, -20, 10, 20], move_to_middle_strength = 0.01,
        alert_distance = 100, formation_flying_distance = 10000,
        formation_flying_strength = 0.125):
        self.no_of_boids = no_of_boids
        self.positions = self.new_flock(self.no_of_boids, np.array(position_limits[0:2]), np.array(position_limits[2:4]))
        self.velocities = self.new_flock(self.no_of_boids, np.array(velocity_limits[0:2]), np.array(velocity_limits[2:4]))
        self.move_to_middle_strength = move_to_middle_strength
        self.alert_distance = alert_distance
        self.formation_flying_distance = formation_flying_distance
        self.formation_flying_strength = formation_flying_strength
    
    def new_flock(self, no_of_boids, lower_limits, upper_limits):
        width = upper_limits - lower_limits
        return (lower_limits[:, np.newaxis] + np.random.rand(2,no_of_boids)*width[:, np.newaxis])
      
    def update_boids(self, positions, velocities):
        separations, square_distances = self.squared_distance(positions)
        self.fly_towards_the_middle(positions, velocities)
        self.fly_away_from_nearby_boids(positions, velocities, separations, square_distances)
        self.match_speed_with_nearby_boids(positions, velocities, square_distances)
        positions += velocities # Move according to velocities
        
    # Fly towards the middle
    def fly_towards_the_middle(self, positions, velocities):
        middle = np.mean(positions, 1)
        direction_to_middle = positions - middle[:, np.newaxis]
        velocities -= direction_to_middle * self.move_to_middle_strength


    #calculates the separation and squared distance from nearby boids
    def squared_distance(self, positions):
        separations = positions[:, np.newaxis, :] - positions[:, :, np.newaxis]
        squared_displacements = separations * separations
        square_distances = np.sum(squared_displacements, 0)
        return separations, square_distances
        
    # Fly away from nearby boids
    def fly_away_from_nearby_boids(self, positions, velocities, separations, square_distances):
        far_away = square_distances > self.alert_distance
        separations_if_close = np.copy(separations)
        separations_if_close[0,:,:][far_away] = 0
        separations_if_close[1,:,:][far_away] = 0
        velocities += np.sum(separations_if_close,1)
        
	# Try to match speed with nearby boids
    def match_speed_with_nearby_boids(self, positions, velocities, square_distances):
        velocity_differences = velocities[:,np.newaxis,:] - velocities[:,:,np.newaxis]
        very_far=square_distances > self.formation_flying_distance
        velocity_differences_if_close = np.copy(velocity_differences)
        velocity_differences_if_close[0,:,:][very_far] = 0
        velocity_differences_if_close[1,:,:][very_far] = 0
        velocities -= np.mean(velocity_differences_if_close, 1) * self.formation_flying_strength

    def run_simulation(self,xlim=(-500,1500), ylim=(-500,1500), frames=50, interval=50):
         figure = plt.figure()
         axes = plt.axes(xlim = xlim, ylim = ylim)
         self.scatter = axes.scatter(self.positions[0,:], self.positions[1, :])
         anim = animation.FuncAnimation(figure, self.animate, frames = frames, interval = interval)
         plt.show()

    def animate(self, frame):
        self.update_boids(self.positions, self.velocities)
        self.scatter.set_offsets(zip(self.positions.transpose()))

if __name__ == "__main__":
    boids = Boids()
    boids.run_simulation()
   