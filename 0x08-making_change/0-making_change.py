#!/usr/bin/python3
"""
Module for making change
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    coins (list): A list of the values of the coins in your possession.
    total (int): The total amount of money to make change for.

    Returns:
    int: The fewest number of coins needed to meet the total, or 
    -1 if the total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while(total >= i):
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1
