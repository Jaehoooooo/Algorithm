from functools import cmp_to_key

def solution(numbers):
    
    numbers = list(map(str, numbers))
    
    def compare(a,b):
        if int(a+b) > int(b+a):
            return -1
        return 1
    
    numbers.sort(key=cmp_to_key(compare))
        
    if numbers[0] == '0':
        return "0"
    
    return "".join(map(str, numbers))