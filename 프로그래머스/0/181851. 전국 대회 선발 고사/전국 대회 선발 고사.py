def solution(rank, attendance):
    
    answer = 0
    rank_list = []
    
    for i in range(len(rank)):
        if attendance[i]:
            rank_list.append((rank[i],i))
    
    rank_list.sort()

    answer = 10000*rank_list[0][1] + 100*rank_list[1][1] + rank_list[2][1]

    return answer