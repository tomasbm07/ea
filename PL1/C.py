from sys import stdin, stdout

def readln():
    return stdin.readline().rstrip()

def outln(n: str):
    stdout.write(str(n))


if __name__ == "__main__":
    array = []
    counter = 0
    
    while True:
        try:
            x = int(readln())
            array.append(x)
        except:
            array.sort()
            break
    
    for i in array:
        if counter == len(array) - 1:
            outln(i)
            outln('\n')
        else:
            outln(i)
            outln('\n')
            counter += 1
