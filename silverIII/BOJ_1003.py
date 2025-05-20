memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    result = fib(n - 1) + fib(n - 2)
    memo[n] = result
    return result


n = int(input())
t = []
for i in range(n):
    t.append(int(input()))

for i in t:
    if i == 0:
        print(1, 0)
    elif i == 1:
        print(0, 1)
    else:
        print(fib(i-1), fib(i))