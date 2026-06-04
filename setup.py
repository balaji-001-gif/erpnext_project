from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="projects",
    version="15.0.0",
    description="Standalone Projects app for ERPNext v15",
    author="ERPNext Community",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
)
