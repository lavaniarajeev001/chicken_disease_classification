from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT="-e ."

def get_requirements(file_path:str)-> List:
    requirements=[]
    requirements=[req.replace("\n","") for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements
            

setup(
    name="cnnClassifier",
    version="0.0.0",
    author="Rajeev Lawania",
    author_email="rajeev.lavania@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)