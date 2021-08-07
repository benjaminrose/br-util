from setuptools import setup, find_packages

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name="br_util",
    version="0.0.1",
    author="Benjamin Rose",
    author_email="benjamin.rose@duke.edu",
    description="Extending the twins embedding with neural nets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/benjaminrose/br_uti",
    packages=find_packages(include=["br_util", "br_util.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["astropy", "pandas", "numpy", "matplotlib", "seaborn", "scipy"],
    # entry_points={"console_scripts": ["my-command=br_util.cli:main"]},
)
