'''
the setup.py file is essential for packaging and distributing Python projects.
It provides metadata about the project and instructions on how to install it.
'''

from setuptools import setup, find_packages
from typing import List


def get_requirements()-> List[str]:
    '''
    This function reads the requirements.txt file and returns a list of dependencies.
    '''
    
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement=line.strip()
                
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
                    
    except FileNotFoundError:
        print("requirements.txt file not found.")
        
    return requirement_lst

setup(
    name='Network-Security',
    version='0.0.1',
    author='Priyanshu Kothari',
    author_email='priyanshukothari1808@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
    )