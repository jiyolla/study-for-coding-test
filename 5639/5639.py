import sys


def solve():
    preorder = list(map(int, sys.stdin.readlines()))
    n = len(preorder)
    # Procedure
    # 0. Given a preorder of a binary search tree
    # 1. The first element is the root, and is printed after all sub trees are printed
    # 2. Remaining elements is divided into two by the value of first element
    # 3. Do the procedure again on both sub tree

    print_buf = []
    stack = [(0, n - 1)]
    while stack:
        start, end = stack.pop()
        print_buf.append(f'{preorder[start]}')
        for i in range(start + 1, end + 1):
            if preorder[start] < preorder[i]:
                if start + 1 <= i - 1:
                    stack.append((start + 1, i - 1))
                if i <= end:
                    stack.append((i, end))
                break
        else:
            if start + 1 <= end:
                stack.append((start + 1, end))
    print('\n'.join(print_buf[::-1]))


solve()
