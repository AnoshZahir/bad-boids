Bad_boids package
=================
This library creates a simulation of a flock of birds.  A number of parameters can be changed to see how the behavior of the flock alters.

### Background
This library is created as an exercise in refactoring.  The original code is located here:  https://github.com/jamespjh/bad-boids.git.  The model is based on 'flocks, herds and schools: a distributed behavioral model' by Craig W Reynolds. 

### How to install
* Pip install:
    * pip install git+https://github.com/AnoshZahir/bad_boids.git

* Alternavtively
    * download the package
    * Go to the package's root directory using the command line
    * Depeding on your machine:
        * Windows: python setup.py install
        * Mac/other: sudo python setup.py install

The package will now be installed and ready to use.

### How to use
Below is an example of how to use the command line:
 * bad_boids --config your_config_file_here.
 * Note that '-c' can be used as a shortcut for '--config'.
 * As a default, 'config.cfg' will be loaded if no config file is specified.  Details of that file are in the next section.

### Config file
 * The default config file 'config.cfg' has the following parameters:
    * Section: boids_initiate.  This is where the number of boids, their positions and velocities as well as dynamics of the flock behavior are set.
        * no_of_boids = 50. Set the number of boids in the simulation.
        * position_limits = [-450, 300, 50, 600]. Set the boundaries within which each boid will take an initial position.
        * velocity_limits = [0, -20, 10, 20]. Set the boundaries within which each boid will take an initial velocity.
        * move_to_middle_strength = 0.01. Model is designed for the birds to move to the centre of the flock.  This is the strength of their tendency to do so.
        * alert_distance = 100. Maximum distance a bird can be from another before it moves towards the flock centre.
        * formation_flying_distance = 10000.  The range within which birds can move away from the main flock.
        * formation_flying_strength = 0.125.  How tightly should the flock fly together.
* Section: run_simulation.  This is where the parameters of the simulation are set.
        * xlim = [-500,1500]. The limts of the plot's x axis.
        * ylim = [-500,1500]. The limts of the plot's x axis.
        * frames = 50. The number of frames in the simulation.
        * interval = 50.  How long between each frame.

* Each parameter is set a default value, which have the following implications:
    * The parameter's default value is used if one is not given in the config file.  However, note that any config file must be formatted to contain the two sections 'boids_initiate' and 'run_simulation.
    * Running 'bad_boids' on the command line without specifying a config file will run the simulation with the above default values for all the parameteres.

