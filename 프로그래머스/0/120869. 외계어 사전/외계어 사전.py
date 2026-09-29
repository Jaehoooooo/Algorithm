def solution(spell, dic):
    

    answer = 2
    
    for i in dic:
        dic_dict = {}

        dict_list = list(map(str, i))
        for j in spell:
            if j in dict_list:
                dic_dict[j] = dic_dict.get(j, 0) + 1
            else:
                dic_dict[j] = dic_dict.get(j, 0)
        
        if all(v ==1 for v in dic_dict.values()):
            return 1
            break
        else:
            answer = 2
                
                
    return answer