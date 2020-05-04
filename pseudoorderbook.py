from xy import exchange

#print(exchange({"x":100.0, "y":100.0}, 1, "x"))

pool = {"x":100.0, "y":100.0}
for item in range(0, 100):
    res = exchange(pool, 1, "x")
    print(res)
    pool = res[1]