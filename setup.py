from setuptools import setup, find_packages

setup(
    name="lbh-sdk",
    version="0.3.0",
    packages=find_packages(),
    author="Cristhiam Leonardo Hernández Quiñonez (CLHQ)",
    description="SDK oficial de referencia del protocolo LBH (Lenguaje Binario HormigasAIS)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Thrumanshow/lbh-sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
