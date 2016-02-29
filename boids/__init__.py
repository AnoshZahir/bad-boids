from boids import Boids
from argparse import ArgumentParser
import ConfigParser
import json

def main():
    
    parser = ArgumentParser(description = "A simulation of a flock of birds.")
    parser.add_argument('--config', '-c', default = 'config.cfg', help = 'select config file')
    arguments = parser.parse_args()

    config = ConfigParser.ConfigParser()
    with open(arguments.config) as config_file:
        config.readfp(config_file)
        no_of_boids = config.getint('boids_initiate', 'no_of_boids')
        position_limits =  json.loads(config.get('boids_initiate', 'position_limits'))
        velocity_limits =  json.loads(config.get('boids_initiate', 'velocity_limits'))
        move_to_middle_strength = config.getfloat('boids_initiate', 'move_to_middle_strength')
        alert_distance = config.getfloat('boids_initiate', 'alert_distance')
        formation_flying_distance = config.getfloat('boids_initiate', 'formation_flying_distance')
        formation_flying_strength = config.getfloat('boids_initiate', 'formation_flying_strength')

        xlim = json.loads(config.get('run_simulation','xlim'))
        ylim = json.loads(config.get('run_simulation', 'ylim'))
        frames = config.getint('run_simulation', 'frames')
        interval = config.getint('run_simulation', 'interval')
            
        boids = Boids(no_of_boids = no_of_boids, position_limits = position_limits,
            velocity_limits = velocity_limits,
            move_to_middle_strength = move_to_middle_strength,
            alert_distance = alert_distance,
            formation_flying_distance = formation_flying_distance,
            formation_flying_strength = formation_flying_strength)
    
        boids.run_simulation(xlim = tuple(xlim), ylim = tuple(ylim), frames = frames,
                          interval = interval)