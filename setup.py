from setuptools import setup, find_packages
from typing import List
def read_requirements(file_path: str)->List[str]:
    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n", "") for req in requirement]
        if "-e ." in requirement:
            requirement.remove("-e .")
    return requirement
setup(
    name='datascience',
    version='0.0.1',
    author='Your Name',
    author_email = "oraya069@gmail.com",
    packages=find_packages(),
    install_requires=read_requirements('requirements.txt'),
    description='A package for data science projects')