from setuptools import find_packages, setup
from typing import List
import os

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(os.path.join(os.path.dirname(__file__), file_path)) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Akshat',
    author_email='akshat.rajkisu@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
