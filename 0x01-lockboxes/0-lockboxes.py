#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True

    stack = [0]  # Start with the first box
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                stack.append(key)

    return all(unlocked_boxes)


boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 2], [3, 4], [2], []]
print(canUnlockAll(boxes))  # Output: False
