def solution(n, lost, reserve):
    
    answer = 0
    
    student = [0]*(n+1)
    
    for i in range(1,n+1):
        if i in lost and i in reserve:
            student[i] = 1
            lost.remove(i)
            reserve.remove(i)
            
    
    for i in range(1,n+1):
        # if i in lost and i in reserve:
        #     # student[i] = 1
        #     lost.remove(i)
        #     reserve.remove(i)
        if i not in lost:
            student[i] = 1
        if i in lost:
            if (i-1) in reserve: 
                student[i] = 1
                reserve.remove(i-1)
            elif (i+1) in reserve:
                student[i] = 1
                reserve.remove(i+1)
    answer = sum(student)
    return answer