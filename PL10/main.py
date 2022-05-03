from sys import stdin, stdout
from pprint import pprint
from math import sqrt


def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n) + "\n")


def distance(computers, a, b):
    return sqrt(
        abs(computers[a][0] - computers[b][0]) ** 2
        + abs(computers[a][1] - computers[b][1]) ** 2
    )


def find_set(set, i):
    if set[i] == i:
        return i
    return find_set(set, set[i])


def union_set(set, rank, x, y):
    a = find_set(set, x)
    b = find_set(set, y)

    if rank[a] > rank[b]:
        set[b] = a
    elif rank[a] < rank[b]:
        set[a] = b
    else:
        set[a] = b
        rank[b] += 1


def kruskal(graph, n, union_find):
    i, e = 0, 0
    set = []
    rank = []

    # Sort based on weight
    graph = sorted(graph, key=lambda item: item[2])

    # Initialize set and rank
    for node in range(n):
        set.append(node)
        rank.append(0)

    # Add known sets
    for a, b, _ in union_find:
        e += 1
        union_set(set, rank, a, b)

    union_find = []

    while e < n - 1:
        u, v, w = graph[i]
        i += 1
        x = find_set(set, u)
        y = find_set(set, v)
        if x != y:
            e += 1
            union_find.append([u, v, w])
            union_set(set, rank, x, y)

    return union_find


if __name__ == "__main__":

    while True:
        try:
            n = int(readln())
            graph = []
            union_find = []
            computers = []
            sum = 0
            distances = [
                [0 for _ in range(n)] for __ in range(n)
            ]  # guardar distancias. para n ter de as calcular novamente

            # Read pc coordinates
            for i in range(n):
                computers.append(list(map(int, readln().split())))

            # Calculate distance between them
            for i in range(n):
                for j in range(i + 1, n):
                    d = distance(computers, i, j)

                    distances[i][j] = d
                    distances[j][i] = d
                    graph.append([i, j, d])
                    graph.append([j, i, d])

            # pprint(graph)

            # Set Union-Find structure with already connected pc's
            for i in range(int(readln())):
                a, b = list(map(int, readln().split()))
                a -= 1
                b -= 1
                union_find.append([a, b, distances[a][b]])

            # Do Kruskal algorithm
            union_find = kruskal(graph, n, union_find)

            # pprint(union_find)

            for i in union_find:
                sum += i[2]

            print(f"{sum:.2f}")

        except:
            break
