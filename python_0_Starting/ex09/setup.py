from setuptools import setup, find_packages

setup(
	name='ft_package',
	version='0.0.1',
	packages=find_packages(),
	description=open("README.md").read(),
	author='sachouam',
	author_email='sachouam@student.42.fr',
	url=": https://github.com/Claken/ft_package",
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[], 
)