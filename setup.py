# ############################################
# 
#         TrakteerDonate Package Setup        
#          ~~ 2023 (c) by Realzzy ~~
# 
# ############################################

from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="trakteerdonate",
    version="1.0a2",
    author="Realzzy",
    author_email="hello@therealzzy.xyz",
    description="An easy way to listen for Trakteer donation in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/then77/trakteerdonate",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=["websockets"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.6",
)