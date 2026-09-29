def solution(spell, dic):
    
    answer = 2
    
    for i in dic:
        dic_dict = {}
        for j in spell:
            if j in i:
                dic_dict[j] = dic_dict.get(j, 0) + 1
            else:
                dic_dict[j] = dic_dict.get(j, 0)
                
        if all(v == 1 for v in dic_dict.values()):
            answer = 1
            break
        else:
            anwser = 2
            
                
    return answer