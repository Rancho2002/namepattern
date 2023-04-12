from setuptools import setup

VERSION = '0.0.1'
DESCRIPTION = 'Printing name pattern with python'
LONG_DESCRIPTION = 'A package that prints name pattern with python takes input, design style(pattern type), and length from user and prints the pattern.'

# Setting up
setup(
    name="namepattern",
    version=VERSION,
    author="Arijit Ghosh",
    author_email="subhasghosh196@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=["namepattern"],
    install_requires=[],
    keywords=['python', 'namepattern', 'pattern'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)