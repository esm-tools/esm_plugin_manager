#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["esm_parser @ git+https://github.com/esm-tools/esm_parser.git"]

setup_requirements = []

test_requirements = []

setup(
    author="Dirk Barbi, Paul Gierz, Sebastian Wahl",
    author_email="dirk.barbi@awi.de",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Plugin Manager for python codes",
    install_requires=requirements,
    license="GNU General Public License v2",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="esm_plugin_manager",
    name="esm_plugin_manager",
    packages=find_packages(include=["esm_plugin_manager", "esm_plugin_manager.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/esm-tools/esm_plugin_manager",
    version="5.0.0",
    zip_safe=False,
    entry_points={"console_scripts": ["esm_plugins=esm_plugin_manager.cli:main"]},
)
