from math import floor
from sys import stdin, stdout

# from time import time
# from pprint import pprint


def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n))
    stdout.write("\n")


def pizza(n, cooking_time):
    cooking_time = [0] + cooking_time
    T = sum(cooking_time)
    aux = floor(T / 2)
    cache = [[True if _ == 0 else False for _ in range(aux + 1)] for __ in range(n + 1)]
    total = 0

    # pprint(cache)

    for i in range(n + 1):
        for j in range(aux + 1):
            if cooking_time[i] > j:
                cache[i][j] = cache[i - 1][j]
            else:
                cache[i][j] = cache[i - 1][j] or cache[i - 1][j - cooking_time[i]]

    # pprint(cache)

    for i in range(aux, -1, -1):
        # print(f"i = {i}, n = {n-1}")
        if cache[n][i] == True:
            x = n
            y = i
            while x > 0:
                if cache[x - 1][y] != True:
                    total += cooking_time[x]
                    y -= cooking_time[x]
                x -= 1

            return T - 2 * total


if __name__ == "__main__":
    # start = time()

    while True:
        try:
            n = int(readln())
        except:
            break

        cooking_time = [int(readln()) for _ in range(n)]

        outln(pizza(n, cooking_time))

    # outln(time() - start)
