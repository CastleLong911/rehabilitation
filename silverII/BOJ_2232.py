n = int(input())
p = [int(input()) for _ in range(n)]
for i in range(n):
    if n > 1:
        if i == 0:
            if p[i] >= p[i+1]:
                print(i+1)
        elif i == n-1:
            if p[i-1] <= p[i]:
                print(i+1)
        else:
            if p[i-1] <= p[i] and p[i] >= p[i+1]:
                print(i+1)
    else:
        print(i+1)