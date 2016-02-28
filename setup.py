from setuptools import setup, find_packages

setup(
    name = "Bad boids",
    version = "0.1",
    description = "A simulation of a flock of birds.",
    url = "https://github.com/AnoshZahir/bad_boids.git",
    licence = "MIT",
    author = "Anosh Zahir",
    author_email = "anosh.zahir15@imperial.ac.uk",
    packages = find_packages(exclude = ['*test']),
    install_requires = ['argparse', 'matplotlib', 'numpy', 'nose', 'mock']
)

 