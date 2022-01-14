#!/usr/bin/env python
import os
import sys

import numpy as np
import prettymatrix

__author__ = "Arian Jamasb"
__email__ = "arian@jamasb.io"


def run(filename: str):
    os.system(f"echo 'Num Rows: ';wc -l {filename}")
    os.system(f"echo 'Num Columns: '; head -1 {filename} | tr ';|,|\t' '\n' | wc -l")
    command = f"column -s, -t < '{filename}' | less -#2 -N -S;"
    os.system(command)


def main():
    filename = sys.argv[1]
    run(filename)
