from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(path:str) -> List[str]:
    """This function will grab all of the packages from requirements.txt"""
    requirements = []
    with open(path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name = "JaneStreet-Forcasting",
    version = "0.0.1",
    author = "Swapnil",
    author_email = "sarmahs538@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt") 
)