pool = {"x":100.0, "y":100.0}

def exchange(pool_before, size, asset):
    pool_after = {}
    if asset == "x":
        pool_after["x"] = pool_before["x"] + size
        pool_after["y"] = (pool_before["y"] * pool_before["x"]) / pool_after["x"]
        change_result = pool_after["y"] - pool_before["y"]
    else:
        pool_after["y"] = pool_before["y"] + size
        pool_after["x"] = (pool_before["x"] * pool_before["y"]) / pool_after["y"]
        change_result = pool_after["x"] - pool_before["x"]
    return (change_result, pool_after)

print(exchange(pool, 1, "x"))
