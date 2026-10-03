def solution(data, ext, val_ext, sort_by):
    answer = []
    
    feature = ['code', 'date', 'maximum', 'remain']
    
    if ext == 'code':
        ext = 0
    elif ext == 'date':
        ext = 1
    elif ext == 'maximum':
        ext = 2
    elif ext == 'remain':
        ext = 3
        
    if sort_by == 'code':
        sort_by = 0
    elif sort_by == 'date':
        sort_by = 1
    elif sort_by == 'maximum':
        sort_by = 2
    elif sort_by == 'remain':
        sort_by = 3
    
    for i in data:
        if i[ext] < val_ext:
            answer.append(i)
    
    answer.sort(key=lambda x:x[sort_by])
    
    return answer