def minPartition(self, N):
        coin = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        dp = [None for i in range(N+1)]
        dp[0] = []
        for i in range(N+1):
            for j in coin:
                combination = [*dp[i], j]
                if i+j <= N:
                    if dp[i+j] is None or len(dp[i+j]) > len(combination):
                        dp[i+j] = combination
        ans = dp[N]
        return ans[::-1]