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
            opening_brackets_stack.append(Bracket(next,i))
            

        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            opening_brackets_stack.pop()
            
            
    if opening_brackets_stack:
        return opening_brackets_stack[-1].position + 1 
    return "Success"


def main():
    text = input()
    if text == 'F':
        file_name = input()
        with open(file_name, 'r') as f:
            input_string = f.read()
            mismatch = find_mismatch(input_string)
            print(mismatch)
        pass
    elif text == 'I':
        input_string = input()
        mismatch = find_mismatch(input_string)
        print(mismatch)
    else:
        mismatch = find_mismatch(text)
        print(mismatch)


if __name__ == "__main__":
    main()
