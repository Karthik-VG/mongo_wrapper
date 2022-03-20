from curses.ascii import US
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "mongoops-atlas"
USER_NAME = "Karthik-VG"

setuptools.setup(
    name= f"{PROJECT_NAME}-{USER_NAME}",
    version="0.0.1",
    author=USER_NAME,
    author_email="karthikvg.engineer@gmail.com",
    description="Its a implementation of mongodB operations for atlas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url= f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": "https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires = [
        "pymongo==2.8",
        "pandas",
        "json",
        "dns",
        "sys"
    ]

)