def solution(q, r, code):
    
    code_list = list(map(str, code))
    answer = []
    
    for i in range(len(code_list)):
        if (i % q) == r:
            answer.append(code_list[i])
        
    answer = ''.join(map(str,answer))
    return answer