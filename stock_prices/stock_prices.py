#!/usr/bin/python

import argparse


def find_max_profit(prices):
    if not prices:
        return 0

    cur_min = prices[0]
    profit = -cur_min

    for i in range(1, len(prices)):
        price = prices[i]
        if price - cur_min > profit:
            profit = price - cur_min

        if price < cur_min:
            cur_min = price

    return profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}."
          .format(profit=find_max_profit(args.integers), prices=args.integers))
