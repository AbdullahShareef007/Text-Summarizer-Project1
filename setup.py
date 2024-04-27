import setuptools

# Read the contents of README.md file for the long description
with open("README.md", "r", encoding="utf-8" ) as f: 
    long_description = f.read()

# Define package metadata
__version__ = "0.0.0"
REPO_NAME= "Text-Summarizer-Project1"
AUTHOR_USER_NAME= "AbdullahShareef007"
SRC_REPO="TextSummarizer"
AUTHOR_EMAIL= "abdullahshareef7945512@gmail.com"

# Setup configuration
setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AbdullahShareef007/Text-Summarizer-Project1",
    package_dir= {"": "src"},  # Specify the package directory (source code)
    packages=setuptools.find_packages(where="src"),  # Find packages in the source directory
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
