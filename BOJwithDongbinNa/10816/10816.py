import sys
from collections import Counter

read = sys.stdin.readline
read()
cards = Counter(read().split())
read()
reqs = read().split()

print(*[str(cards[req]) for req in reqs])
