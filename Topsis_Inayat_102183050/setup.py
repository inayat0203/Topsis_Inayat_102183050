import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Topsis_Inayat_102183050",
    version="0.1",
    author="Inayat",
    author_email="inayat0203@gmail.com",
    description="A package -> Calculates Topsis Score and Rank them accordingly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/inayat0203/TOPSIS_INAYAT_102183050",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["Topsis_Inayat_102183050"],
    include_package_data=True,
    install_requires='pandas',
    entry_points={
        "console_scripts": [
            "topsis=Topsis_Inayat_102183050.102183050:main",
        ]
    },
)