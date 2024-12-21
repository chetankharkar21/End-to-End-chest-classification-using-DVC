import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Metadata
__version__ = "0.0.0"

REPO_NAME = "End-to-End-chest-classification-using-DVC"
AUTHOR_USER_NAME = "chetankharkar21"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "shivkharkar99@gmail.com"

# Setup configuration
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for CNN-based classification application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)
