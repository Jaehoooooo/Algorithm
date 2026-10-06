def solution(l, r):
    answer = []
    result = []
    
    for i in range(l, r+1):
        result = ''.join(map(str, f'{i}'))
        cnt = 0
        for j in result:
            if j == "0" or j == "5":
                cnt += 1
            else:
                break
            
            if cnt == len(result):
                answer.append(int(result))
    
    answer = list(set(answer))
    answer.sort()
    
    if answer == []:
        return [-1]
    
    return answer