size = list(map(int, input().split()))
map_ = []
pw = 0
pb = 0
def merge(x, y, c):
    if x < 0 or x >= size[0] or y < 0 or y >= size[1]:
        return 0
    elif map_[y][x] is not c:
        return 0
    else:
        map_[y][x] = 0
        return 1 + merge(x-1, y, c) + merge(x+1, y, c) + merge(x, y-1, c) + merge(x, y+1, c)

for i in range(size[1]):
    line = input()
    map_.append(list(line))

for i in range(size[1]):
    for j in range(size[0]):
        if map_[i][j] == 0:
            continue
        else:
            if map_[i][j] == 'W':
                pw += merge(j, i, map_[i][j]) ** 2
            else:
                pb += merge(j, i, map_[i][j]) ** 2

print(pw, pb)