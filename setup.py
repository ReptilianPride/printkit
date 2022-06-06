from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1'
DESCRIPTION = 'printkit enables you to have a prettier outputs. Change the text and background color of your print commands in your code.'

# Setting up
setup(
    name="printkit",
    version=VERSION,
    author="printkit (CipherKill)",
    author_email="alanraju99@gmail.com",
	url="https://github.com/CipherKill/printkit",
	license='MIT',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    keywords=['python','print','terminal','console','colors','style'],
	install_requires=[],
    classifiers=[
		"Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
