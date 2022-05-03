from sys import stdin, stdout

def readln():
    return stdin.readline().rstrip()

def outln(n: str):
    stdout.write(str(n))
    stdout.write('\n')


def check_array(array, n):
    
    array.sort()
    #print(n, array)
    for i in range(len(array) - 2) :
        j = i + 1
        k = n - 1
        while j < k:
            #print(i, j, k)
            sum = array[i] + array[j] + array[k]
            if sum == 0:
                return True
            elif sum < 0:
                j += 1
            else:
                k -= 1     
    return False


if __name__ == "__main__":
    array = []
    x = 0
    n = int(readln())
    
    while True:
        try:
            x = int(readln())
        except:
            break
        
        if x != 0:
            array.append(x) 
        else:
            result = check_array(array, n)
            if result is True:
                print('Fair')
            else:
                print('Rigged')

            array = []
            n = readln()
            if n == '':
                break
            else:
                n = int(n)
