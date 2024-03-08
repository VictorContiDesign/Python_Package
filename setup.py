from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.0.1'
DESCRIPTION = 'Este paquete permite consumir el API de CodigoFacilito'
PACKAGE_NAME = 'mi_primer_paquete_cf'
AUTHOR = 'Victor Joseph Conti Romero'
EMAIL = 'victor.conti.dev@gmail.com'
GITHUB_URL = 'https://github.com/VictorContiDesign/python_package/tree/master'

setup(
    name = PACKAGE_NAME,
    packages = [DESCRIPTION],
    version = VERSION,
    license='MIT',
    description = DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author = AUTHOR,
    author_email = EMAIL,
    url = GITHUB_URL,
    keywords = [
        'codigofacilito',
        'miprimerpaquete',
        ],
    install_requires=[ 
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)