def solution(phone_number):
    answer = ''
    
    phone_len = len(phone_number)
    
    answer_star = phone_number[:-4]
    answer_star = len(answer_star)
    
    answer = '*'*answer_star + phone_number[phone_len-4:]
        
    
    return answer