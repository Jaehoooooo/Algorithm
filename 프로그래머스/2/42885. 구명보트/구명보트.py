from collections import deque

def solution(people, limit):
    answer = 0

    people.sort()
    people = deque(people)
    
    while people:
        # print(people)
        heavy = people.pop()
        answer += 1
        
        for i in people:
            if (heavy + i) <= limit:
                people.popleft()
                # answer += 1
                break
            else:
                # answer += 1
                break                
                
    return answer