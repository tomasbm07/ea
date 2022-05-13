from sys import stdin, stdout
from pprint import pprint


def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n) + "\n")


if __name__ == "__main__":
    n = int(readln())

    intersection_min = [float("-inf"), float("-inf"), float("-inf")]
    intersection_max = [float("inf"), float("inf"), float("inf")]
    for i in range(n):
        x, y, z, size = list(map(int, readln().split()))
        intersection_min[0] = max(intersection_min[0], x)
        intersection_min[1] = max(intersection_min[1], y)
        intersection_min[2] = max(intersection_min[2], z)

        intersection_max[0] = min(intersection_max[0], x + size)
        intersection_max[1] = min(intersection_max[1], y + size)
        intersection_max[2] = min(intersection_max[2], z + size)
    outln(
        max(0, intersection_max[0] - intersection_min[0])
        * max(0, intersection_max[1] - intersection_min[1])
        * max(0, intersection_max[2] - intersection_min[2])
    )
