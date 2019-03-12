import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hello_pkg",
    version="0.0.1",
    author="LiuTianping",
    author_email="937406831@qq.com",
    description="A small hello package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lieyingzaixian/hello",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)