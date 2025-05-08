import math

num = int(input())

nums = [[] for i in range(num)]

for i in range(num):
    nums[i] = input().split()

for i in range(num):
    print(int(math.factorial(int(nums[i][1])) / (math.factorial(int(nums[i][0])) * math.factorial(int(nums[i][1])-int(nums[i][0])))))