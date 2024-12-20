from setuptools import find_packages, setup

setup(
    name="VeMatch",
    version="0.0.1",
    packages=find_packages(),
    package_data={"vematch": ["datasets/datasets.yaml"]},
    install_requires=["requests", "PyYAML", "tqdm", "torch"],
    python_requires=">=3.10",
    description="A comprehensive toolkit for managing datasets and implementing advanced techniques for similar image identification.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Gabriel Soares Baptista",
    author_email="gsoaresbaptista@gmail.com",
    url="https://github.com/gsoaresbaptista/VeMatch",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
