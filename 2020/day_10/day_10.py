with open("test/test_0.txt") as f:
    jolts = [int(x) for x in f.read().splitlines()]
