def can_shift(s, goal):
    if len(s) != len(goal):
        return False

    n = len(s)
    for i in range(n):
        if s[i:] + s[:i] == goal:
            return True

    return False


s = "abcde"
goal = "cdeab"
print(can_shift(s, goal))
