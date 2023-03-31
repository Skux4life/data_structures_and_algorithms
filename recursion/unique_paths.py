#!/usr/bin/env python3

def unique_paths(rows, columns):
    if rows == 1 or columns == 1:
        print('no memo')
        return 1
    else:
        print('no memo')
        return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)

def unique_paths_memo(rows, columns, memo):
    if rows == 1 or columns == 1:
        print('memo')
        return 1
    else:
        key = (rows, columns)
        if not memo.get(key):
            memo[key] = unique_paths_memo(rows - 1, columns, memo) + unique_paths_memo(rows, columns - 1, memo)
        print('memo')
        return memo[key]

def main():
    print(unique_paths(4, 6))
    print(unique_paths_memo(4, 6, {}))
    

if __name__ == '__main__':
    main()