from setuptools import setup, find_packages

setup(
    name="owui-sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "pydantic>=2.0.0",
        "python-dotenv>=1.0.0",
    ],
    author="Burak Bolat",
    author_email="burakbolat08@gmail.com",
    description="Python SDK for Open WebUI API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/burakbolat8/owui-sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
) 