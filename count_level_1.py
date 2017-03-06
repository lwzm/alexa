#!/usr/bin/env python3

import collections
import os
import sys
import time
import pathlib


def main():
    cnt = collections.Counter()
    while True:
        try:
            s = input()
        except Exception as e:
            break
        *_, a, b = s.split(".")
        cnt[(a,b)] += 1
    for k, v in cnt.most_common(50):
        print(k, v)


if __name__ == '__main__':
    main()
