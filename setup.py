from setuptools import setup

setup(name='reservoirgen',
      version='0.1',
      description='Generates reservoirs in python3',
       author='Nathaniel Rodriguez',
      packages=['reservoirgen'],
      url='https://github.com/Nathaniel-Rodriguez/reservoirgen.git',
      install_requires=[
          'numpy',
      ],
      include_package_data=True)
