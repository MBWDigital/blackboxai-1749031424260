from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in project_gantt/__init__.py
from project_gantt import __version__ as version

setup(
    name="project_gantt",
    version=version,
    description="Show Gantt Chart in Project Detail",
    author="Your Name",
    author_email="your@email.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
