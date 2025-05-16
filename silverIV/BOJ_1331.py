pos = ''
pos_f = ''
check = True
board = [[0 for i in range(6)] for i in range(6)]
for i in range(36):
    t = input()
    if pos == '':
        pos = t
        pos_f = t
    else:
        if not((abs(ord(pos[0]) - ord(t[0])) == 2 and abs(int(pos[1]) - int(t[1])) == 1) or (abs(ord(pos[0]) - ord(t[0])) == 1 and abs(int(pos[1]) - int(t[1])) == 2)) :
            check = False
        pos = t
    board[ord(pos[0])-65][int(pos[1]) - 1] += 1

for i in board:
    for j in i:
        if j != 1:
            check = False
            
if not ((abs(ord(pos[0]) - ord(pos_f[0])) == 2 and abs(int(pos[1]) - int(pos_f[1])) == 1) or (abs(ord(pos[0]) - ord(pos_f[0])) == 1 and abs(int(pos[1]) - int(pos_f[1])) == 2)):
    check = False

if check:
    print("Valid")
else:
    print("Invalid")

