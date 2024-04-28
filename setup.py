from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT= "-e ."
def getrequirements(file_path:str)->List[str]:
    '''
    returns requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [r.replace("\n","") for  r in requirements]

        if(HYPHEN_E_DOT in requirements):
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
name='mlproject',
version='0.0.1',
author='krish',
author_email='somya.agarwal07@gmail.com',
packages=find_packages(),
install_requires=getrequirements('requirements.txt')


)