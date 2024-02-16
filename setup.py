import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="judini",
    version="0.1.10",
    author="Judini Inc.",
    author_email="daniel@judini.ai",
    description="CodeGPT python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JudiniLabs/judini-python",
    packages=setuptools.find_packages(),
    package_data={"judini": ["VERSION"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests", "aiohttp", "asyncio", "python-dotenv", "pydantic"
    ],
)