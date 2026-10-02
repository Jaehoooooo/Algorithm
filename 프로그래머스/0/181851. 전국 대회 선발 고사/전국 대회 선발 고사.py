def solution(rank, attendance):
    
    answer = 0
    rank_list = []
    
    for i in range(len(rank)):
        if attendance[i]:
            rank_list.append(rank[i])
    
    rank_list.sort()
    cnt = 2
    for i in range(len(rank_list)):
        while cnt >= 0:
            for j in range(len(rank)):
                if rank[j] == rank_list[i]:
                    answer += j*(100**cnt)
                    cnt -= 1
                    break
            break

    return answer