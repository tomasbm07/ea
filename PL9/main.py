from sys import stdin, stdout
from pprint import pprint

# from time import time


def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n) + "\n")


def min_distance(distance, queue, n):
    minimum = float("inf")  # Inicialize as infite
    min_index = -1

    for i in range(n):
        if distance[i] < minimum and i in queue:
            minimum = distance[i]
            min_index = i

    return min_index


# Djikstra algorithm with adjancency matrix with wights
def shortest_path(graph, n, end):
    distance = [float("inf") for _ in range(n)]  # Set distance to all nodes as infinite
    distance[0] = 0  # Set start node distance to itself -> 0

    # Add all vertices to a queue
    queue = []
    for i in range(n):
        queue.append(i)

    # Update distance from source to all vertices
    while queue:
        u = min_distance(distance, queue, n)
        queue.remove(u)

        for i in range(n):
            if graph[u][i] and i in queue:
                if distance[u] + graph[u][i] < distance[i]:
                    distance[i] = distance[u] + graph[u][i]

    outln(distance[end])


if __name__ == "__main__":
    # start = time()
    # outln(time() - start)

    n, end = list(map(int, readln().split()))
    n -= 1
    end -= 1

    graph = [[0 for __ in range(n + 1)] for _ in range(n + 1)]

    for _ in range(n + 1):
        aux = list(map(int, readln().split()))
        x = aux[0] - 1
        aux = aux[1:]
        # print(aux)
        for i in range(len(aux)):
            if aux[i] != -1:
                graph[x][i] = aux[i]
                graph[i][x] = aux[i]
                
    pprint(graph)

    shortest_path(graph, n + 1, end)
