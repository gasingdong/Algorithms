#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    plays = ["rock", "paper", "scissors"]

    def add_plays(n):
        if n <= 0:
            return [[]]
        if n == 1:
            return [[play] for play in plays]

        old_round = add_plays(n - 1)
        new_round = []
        for play in plays:
            for item in old_round:
                new_round.append([play] + item)
        return new_round

    return add_plays(n)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
