from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirements=line.strip()
                if requirements and requirements != '-e .':
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")

    return requirements_lst

setup(
    name='networksecurity',
    version='0.0.1',
    author='NATAN',
    author_email='natan@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
