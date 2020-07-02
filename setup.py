from setuptools import setup, find_packages

setup(
    name="kuvat-api",
    version="0.2",
    packages=find_packages(),
    author="Niko Riipiranta",
    description="Kuvat.fi API",
    install_requires=[
        "requests"
    ],
    tests_require=[
        "pytest"
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License"
    ]
)
