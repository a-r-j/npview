# NPView

[![PyPI version](https://badge.fury.io/py/npview.svg)](https://badge.fury.io/py/npview)
![supported python versions](https://img.shields.io/pypi/pyversions/npview)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


CLI tools for quickly viewing data in various formats (eventually). Currently only `.npy` files are supported.

## Installation

```bash
pip install npview
```

## Usage

```bash
npv {PATH_TO_YOUR_FILE.npy} {THRESHOLD}
```

Where `{THRESHOLD}` is an integer specifying Total number of array elements which trigger summarization rather than full repr. Default is `sys.maxsize`.

```bash
npp {PATH_TO_YOUR_FILE.npy}
```

Will attempt to print your saved matrix & itss dimensions using [prettymatrix](https://github.com/samueljamesbell/prettymatrix):

```bash
# (2x2)
#  ┌          ┐
#  │ 1   22   │
#  │ 333 4444 │
#  └          ┘
#
```