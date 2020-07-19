from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'PyConfidentiality'
AUTHOR = 'Smaranjit Ghose,Anush Bhatia'
AUTHOR_EMAIL = 'smaranjitghose@protonmail.com,anushbhatia1234@gmail.com'
URL = 'https://github.com/you/pyconfidentiality'
KEYWORDS = "rsa email-sender python cryptography smtp"



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
      keywords = KEYWORDS,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )

   classifiers = [
       "Development Status :: 5 - Production/Stable",
       "Topic :: Software Development :: Build Tools",
       "License :: OSI Approved :: MIT License",
       "Environment :: Console",
       "Operating System :: OS Independent",
       "Intended Audience :: Science/Research",
       "Intended Audience :: Developers",
       "Intended Audience :: Financial and Insurance Industry",
       "Intended Audience :: Healthcare Industry",
       "Topic :: Scientific/Engineering",
       "Framework :: IPython",
       "Programming Language :: Python :: 3",
       "Programming Language :: Python :: 3.6",
       "Programming Language :: Python :: 3.7",
       "Programming Language :: Python :: 3.8",
       "Programming Language :: Python :: 3.9",
   ],
   
