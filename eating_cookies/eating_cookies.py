#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    cache = [0] * n

    def eat(n):
        if n < 0:
            return 0
        elif n == 0:
            return 1

        nonlocal cache
        if cache[n - 1] == 0:
            cache[n - 1] = eat(n - 3) + eat(n - 2) + eat(n - 1)

        return cache[n - 1]

    return eat(n)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print(
            f"There are {eating_cookies(num_cookies)} ways for Cookie Monster"
            + f"to eat {num_cookies} cookies.")
    else:
        print('Usage: eating_cookies.py [num_cookies]')
