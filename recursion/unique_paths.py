#!/usr/bin/env python3

def unique_paths(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    else:
        return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)

def main():
    print(unique_paths(4, 6))

if __name__ == '__main__':
    main()