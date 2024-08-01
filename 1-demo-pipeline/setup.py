from setuptools import setup, find_packages

setup(name="census-income",
      version="0.0.1",
      author="anjali",
      author_email="test@gmail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]   # you can write a function for package installation as there can be too many packages to be installed
      )