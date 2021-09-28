from setuptools import setup, find_packages

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name="br_util",
    version="0.0.1-dev",
    author="Benjamin Rose",
    author_email="benjamin.rose@duke.edu",
    description="????",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/benjaminrose/br_util",
    packages=find_packages(include=["br_util", "br_util.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "astropy",
        "pandas",
        "numpy",
        "matplotlib",
        # "seaborn",
        "scipy",
        "click",
    ],
    entry_points={"console_scripts": ["p2sigma=br_util.cli:p2sigma"]},
)
