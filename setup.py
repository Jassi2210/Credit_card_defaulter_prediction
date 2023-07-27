from setuptools import setup,find_packages
from typing import List

HYPAN_E_DOT = "-e ."

def get_requirements(filepath:str)->List[str]:
    requirements = []

    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n","") for i in requirements]

        if HYPAN_E_DOT in requirements:
            requirements.remove(HYPAN_E_DOT)

    return requirements

setup(
    name="credit_card_defaulter_prediction",
    version="0.0.1",
    author="Jasvinder Singh Shodi",
    author_email="jassi.shodi@gamil.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)