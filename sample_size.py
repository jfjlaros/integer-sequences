#!/usr/bin/env python

"""
Calculate the minimal sample size for which a certain percentage can occur.
"""


import argparse


def minimal_sample_size(resolution=100):
    l = [1] + [0] * resolution

    for n in range(1, (resolution + 1)):
        for f in range(1, n + 1):
            p = int(round(f * float(resolution) / n))

            if not l[p]:
                l[p] = n

    return l


def minimal_sample_size_without_rounding(resolution=100):
    l = [1] + [0] * resolution

    for n in range(1, (resolution + 1)):
        for f in range(1, n + 1):
            if not f * resolution % n:
                p = int(round(f * float(resolution) / n))

                if not l[p]:
                    l[p] = n

    return l


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', dest='resolution', type=int, default=100)
    arguments = parser.parse_args()

    for n, p in enumerate(minimal_sample_size(arguments.resolution)):
        print n, p


if __name__ == '__main__':
    main()
