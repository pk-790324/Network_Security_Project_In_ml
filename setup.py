from setuptools import find_packages,setup
from typing import List


#this function will return the list of requirements 
def get_requirements()->List[str]:
    requirements_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirements_lst.append(requirement)

    except FileNotFoundError:
        print('reqirements.txt file not found')

    return requirements_lst




setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='pappu yadav',
    author_email='pappuyadav98199@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
