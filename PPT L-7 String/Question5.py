def reverse_str(s, k):
    result = list(s)
    n = len(result)
    i = 0

    while i < n:
        left = i
        right = min(i + k - 1, n - 1)

        while left < right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1

        i += 2 * k

    return "".join(result)


s = "abcdefg"
k = 2
print(reverse_str(s, k))
