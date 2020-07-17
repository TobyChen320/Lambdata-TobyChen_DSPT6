import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Lambdata-TobyChen_DSPT6",  # Replace with your own username
    version="0.0.4",
    author="Toby Chen",
    author_email="toby-chen@lambdastudents.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TobyChen320/Lambdata-TobyChen_DSPT6",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
