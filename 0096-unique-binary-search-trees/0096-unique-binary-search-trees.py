
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = 0
            for j in range(1, i + 1):
                left = dp[j - 1]
                right = dp[i - j]
                dp[i] += left * right
        return dp[n]

        