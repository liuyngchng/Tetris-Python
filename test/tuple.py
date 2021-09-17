def tuple1():
    x = 10
    y = 20
    return x, y


def tuple2():
    a = 1
    b = 2
    return (a, b)


if __name__ == "__main__":
    import pdb;pdb.set_trace()
    print(tuple1(), type(tuple1()))
    print(tuple2(), type(tuple2()))
