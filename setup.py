import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cryptocmp",
    version="0.0.1",
    author="OkThought",
    author_email="bogush.vano@gmail.com",
    description="Python3 Wrapper for CryptoCompare's public API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OkThought/cryptocmp",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)