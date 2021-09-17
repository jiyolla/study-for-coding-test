import sys
nums = list(map(int, sys.stdin.readlines()))[1:]
final = [0] * len(nums)
cursor = 0
for n in nums:
    if n == 0:
        cursor -= 1
    else:
        final[cursor] = n
        cursor += 1
print(sum(final[0:cursor]))
