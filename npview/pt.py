#!/usr/bin/env python
try:
    import torch
except ImportError:
    raise ImportError('Please install PyTorch: go to pytorch.org')

import sys

import numpy as np
import torch

__author__ = "Arian Jamasb"
__email__ = "arian@jamasb.io"


def run(filename: str):
    data = torch.load(filename)
    if isinstance(data, torch.Tensor):
        print("Shape: ", data.shape)
        print(data)
    else:
        for i in data:
            print("Shape: ", i.shape)
            print(i)


def main():
    filename = sys.argv[1]
    try:
        threshold = int(sys.argv[2])
    except IndexError:
        threshold = threshold = sys.maxsize
    np.set_printoptions(threshold=threshold)
    run(filename)
