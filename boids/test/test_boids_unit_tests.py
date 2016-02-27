from ..boids import Boids

import numpy as np
from numpy import testing as npt
from mock import patch
import yaml
import os
 
def test_new_flock():
    with open(os.path.join(os.path.dirname(__file__),'fixtures', 'unit_tests_data.yaml')) as dataset:
        new_flock_data = yaml.load(dataset)['test_new_flock']
        
        for data in new_flock_data:
            rand = data.pop('rand')
            positions  = data.pop('positions')
            velocities = data.pop('velocities')
    
    with patch.object(np.random, 'rand', return_value=rand) as mock_method:
        boids=Boids()
	npt.assert_array_equal(np.asarray(positions),  boids.positions)
	npt.assert_array_equal(np.asarray(velocities), boids.velocities)