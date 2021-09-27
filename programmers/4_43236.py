# https://programmers.co.kr/learn/courses/30/lessons/43236
# 징검다리

# 약 50000개의 거리들을 정렬해서 
# 최소인 애들을 뽑아서, 어떤 기준에 의거해서 그 거리가 포함하는 노드 하나를 없애고
# 노드를 없앨 때, 무조건 또 하나의 거리도 영향을 받기에, 걔를 50000개 속에서 binary search를 찾고
# 걔를 pop하고 수정하고, 다시 삽입(bisect이용)해서 
# 이 과정을 반복하면 될 것 같다.

# 여기서 해겨할 디테일, 동거리 애들 선정 기준.

from collections import namedtuple
import math
import bisect


class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            return self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)

tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print(tree.find(3).v)
print(tree.find(10))
tree.deleteTree()
tree.printTree()


def solution(distance, rocks, n):
    rocks.extend([0, distance])
    rocks.sort()
    Rock = namedtuple('Rock', ['left', 'right'])
    new_rocks = [Rock(math.inf, rocks[1])]
    for i in range(1, len(rocks) - 1):
        new_rocks.append(Rock(rocks[i] - rocks[i - 1], rocks[i + 1] - rocks[i]))
    new_rocks.append(Rock(rocks[-1], math.inf))
    rocks = new_rocks

    Distance = namedtuple('Distance', ['length', 'left_rock', 'right_rock'])
    distances = []
    for i in range(1, len(rocks)):
        distances.append(Distance(rocks[i].left, rocks[i - 1], rocks[i]))
    distances.sort(key=lambda distance: (distance.length, min(distance.left_rock.right, distance.right_rock.left)))
    
    for _ in range(n):
        # Pop the shortest distance
        distance = distances.pop(0)
        
        # Modify the affected distance
        if distance.left_rock.right < distance.right_rock.left:
            dist = distance.left_rock.right
            for i in range(bisect.bisect_left(distances, dist), bisect.bisect(distances, dist)):
                if distances[i].right_rock == distance.left_rock:
                    distances[i].right_rock = distance.right_rock
                    modified_distance = distances.pop(i)
        else:
            dist = distance.right_rock.left
            for i in range(bisect.bisect_left(distances, dist), bisect.bisect(distances, dist)):
                if distances[i].left_rock == distance.right_rock:
                    distances[i].left_rock = distance.left_rock
                    modified_distance = distances.pop(i)
        bisect.modified_distance
        
        
        
        
    
    answer = 0
    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))
