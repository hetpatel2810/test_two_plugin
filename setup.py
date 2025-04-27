#!/usr/bin/env python
import setuptools;

with open("requirements_test_one_plugin.txt") as f:
    requirements = f.read().splitlines();
    requirements = [req.replace("==", ">=") for req in requirements];

# normal setuptool inputs
setuptools.setup(
    version="0.1.0",
    name="pollination-test-two-plugin",  # will be used for package name unless it is overwritten using __queenbee__ info.
    author="hetpatel2810",  # the owner account for this package - required if pushed to Pollination
    author_email="hetpatel2810@gmail.com",
    packages=setuptools.find_namespace_packages(  # required - that's how pollination find the package
        include=["pollination.*"], exclude=["tests", ".github"]
    ),
    install_requires=requirements,
    url="https://github.com/pollination",  # will be translated to home
    project_urls={
        "docker": "https://mcr.microsoft.com/en-us/artifact/mar/powershell/tags",
    },
    description="test-one-plugin-description",  # will be used as package description
    long_description="test-one-plugin-long-description",  # will be translated to ReadMe content on Pollination
    long_description_content_type="text/markdown",
    maintainer="hetpatel2810",  # Package maintainers. For multiple maintainers use comma
    maintainer_email="hetpatel2810@gmail.com",
    keywords="test one plugin",  # will be used as keywords
    zip_safe=False,
    license="MIT",  # <-- This is the correct place for the license name
    classifiers=[
        "License :: OSI Approved :: MIT License",  # <-- Good to include for clarity
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)