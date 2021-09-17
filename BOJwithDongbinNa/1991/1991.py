def solve():
    n = int(input())
    child = {}
    for _ in range(n):
        node, left, right = input().split()
        child[node] = (left, right)

    print_buf = []

    def preorder(node):
        print_buf.append(node)
        if child[node][0] in child:
            preorder(child[node][0])
        if child[node][1] in child:
            preorder(child[node][1])

    def inorder(node):
        if child[node][0] in child:
            inorder(child[node][0])
        print_buf.append(node)
        if child[node][1] in child:
            inorder(child[node][1])

    def postorder(node):
        if child[node][0] in child:
            postorder(child[node][0])
        if child[node][1] in child:
            postorder(child[node][1])
        print_buf.append(node)

    preorder('A')
    print_buf.append('\n')
    inorder('A')
    print_buf.append('\n')
    postorder('A')
    print(''.join(print_buf))


solve()
