class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minimum_length = float("inf")
        memo = {}

        def dfs(total):
            if total in memo:
                return memo[total]
            if total > amount:
                return float("inf")
            if total == amount:
                return 0  # Found a valid way to reach amount
            
            min_coins = float("inf")
            for coin in coins:
                num_coins = 1 + dfs(total + coin)
                min_coins = min(min_coins, num_coins)

            memo[total] = min_coins
            return min_coins

        result = dfs(0)
        return result if result != float("inf") else -1