#/usr/bin/python3
"""0-lockboxes."""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened."""
    unlocked = [boxes[0]]
    for box in unlocked:
        for b in box:
            if b < len(boxes) and boxes[b] not in unlocked:
                unlocked.append(boxes[b])
    return len(unlocked) == len(boxes)
