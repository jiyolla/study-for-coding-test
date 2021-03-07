import random


def gen():
    random.seed(102)
    N = 100000
    tree = [None] * (N + 1)

    def spawn(parent, this, n):
        max_n_child = random.randint(1, 10)
        tree[this] = parent
        n = n - 1
        count = this + 1
        for i in range(max_n_child):
            if n < 1:
                break
            n_childs_node = random.randint(1, n)
            n = n - n_childs_node
            spawn(this, count, n_childs_node)
            count += n_childs_node
        else:
            spawn(this, count, n)
    spawn(0, 1, N)
    print(N)
    for i in range(2, N + 1):
        print(i, tree[i])
    q = random.randint(1, N)
    print(q)
    for _ in range(q):
        print(random.randint(1, N), random.randint(1, N))
    for i in range(2, N + 1):
        print(f'tree[{i}]: {tree[i]}')


gen()
