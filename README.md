

| **Authors**  | **Project** |  **Build Status** | **License** | **Code Quality** | **Documentation** |
|:------------:|:-----------:|:-----------------:|:-----------:|:----------------:|:---:|
|**R. Biondi** |**PUMA**      | **Windows** : [![Windows CI](https://github.com/RiccardoBiondi/PUMA/workflows/Windows%20CI/badge.svg)](https://github.com/RiccardoBiondi/PUMA/actions/workflows/windows.yml)    <br/> **Ubuntu** : [![Ubuntu CI](https://github.com/RiccardoBiondi/PUMA/workflows/Ubuntu%20CI/badge.svg)](https://github.com/RiccardoBiondi/PUMA/actions/workflows/ubuntu.yml)            |      [![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/RiccardoBiondi/PUMA/blob/master/LICENSE.md)       |  **codebeat** [![codebeat badge](https://codebeat.co/badges/6021933b-ccad-4811-b7a4-cf6924956ea7)](https://codebeat.co/projects/github-com-riccardobiondi-PUMA-master)         <br> **codacy** [![Codacy Badge](https://app.codacy.com/project/badge/Grade/e5f17dafa6654034b605f67f6c8dfce9)](https://www.codacy.com/gh/RiccardoBiondi/PUMA/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=RiccardoBiondi/PUMA&amp;utm_campaign=Badge_Grade)     | [![Documentation Status](https://readthedocs.org/projects/PUMA/badge/?version=latest)](https://PUMA.readthedocs.io/en/latest/?badge=latest)|

[![GitHub pull-requests](https://img.shields.io/github/issues-pr/RiccardoBiondi/PUMA.svg?style=plastic)](https://github.com/RiccardoBiondi/PUMA/pulls)
[![GitHub issues](https://img.shields.io/github/issues/RiccardoBiondi/PUMA.svg?style=plastic)](https://github.com/RiccardoBiondi/PUMA/issues)

[![GitHub stars](https://img.shields.io/github/stars/RiccardoBiondi/PUMA.svg?label=Stars&style=social)](https://github.com/RiccardoBiondi/PUMA/stargazers)
[![GitHub watchers](https://img.shields.io/github/watchers/RiccardoBiondi/PUMA.svg?label=Watch&style=social)](https://github.com/RiccardoBiondi/PUMA/watchers)


# Personal Use Macro Archive

PUMA is a more or less organized and structured collection of utilities code snipped
analysis tools.


1. [Contents](#Contents)
2. [Prerequisites](#Prerequisites)
3. [Installation](#Installation)
4. [Usage](#Usage)
5. [Contribute](#Contribute)
6. [License](#License)
7. [Authors](#Authors)
8. [References](#References)
9. [Acknowledgments](#Acknowledgments)
10. [Citation](#Citation)


## Contents

| **Module Name**| **Description**|
|:--------------:|:--------------:|
| profiler       | Series of snipped and class to perform script time profiling |
| units          | Colelciton of basic units class for different physical units. Improve processing and type  hints |

## Prerequisites

Supported python versions: ![Python version](https://img.shields.io/badge/python-3.8.*|3.9.*|3.10.*|3.11.*-blue.svg). Also vesion 3.6 and 3.7  are supperted but not tested.

To run the tests you need to install ```PyTest``` and ```Hypothesis```.
Installation instructions are available at: [PyTest](https://docs.pytest.org/en/6.2.x/getting-started.html), [Hypothesis](https://docs.pytest.org/en/6.2.x/getting-started.html)


## Installation

Download the project or the latest release:

```console
git clone https://github.com/RiccardoBiondi/PUMA
```

```console
python setup.py develop --user
```

### Testing

We have provide a test routine in [test](./test) directory. This routine use:
  - pytest >= 3.0.7

  - hypothesis >= 4.13.0

Please install these packages to perform the test.
You can run the full set of test with:

```console
  python -m pytest
```

## Usage

**TODO**

## Contribute

Any contribution is welcome.  You can fill a issue or a pull request!


## License

Any contribution is more than welcome. Just fill an [issue]() or a [pull request]() and we will check ASAP!

See [here]() for further information about how to contribute with this project.

## Authors

* **Riccardo Biondi** [git](https://github.com/RiccardoBiondi), [unibo](https://www.unibo.it/sitoweb/riccardo.biondi7)