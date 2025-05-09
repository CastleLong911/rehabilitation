import datetime

startDay = list(map(int, input().split()))
endDay = list(map(int, input().split()))

sdd = datetime.datetime(startDay[0], startDay[1], startDay[2])
edd = datetime.datetime(endDay[0], endDay[1], endDay[2])
if sdd.year + 1000 < 10000:
    try:
        sdd_t = datetime.datetime(startDay[0] + 1000, startDay[1], startDay[2])
    except:
        sdd_t = datetime.datetime(startDay[0] + 1000, startDay[1], 28)

    if(sdd_t <= edd):
        print("gg")
    else:
        print("D-" + str((edd-sdd).days))
else:
    print("D-" + str((edd-sdd).days))