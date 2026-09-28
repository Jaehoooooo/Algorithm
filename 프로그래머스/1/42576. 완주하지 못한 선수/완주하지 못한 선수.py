def solution(participant, completion):
    
    participant_dict = {}
    completion_dict = {}
    
    for i in participant:
        participant_dict[i] = participant_dict.get(i, 0) + 1
        
    for i in completion:
        completion_dict[i]= completion_dict.get(i,0) + 1
        
    for i in completion_dict:
        participant_dict[i] -= completion_dict[i]
        if participant_dict[i] == 0:
            participant_dict.pop(i)
    
    answer = ''.join(map(str,participant_dict))
    return answer