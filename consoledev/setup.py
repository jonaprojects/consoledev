import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="consoledev",
    version="1.0.1",
    description="Light tool for creating interactive colored consoles.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://www.google.com",
    author="Jonathan",
    author_email="fakemail@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["consoledev"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "consoledev=__main__:main",
        ]
    },
)
