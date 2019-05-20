import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "PyodbcListOfDicts",
    version = "2019.04.09",
    author = "Dariyush",
    author_email = "dariyush@gmail.com",
    description = "Returns a List Of Dicts if quering DataBase using PyODBC",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url="https://github.com/dariyush/PyodbcListOfDicts",
    packages = setuptools.find_packages(),
    install_requires = ['pyodbc'],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)