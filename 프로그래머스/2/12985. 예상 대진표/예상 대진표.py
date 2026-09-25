import math

def solution(n,a,b):

    N = round(math.log(n,2))
    num = 0

    
    for i in range(N,0, -1):
        a=int((a+1)//2)
        b=int((b+1)//2)
        if (b-a) == 0:
            num += 1
            break
        else:
            num += 1
    
    return num