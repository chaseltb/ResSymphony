from setuptools import setup

setup(name='ressymphony',
      version='0.1.4c',
      description='Controller for CircuitSymphony - distributed SPICE',
      url='https://github.com/nfrik/ResSymphony',
      author='Nikolay Frick',
      author_email='nvfrik@ncsu.edu',
      license='MIT',
      packages=['resutils'],
      install_requires=[
          'tqdm','sklearn-deap'
      ],
      zip_safe=False)
