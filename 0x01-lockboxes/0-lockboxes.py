#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """ Write a method that determines if all the boxes can be opened.
    @boxes is a list of lists
    """
    n = len(boxes)
    unlocked = set([0])  # Start with the first box unlocked
    keys = list(boxes[0])  # Start with the keys in the first box
    queue = keys[:]
    
    while queue:
        key = queue.pop(0)
        if key < n and key not in unlocked:
            unlocked.add(key)
            for new_key in boxes[key]:
                if new_key not in unlocked:
                    queue.append(new_key)
    
    return len(unlocked) == n