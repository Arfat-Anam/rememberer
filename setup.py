from setuptools import setup, find_packages
from pathlib import Path

# Read the long description from the README.md file
here = Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="rememberer",
    version="0.1.5",
    description="A lightweight tool to help Python functions remember their previous results using pickle caching.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ChamRun",
    author_email="chrm@aut.ac.ir",
    url="https://github.com/ChamRun/rememberer",
    project_urls={
        "Homepage": "https://chamrun.github.io/",
        "Source": "https://github.com/ChamRun/rememberer",
    },
    license="MIT",
    keywords=["pickle", "cache", "memoization", "function caching"],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.5",
    install_requires=[
        "pickle5; python_version<'3.8'"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
