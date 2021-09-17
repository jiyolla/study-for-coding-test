# import sys


def solve():
    # sys.setrecursionlimit(10**6)
    n = int(input())
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))

    # Procedure
    # 0. Given a inorder and postorder of a tree.
    # 1. Set the last element in postorder as root node
    # 2. Search that root node in inorder
    # 3. Do the procedure again on left side and right side divided by that root node
    # Corresponding subpostorder can be infered from the lenghth of left side.
    # This procedure itself visits node in preorder.
    inorder_index = [None] * (n + 1)
    for idx, node in enumerate(inorder):
        inorder_index[node] = idx

    print_buf = []
    """
    def find(in_start, in_end, post_start, post_end):
        if in_start > in_end:
            return
        root = postorder[post_end]
        # index() is too slow here
        # root_idx = inorder[in_start:in_end + 1].index(root)
        root_idx = inorder_index[root]

        print_buf.append(f'{root}')
        in_len = root_idx - 1 - in_start
        find(in_start, root_idx - 1, post_start, post_start + in_len)
        find(root_idx + 1, in_end, post_start + in_len + 1, post_end - 1)

    find(0, len(inorder) - 1, 0, len(postorder) - 1)
    """

    stack = [(0, len(inorder) - 1, 0, len(postorder) - 1)]
    while stack:
        in_start, in_end, post_start, post_end = stack.pop()
        root_idx = inorder_index[postorder[post_end]]
        in_len = root_idx - 1 - in_start
        print_buf.append(f'{postorder[post_end]}')
        if root_idx + 1 <= in_end:
            stack.append((root_idx + 1, in_end, post_start + in_len + 1, post_end - 1))
        if in_start <= root_idx - 1:
            stack.append((in_start, root_idx - 1, post_start, post_start + in_len))
    print(' '.join(print_buf))
    # """


solve()
