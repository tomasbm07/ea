from sys import stdin, stdout

# from time import time
from pprint import pprint
from collections import deque


def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n))
    stdout.write("\n")


def train_timetable(connections, n):
    Q = deque()
    color = [-1 for _ in range(n)]

    color[0] = 1
    Q.append(0)
    while len(Q) != 0:
        t = Q.popleft()
        for i in connections[t]:
            if color[i] == -1:
                color[i] = 1 - color[t]
                Q.append(i)
            elif color[i] == color[t]:
                return False
    return True


if __name__ == "__main__":
    # start = time()

    while True:
        try:
            n, m = list(map(int, readln().split()))
            connections = [[] for _ in range(n)]

            for _ in range(m):
                x, y = list(map(int, readln().split()))
                connections[x - 1].append(y - 1)
                connections[y - 1].append(x - 1)

            outln("NOT SURE") if train_timetable(connections, n) else outln("NO")
        except:
            break

        # pprint(connections, width=140, compact=False)

    # outln(time() - start)
