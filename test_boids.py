from boids import generate_random_uniform
from nose.tools import assert_almost_equal
import random

def test_generate_random_uniform():
    random.seed(1)
    x = [random.uniform(-450,50.0) for x in range(50)]
    random.seed(1)
    x1 = generate_random_uniform(-450,50.0, 50)
    for value in range(50):
        assert_almost_equal(x[value], x1[value], delta = 0.01)

''' commenting out bad implementation code until ready to work on it.

# from boids import update_boids
# from nose.tools import assert_almost_equal
# import os
# import yaml
        
def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data=regression_data["before"]
    update_boids(boid_data)
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
	
'''