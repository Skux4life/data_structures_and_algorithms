#!/usr/bin/env python3

# Write a function that uses a stack to reverse a string

from stack import Stack


def reverse_string(str):
    my_stack = Stack()
    for char in str:
        my_stack.push(char)
    reversed = ''
    while not my_stack.is_empty():
        reversed += my_stack.read()
        my_stack.pop()
    return reversed

def main():
    test_string = 'abcdefg'
    print(reverse_string(test_string))

# --------------------------------------------------
if __name__ == '__main__':
    main()