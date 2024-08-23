from typing import List

def solution(cost: List[int]) -> int:
    n = len(cost)
    dp = [0] * n
    dp[0], dp[1] = cost[0], cost[1]
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    return min(dp[-1], dp[-2])

if __name__ == "__main__":
    print(solution([10, 15, 20])) # Expected 15
    print(solution([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])) # Expected 6
    