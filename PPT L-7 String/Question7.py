def build_string(s):
    stack = []
    for char in s:
        if char != '#':
            stack.append(char)
        elif stack:
            stack.pop()
    return "".join(stack)


def backspace_compare(s, t):
    return build_string(s) == build_string(t)


s = "ab#c"
t = "ad#c"
print(backspace_compare(s, t))
