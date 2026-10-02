def solution(code):
    answer = ''
    code_list = []
    mode = 0
    
    for i in range(len(code)):
        
        if code[i] == '1':
            mode = (mode + 1)%2
        elif mode == 1:
            if i%2 !=0:
                code_list.append(code[i])
        else:
            if i%2 == 0:
                code_list.append(code[i])
    
    if len(code_list) == 0:
        return 'EMPTY'
    
    return ''.join(map(str, code_list))