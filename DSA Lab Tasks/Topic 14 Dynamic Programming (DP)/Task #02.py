#  Longest Common Subsequence
def lcs_memo(text1, text2):
    memo = {}
    
    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == len(text1) or j == len(text2):
            return 0
        if text1[i] == text2[j]:
            memo[(i, j)] = 1 + helper(i+1, j+1)
        else:
            memo[(i, j)] = max(helper(i+1, j), helper(i, j+1))
        return memo[(i, j)]
    
    return helper(0, 0)

def lcs_tabulation(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# Test
print("LCS length (memo):", lcs_memo("AGGTAB", "GXTXAYB"))
print("LCS length (tabulation):", lcs_tabulation("AGGTAB", "GXTXAYB"))