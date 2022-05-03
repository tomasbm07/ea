from sys import stdin, stdout

def readln():
    return stdin.readline().rstrip()

def outln(n):
    stdout.write(str(n))
    stdout.write("\n")
    
    

if __name__ == "__main__":
    time = 1
    n = int(readln())
    
    for i in range(n):
        x = readln().split(' ')
        a, b = int(x[0]), int(x[1])
        if a > time:
            time += a - time
        time += b
        
    outln(time)
        
        
        
