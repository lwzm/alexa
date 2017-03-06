#!/usr/bin/env python3

import os
import sys
import time
import pathlib


def main():
    d = pathlib.Path("hosts")

    hosts_list = []
    hosts = set()
    for p in d.glob("*"):
        with p.open() as f:
            se = set(f.readlines())
            hosts_list.append(se)
            hosts |= se
        print(p, len(hosts))

    with open("hosts.union", "w") as f:
        for i in set.union(*hosts_list):
            f.write(i)

    with open("hosts.intersection", "w") as f:
        for i in set.intersection(*hosts_list):
            f.write(i)

if __name__ == '__main__':
    main()
