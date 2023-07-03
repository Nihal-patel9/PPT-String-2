def reverse_words(s):
    words = s.split()
    result = []

    for word in words:
        reversed_word = reverse_string(word)
        result.append(reversed_word)

    return " ".join(result)


def reverse_string(word):
    left = 0
    right = len(word) - 1
    reversed_word = list(word)

    while left < right:
        reversed_word[left], reversed_word[right] = reversed_word[right], reversed_word[left]
        left += 1
        right -= 1

    return "".join(reversed_word)


s = "Let's take LeetCode contest"
print(reverse_words(s))
