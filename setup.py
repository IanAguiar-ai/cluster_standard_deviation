from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.1"
DESCRIPTION = "Cluster Deviation.\nClustering system made from scratch, designed to be as simple as possible."
LONG_DESCRIPTION = "Classification system that uses the concept of standard deviation and 'pull' and 'push' iterations. For more details read the instructions on git 'https://github.com/IanAguiar-ai/cluster_standard_deviation'."

# Setting up
setup(
    name="cluster_deviation",
    version=VERSION,
    author=["Ian dos Anjos"],
    author_email="<iannaianjos@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=["python", "cluster", "standard deviation", "iterative method"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
