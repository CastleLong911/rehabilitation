import operator

views = {
    "alice": 120,
    "bob": 150,
    "carol": 110,
    "dave": 300,
    "erin": 200
}
v = iter(sorted(views.items(), key=operator.itemgetter(1), reverse=True))

for i in range(3):
    print(next(v)[0])
