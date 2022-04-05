from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='update_gitops_task',
      version='0.2',
      description='Update gitops repo for bumping image and chart version',
      long_description=long_description,
      author='Stakater',
      license='GNU GPLv3',
      packages=['update_gitops_task'],
      zip_safe=False)