class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        f = [0] * (n + 1)  
        g = [0] * (n + 1)  

        f[0] = 1
        if n >= 1:
            f[1] = 1
            g[1] = 0

        for i in range(2, n + 1):
            g[i] = (g[i - 1] + f[i - 2]) % MOD
            f[i] = (f[i - 1] + f[i - 2] + 2 * g[i - 1]) % MOD

        return f[n]
