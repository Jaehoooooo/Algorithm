import sys

input = sys.stdin.readline

def solution(n):
    mod = 1000000007
    
    if n%2 == 0:
        
        d = [0]*(n+1)
        d[0] = 1
        d[2] = 3
        
        for i in range(4, n+1, 2):
            d[i] = (4*d[i-2] - d[i-4]) % mod
        
    else:
        anw = 0
        
    
    return d[i]