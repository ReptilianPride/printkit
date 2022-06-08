# Printkit - Make your outputs look great #

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<img alt="Project stage: Development" src="https://img.shields.io/badge/Project%20Stage-Development-yellowgreen.svg" />
[![PyPi version](https://badgen.net/pypi/v/printkit)](https://pypi.com/project/pip)

Printkit is an easy to use python package which contains various tools that enable you to have a distinct and good looking outputs.

## Features: ##
- Change Text Colors
- Change Background Colors

Still working on making the program better with additional features. :blush:

# Installation #
Install and update using [pip](https://pip.pypa.io/en/stable/installation/)

```bash
pip install printkit
```

# How to use printkit #

##  Imports ##
```python
from printkit import *
```

## Usage ##
```python
cprint.[colorname]([string]) #change text color
bgcolor.[colorname]([string]) #change background color


#custom options
cprint.custom([string],color=[ansi color code])
bgcolor.custom(color=[ansi color code])
```

## Miscellaneous Methods ##
```python
import printkit

#To get printkit version
printkit.version()

#To get the available colornames
printkit.colors()
```

## For changing output color ##
### Code ###
```python
#To print 'Success' in green text color
cprint.green('Success')
```
### Output ###
![output for color text](./docs/out1.PNG)

## For changing background color of terminal/console ##
### Code ### 
```python
#Change the background color to cyan
bgcolor.cyan()

#Print with black text
cprint.black('Hello World')

#Make the background color to default
bgcolor.default()
```

### Output ###
![output for background change](./docs/out2.PNG)

## Click [here](./docs/COLORS.md) to see the available colors