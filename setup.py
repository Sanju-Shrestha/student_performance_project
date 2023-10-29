from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            req = line.strip()
            if req and req != HYPEN_E_DOT:
                requirements.append(req)

    return requirements




setup(
name='student_performannce_project',
version='0.0.1',
author='Sanju',
author_email='sanjushresthanp@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)