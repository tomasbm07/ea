from sys import stdin, stdout

def readln():
    return stdin.readline().rstrip()

def outln(n: str):
    stdout.write(str(n))
    stdout.write('\n')


if __name__ == "__main__":
    x = readln().split(' ')
    a, b = int(x[0]), int(x[1])
    outln(f"{a*b}")


