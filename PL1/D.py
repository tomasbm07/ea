import queue
from sys import stdin, stdout
from collections import deque

def readln():
    return stdin.readline().rstrip()

def outln(n):
    stdout.write(str(n))
    stdout.write('\n')
    

if __name__ == "__main__":
    
    #array = [0 for i in range(100000)]
    inserted  = 1
    pointer = 0
    x = 0
    
    array = deque([0])
    
    while True:
        instruction = readln().split(' ')
        
        if instruction == ['']:
            break
        
        if instruction[0] == "INSERT":
            if instruction[1] == 'RIGHT':
                #array.append(int(instruction[2]))
                pass
            else:
                #array.appendleft(int(instruction[2]))
                pass
            
        else: # Move
            if instruction[1] == 'RIGHT':
                pointer += 1
            else:
                pointer -= 1
    
    while x < inserted:
        outln(array[x])
        x += 1
    