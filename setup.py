from setuptools import find_packages, setup
from typing import List




setup(

    name="US_Visa_Pred",
    version="0.0.1",
    author="Faizan Riaz",
    author_email="riazfaizan614@gmail.com",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.125.0",
        "mlflow==3.5.1",
        "dagshub==0.3.34",
        "evidently==0.2.8",
        "scikit-learn",
        "pandas",
        "numpy",
    ],

)