from setuptools import find_packages , setup
from typing import List

hyphen = "-e ."
def get_requirements(file_path:str) -> List[str] :
    requ=[]
    with open(file_path) as file_obj :
        requ = file_obj.readlines()
        requ = [req.strip() for req in requ]
        
        if hyphen in requ :
            requ.remove(hyphen)
    print("Installing requirements:", requ) 
    return requ

setup(
name="ml_project",
version='0.0.1',
author="Varun",
author_email="varunsaxena5elc@gmail.com",
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)

