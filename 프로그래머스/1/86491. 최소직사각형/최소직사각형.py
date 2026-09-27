def solution(sizes):
    
    max_w = 0
    max_h = 0
    
    for i in sizes:
        if i[0] < i[1]:
            a = i[0]
            i[0] = i[1]
            i[1] = a
        
        if max_w < i[0]:
            max_w = i[0]
        if max_h < i[1]:
            max_h = i[1]
            
    answer = max_h*max_w
    
    return answer