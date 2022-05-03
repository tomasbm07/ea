from math import floor
from sys import stdin, stdout

# from time import time
from pprint import pprint


def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n))
    stdout.write("\n")


def unsocial_network(v, size, connections):
    global n
    global best
    global neighbor
    
    if size > best:
        best = size

    ub = 0
    for i in range(v + 1, n):
        if neighbor[i] == 0:
            ub += 1
    if size + ub <= best:
        return

    for i in range(v + 1, n):
        if (i, v) in connections:
            neighbor[i] = neighbor[i] + 1
    for i in range(v + 1, n):
        if neighbor[i] == 0:
            unsocial_network(i, size + 1, connections)
    for i in range(v + 1, n):
        if (i, v) in connections:
            neighbor[i] = neighbor[i] - 1

    #return best


if __name__ == "__main__":
    # start = time()

    # number of people, number of connections
    n, m = list(map(int, readln().split()))

    connections = []
    neighbor = [0 for _ in range(n)]
    best = 0

    for i in range(m):
        x, y = list(map(int, readln().split()))
        connections.append((x, y))
        connections.append((y, x))

    for i in range(n):
        unsocial_network(i, 0, connections)

    outln(best+1)

    # pprint(connections, width=140, compact=False)

    # outln(time() - start)
