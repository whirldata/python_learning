"""setup.py
Ref: # https://packaging.python.org/tutorials/packaging-projects/
"""

__author__      = "Muthu"
__email__ = "mu@whirldatascience.com"
__status__ = "Demo"

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my_pkg", # Replace with your own username
    version="0.0.1",
    author= __author__,
    author_email=__email__,
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)