from ..bad_boids import boids
from nose.tools import assert_almost_equals
import random

from nose.tools import assert_almost_equals
def test_generate_random_uniform():
    random.seed(1)
    x = [random.uniform(-450,50.0) for x in range(50)]
    random.seed(1)
    x1 = generate_random_uniform(-450,50.0, 50)
    assert_almost_equals(x, x1, delta = 0.01)