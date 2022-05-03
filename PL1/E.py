from sys import stdin, stdout

def readln():
    return stdin.readline().rstrip()

def outln(n):
    stdout.write(str(n))
    stdout.write('\n')
    

if __name__ == "__main__":
    n = int(readln())
    for i in range(n):
        stack = []
        x = readln().split(' ')
        for p in x:
            try:
                stack.append(int(p))
            except:
                a = stack.pop()
                b = stack.pop()
                if p == '+':
                    stack.append(b + a)
                else:
                    stack.append(b - a) 
        print(stack[0])

    
