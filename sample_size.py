#!/usr/bin/env python

"""
Calculate the minimal sample size for which a certain percentage can occur.
"""

def minimal_sample_size(resolution=100):
    l = [0] * (resolution + 1)

    for n in range(1, (resolution + 1)):
        for f in range(n + 1):
            p = int(round(f * float(resolution) / n))

            if not l[p]:
                l[p] = n

    return l


for n, p in enumerate(minimal_sample_size()):
    print n, p
