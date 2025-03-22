from setuptools import setup, find_packages

setup(
    name="colorog",
    version="1.0.0",
    author="Alex Holland",
    author_email="<alexh9392@hotmail.com>",
    description="Make Python output not boring!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["termcolor", "colorama", "affixr"],
    keywords=["colorog"],
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: 3.15",
        "Development Status :: 6 - Mature",
        "Operating System :: OS Independent",
    ],
    license="MIT License",
    include=["LICENSE", "README.md"],
)
