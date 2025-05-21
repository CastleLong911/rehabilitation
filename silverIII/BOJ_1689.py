num, m, n = map(int, input().split())
trains = []
timelist = []
for i in range(num):
    tokens = input().split()
    t = {"name": tokens[0], "times": list(map(int, tokens[1:-1]))}
    trains.append(t)
    timelist += trains[i]["times"]

timelist.sort()
firstTime = 0
for i in timelist:
    if m < i:
        firstTime = timelist.index(i)
        break

lastTime = timelist[(firstTime + n - 1) % len(timelist)]

for i in trains:
    if lastTime in i["times"]:
        print(i["name"])
        break