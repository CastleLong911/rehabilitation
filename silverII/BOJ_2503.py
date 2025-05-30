def comp(a, b):
    b = str(b)
    strike, ball = 0, 0
    for i in range(3):
        if b[i] == str(a[0])[i]:
            strike+=1
        elif b[i] in str(a[0]):
            ball+=1
    return True if a[1] == strike and a[2] == ball else False

n = int(input())
res_set = set(i for i in range(123, 988) if len(set(str(i))) == 3 and '0' not in str(i))
res_set_copy = res_set.copy()
answer = [list(map(int, input().split())) for i in range(n)]


for i in answer:
    for j in res_set:
        if i[0] == j:
            res_set_copy.remove(j)
        elif not comp(i,j):
            res_set_copy.remove(j)
    res_set = res_set_copy.copy()

print(len(res_set))