from sys import stdin, stdout
# from time import time


def readln():
    return stdin.readline().rstrip()


def outln(n: str):
    stdout.write(str(n))
    stdout.write("\n")


def chess(x, y, m):
    if m < 0:
        return 0

    if cache.get((x, y), -1) > m:
        return 0
    cache[(x, y)] = m

    counter = 0

    if board[x + 200][y + 200] is False:
        board[x + 200][y + 200] = True
        counter = 1

    return (
        counter
        + chess(x + 2, y - 1, m - 1)
        + chess(x + 2, y + 1, m - 1)
        + chess(x + 1, y + 2, m - 1)
        + chess(x - 1, y + 2, m - 1)
        + chess(x - 2, y + 1, m - 1)
        + chess(x - 2, y - 1, m - 1)
        + chess(x - 1, y - 2, m - 1)
        + chess(x + 1, y - 2, m - 1)
    )


if __name__ == "__main__":

    board = [[False for _ in range(401)] for __ in range(401)]
    # (x, y): m -> fica guardado o numero de jogadas de cada cavalo que passou em x, y
    # se ja tiver passado em x, y um cavalo com 6 jogadas e passar outro com 3, podemos sair pq vai repetir as mesmas casas
    cache = {}
    c = 0

    for _ in range(int(readln())):
        # start = time()
        x, y, m = list(map(int, readln().split()))
        c += chess(x, y, m)

    # print(time() - start)

    outln(c)
