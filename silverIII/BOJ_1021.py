n, m = map(int, input().split())
nums = list(map(int, input().split()))
q = [i for i in range(1, n+1)]
pos = 0
result = 0
for i in nums:
    idx = q.index(i)
    idx_e = len(q) - idx - 1 if len(q) - idx < idx else idx
    pos_e = len(q) - pos - 1 if len(q) - pos < pos else pos
    if abs(pos - idx) > idx_e + pos_e + 1:
        result += idx_e + pos_e + 1
    else:
        result += abs(pos - idx)
    q.remove(i)
    pos = idx
    if pos == len(q):
        pos = 0
print(result)