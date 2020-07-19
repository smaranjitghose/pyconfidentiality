from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'PyConfidentiality'
AUTHOR = 'Smaranjit Ghose,Anush Bhatia'
AUTHOR_EMAIL = 'smaranjitghose@protonmail.com,anushbhatia1234@gmail.com'
URL = 'https://github.com/you/pyconfidentiality'

LICENSE = 'MIT License'
DESCRIPTION = 'Conceal your emails with Python'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = ['numpy', 'smtplib', 'email']

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )
