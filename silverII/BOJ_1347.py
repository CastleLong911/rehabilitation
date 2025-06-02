n = int(input())
footprint = input()
dir, size_left_x, size_right_x, size_up_y, size_down_y, pos_x, pos_y = 0, 0, 0, 0, 0, 0, 0
map_ = [['#' for i in range(101)] for j in range(101)]
map_[50+pos_y][50+pos_x] = '.'
for i in footprint:
    if i == 'R':
        dir = (dir + 1) % 4
    elif i == 'L':
        dir = (dir - 1) % 4
    else:
        if dir == 0:
            pos_y -= 1
            size_down_y = pos_y if pos_y < size_down_y else size_down_y
        elif dir == 1:
            pos_x -= 1
            size_left_x = pos_x if pos_x < size_left_x else size_left_x
        elif dir == 2:
            pos_y += 1
            size_up_y = pos_y if pos_y > size_up_y else size_up_y
        elif dir == 3:
            pos_x += 1
            size_right_x = pos_x if pos_x > size_right_x else size_right_x
    map_[50+pos_y][50+pos_x] = '.'

for i in range(50+size_up_y, 50+size_down_y-1, -1):
    for j in range(50+size_left_x, 50+size_right_x+1):
        print(map_[i][j], end='')
    print()