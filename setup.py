import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="dictionary_generator",
    version="1.0.0",
    description="BMSTU word dictionary generator",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/BoldinDmitry/dictionary_bmstu",
    author="BMSTU",
    author_email="office@bmstu.ru",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["dictionary_generator"],
    include_package_data=True,
    install_requires=["delta", "lxml", "Pillow", "python-docx"],
    entry_points={
        "console_scripts": [
            "dictionary_generator=dictionary_generator.__main__:main",
        ]
    },
)