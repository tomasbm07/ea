from sys import stdin, stdout
from time import time

cost = []
nlig = []
visited = []
best = 0
n = 0


def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n))
    stdout.write("\n")


def net(v, c):
    global best

    if c >= best:
        return

    if v == n:
        best = c
        return

    for i in range(n):
        if visited[i] and nlig[i] < k:
            for j in range(n):
                if not visited[j]:
                    if cost[i][j] > 0:
                        nlig[i] += 1
                        nlig[j] += 1
                        visited[j] = True
                        net(v + 1, c + cost[i][j])
                        nlig[i] -= 1
                        nlig[j] -= 1
                        visited[j] = False


if __name__ == "__main__":

    start = time()
    
    while True:
        try:
            n, m, k = list(map(int, readln().split()))
        except:
            break

        cost = [[0 for _ in range(n)] for __ in range(n)]
        nlig = [0 for _ in range(n)]
        visited = [False for _ in range(n)]
        best = 100000000

        visited[0] = True

        for _ in range(m):
            x, y, c = list(map(int, readln().split()))
            cost[x - 1][y - 1] = c
            cost[y - 1][x - 1] = c

        net(1, 0)
        outln(best) if best != 100000000 else outln("NO WAY!")
    
    outln(time() - start)
