def canUnlockAll(boxes):
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