from sys import stdin, stdout

# from time import time
from pprint import pprint


def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n))
    stdout.write("\n")


def guards(objects, m, n):
    guards = [0 for _ in range(n)]

    i = 0
    guards[0] = objects[0] + m
    
    for j in range(1, n):
        if objects[j] > guards[i] + m:
            guards[i + 1] = objects[j] + m
            i += 1
    return i + 1


if __name__ == "__main__":
    # start = time()

    for _ in range(int(readln())):
        # n -> number of objects to guard
        # m -> depth of vision
        n, m = list(map(int, readln().split()))

        objects = sorted([int(readln()) for i in range(n)])

        # pprint(objects)

        outln(guards(objects, m, n))

    # outln(time() - start)
