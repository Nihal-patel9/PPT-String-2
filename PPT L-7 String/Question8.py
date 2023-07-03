def checkStraightLine(coordinates):
    if len(coordinates) <= 2:
        return True

    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        if (y1 - y0) * (x - x0) != (y - y0) * (x1 - x0):
            return False

    return True


coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
print(checkStraightLine(coordinates))
