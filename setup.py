import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ergast-client-python", # Replace with your own username
    version="0.1",
    author="Thiago Pelizoni",
    author_email="thiago.pelizoni@gmail.com",
    description="A simple client for Ergast Developer API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thiagopelizoni/ergast-client-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
