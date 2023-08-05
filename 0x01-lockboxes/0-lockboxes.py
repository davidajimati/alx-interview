#!/usr/bin/python3
"""
LOCKBOXES ALGO. -> method to determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """function to check if boxes can be unlocked"""
    n = len(boxes)
    visited = set([0])  # Start with the first box (box 0) as visited
    keys_to_check = boxes[0]  # Keys available in the first box

    while keys_to_check:
        next_key = keys_to_check.pop()  # Take the last key from the list
        if next_key < n and next_key not in visited:
            visited.add(next_key)  # Mark the box as visited
            # Add keys from the new box to check
            keys_to_check.extend(boxes[next_key])
    return (len(visited) == n)
