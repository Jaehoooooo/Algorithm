def solution(numbers, target):
    
    def dfs(idx, current_sum):
        
        if idx == len(numbers):
            if current_sum == target:
                return 1
            return 0
        
        plus = dfs(idx+1, current_sum + numbers[idx])
        minus = dfs(idx+1, current_sum - numbers[idx])
        
        return plus + minus
    
    return dfs(0,0)