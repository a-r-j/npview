#!/usr/bin/env python
import sys

import numpy as np
import prettymatrix

__author__ = "Arian Jamasb"
__email__ = "arian@jamasb.io"


def run(filename: str):
    data = np.load(filename, allow_pickle=True)
    try:
        data = prettymatrix.matrix_to_string(data, include_dimensions=True)
    except ValueError:
        print("Shape: ", data.shape)
        pass
    print(data)


def main():
    filename = sys.argv[1]
    # try:
    #    threshold = int(sys.argv[2])
    # except IndexError:
    # threshold = threshold = sys.maxsize
    # np.set_printoptions(threshold=threshold)
    run(filename)
