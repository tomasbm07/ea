from sys import stdin, stdout
from pprint import pprint

t = 0
roots = set()


def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n) + "\n")


def AP(v, graph, low, dfs, parent):
    global t
    global roots

    low[v] = dfs[v] = t
    t += 1
    for i, w in enumerate(graph[v]):
        if w:
            if dfs[i] == -1:
                parent[i] = v
                AP(i, graph, low, dfs, parent)
                low[v] = min(low[v], low[i])
                if dfs[v] == 1 and dfs[i] != 2:
                    roots.add(v)
                if dfs[v] != 1 and low[i] >= dfs[v]:
                    roots.add(v)
            elif parent[v] != i:
                low[v] = min(low[v], dfs[i])


if __name__ == "__main__":
    while True:
        n = int(readln())

        if n == 0:
            break

        graph = [[False for _ in range(n)] for __ in range(n)]
        low = [-1 for _ in range(n)]
        dfs = [-1 for _ in range(n)]
        parent = [-1 for _ in range(n)]
        t = 1
        roots = set()

        for _ in range(n + 1):
            aux = list(map(int, readln().split()))
            # print(aux)
            if aux[0] == 0:
                # pprint(graph)
                AP(0, graph, low, dfs, parent)
                outln(len(roots))
                break
            else:
                aux = [i - 1 for i in aux]
                for i in aux[1:]:
                    graph[aux[0]][i] = True
                    graph[i][aux[0]] = True
