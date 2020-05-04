from xy import exchange

pool = {"x":100.0, "y":100.0}
startedcap = 10
res = exchange(pool, startedcap, "x")
pool = res[1]
my = res[0]

res = exchange(pool, 1, "x")
pool = res[1]
hy = res[0]

res = exchange(pool, my, "y")
pool = res[1]
mx = res[0]
profit = mx - startedcap

print(profit)