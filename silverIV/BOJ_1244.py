num = int(input())
switches = list(map(int, input().split()))
nos = int(input())
std = []
for i in range(nos):
    std.append(list(map(int, input().split())))
    
    if std[i][0] == 1:
        c = 1
        while True:
            if num < c * std[i][1]:
                break
            else:
                switches[c*std[i][1] - 1] = 1 - switches[c*std[i][1] - 1]
            c+=1
    
    else:
        c = 1
        switches[std[i][1] - 1] = 1 - switches[std[i][1] - 1]
        while True:
            if std[i][1] - 1 + c >= num or std[i][1] - 1 - c < 0:
                break
            if switches[std[i][1] - 1 + c] != switches[std[i][1] - 1 - c]:
                break
            else:
                switches[std[i][1] + c - 1] = 1 - switches[std[i][1] + c - 1]
                switches[std[i][1] - c - 1] = 1 - switches[std[i][1] - c - 1]
            c+=1

for i in range(num):
    print(switches[i], end=' ')
    if(i + 1) % 20 == 0:
        print()
print()