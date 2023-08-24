#!/usr/bin/python3
"""making change project"""

def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    if total <= 0:
        return 0

    change = [float('inf')] * (total + 1)
    change[0] = 0

    for i in range(1, total + 1):
        for j in range(len(coins)):
            if coins[j] <= i:
                sub_res = change[i - coins[j]]
                if sub_res != float('inf') and sub_res + 1 < change[i]:
                    change[i] = sub_res + 1

    if change[total] == float('inf'):
        return -1
    else:
        return change[total]
