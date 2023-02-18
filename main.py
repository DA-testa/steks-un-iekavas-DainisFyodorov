# python3
# 221RDB418 Dainis Fjodorovs

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((next, i))
            pass
        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            last_open, last_open_index = opening_brackets_stack.pop()
            if (next == ')' and last_open != '(') or \
               (next == '}' and last_open != '{') or \
               (next == ']' and last_open != '['):
                return i + 1
            pass
    if opening_brackets_stack:
        last_open, last_open_index = opening_brackets_stack.pop()
        return last_open_index + 1
    return 'Success'


def main():
    text = input().upper()
    if text == 'F':
        file_name = input()
        with open(file_name, 'r') as f:
            input_string = f.read()
            mismatch = find_mismatch(input_string)
            print(mismatch)
        pass
    else:
        input_string = input()
        mismatch = find_mismatch(input_string)
        print(mismatch)


if __name__ == "__main__":
    main()
