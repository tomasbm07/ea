from sys import stdin, stdout

def readln():
    return stdin.readline().rstrip()

def outln(n):
    stdout.write(str(n))
    stdout.write("\n")
    

if __name__ == "__main__":
    shoes = [-1 for i in range(200000)]
    
    while True:
        found_match = False
        backup = 200000
        consecutive = 0
        pointer = 0 
        
        x = readln().split(' ')
        if x[0] == 'ADD':
            shoes[pointer] = int(x[1])
            pointer +=  1

        elif x[0] == 'REQUEST':
            r = int(x[1])
            
            print(f"REQUEST {r}, shoes = {shoes[:10]}")
            for i in range(len(shoes)):
                if shoes[i] == -1:
                    consecutive += 1
                else:
                    consecutive = 0
                
                if consecutive == 5:
                    break
                    
                if r == shoes[i]:
                    backup = r
                    found_match = True
                    shoes.pop(i)
                    pointer = i
                    break
                elif shoes[i] > r and backup > shoes[i]:
                        backup = shoes[i]
                        j = i
                        found_match = True
                
                if i == len(shoes) - 1 and found_match:
                    shoes.pop(j)
            
            #print(f"imposible = {impossible}, backup = {backup}")
            if found_match:
                outln(backup)
            else:
                outln('impossible')
                                             
        else:
            break
        