#!/usr/bin/env python3
from setuptools import setup

if __name__ == "__main__":
      setup(name='json_tree',
      version='0.0.1',
      description="""Build a user-friendly tree structure from a JSON string.""",
      url='http://github.com/eric02138/json_tree',
      author='Eric Mattison',
      author_email='emattison@gmail.com',
      license='MIT',
      packages=['src'],
      zip_safe=False)