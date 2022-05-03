from sys import stdin, stdout

def readln():
    return stdin.readline().rstrip()

def outln(n: str):
    stdout.write(str(n))


if __name__ == "__main__":
    n = int(readln())
    array = readln().split(' ')
    counter = 0
    
    for i in array[::-1]:
        if counter == n - 1:
            outln(i + '\n')
        else:
            outln(i + ' ')
            counter += 1
    