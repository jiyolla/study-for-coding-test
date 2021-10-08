# https://programmers.co.kr/learn/courses/30/lessons/81303
# 표 편집

class Node:
    def __init__(self, value, prev):
        self.value = value
        self.prev = prev
        self.next = None
        self.is_deleted = False

    def __repr__(self):
        return f'Node({self.value!r})'
    
def solution(n, k, cmd):
    l = []
    prev = Node(0, None)
    for i in range(1, n):
        l.append(prev)
        cur = Node(i, prev)
        prev.next = cur
        prev = cur
    l.append(prev)
    
    cursor = l[k]
    delete_stack = []
    for c in cmd:
        if c[0] == 'U':
            movement = int(c.split()[1])
            for _ in range(movement):
                cursor = cursor.prev
        elif c[0] == 'D':
            movement = int(c.split()[1])
            for _ in range(movement):
                cursor = cursor.next
        elif c[0] == 'C':
            cursor.is_deleted = True
            delete_stack.append(cursor)
            
            if cursor.prev is not None:
                cursor.prev.next = cursor.next
            if cursor.next is not None:
                cursor.next.prev = cursor.prev

            if cursor.next is not None:
                cursor = cursor.next
            else:
                cursor = cursor.prev
        elif c[0] == 'Z':
            node = delete_stack.pop()
            node.is_deleted = False
            if node.prev is not None:
                node.prev.next = node
            if node.next is not None:
                node.next.prev = node
    
    return ''.join(['X' if node.is_deleted else 'O' for node in l])
    
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
