#!/usr/bin/python

import sys


def making_change(amount, denominations):
    pass


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print(
            f"There are {making_change(amount, denominations)} ways to make"
            + f"{amount} cents.")
    else:
        print("Usage: making_change.py [amount]")
