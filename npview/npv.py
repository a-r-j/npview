#!/usr/bin/env python
import pickle
import sys

import numpy as np

__author__ = "Arian Jamasb"
__email__ = "arian@jamasb.io"


def run(filename: str):
    data = np.load(filename, allow_pickle=True)
    print(data)


def main():
    filename = sys.argv[1]
    try:
        threshold = int(sys.argv[2])
    except IndexError:
        threshold = threshold = sys.maxsize
    np.set_printoptions(threshold=threshold)
    run(filename)
