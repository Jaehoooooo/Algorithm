def solution(answers):
    
    answer = []
    
    a = [1,2,3,4,5]*2000
    b = [2,1,2,3,2,4,2,5]*1250
    c = [3,3,1,1,2,2,4,4,5,5]*1000
    
    a_cnt = 0
    b_cnt = 0
    c_cnt = 0
    
    for i in range(len(answers)):
        if answers[i] == a[i]:
            a_cnt += 1
        if answers[i] == b[i]:
            b_cnt += 1
        if answers[i] == c[i]:
            c_cnt += 1
    
    best_cnt = max(a_cnt, b_cnt, c_cnt)
    
    if best_cnt == a_cnt:
        answer.append(1)
    if best_cnt == b_cnt:
        answer.append(2)    
    if best_cnt == c_cnt:
        answer.append(3)
        
    return answer