def check_if_possible(n, k, target, coins):
    # Create a 2D array to store whether it is possible to make change for each target
    dp = [[False for _ in range(target + 1)] for _ in range(k + 1)]
    
    # Base case: it is possible to make change for 0 cents with 0 coins
    dp[0][0] = True
    
    # Fill the remaining entries of the table using dynamic programming
    for i in range(1, k + 1):
        for j in range(1, target + 1):
            dp[i][j] = dp[i-1][j]
            if j >= coins[i-1]:
                dp[i][j] = dp[i][j] or dp[i][j-coins[i-1]]
    
    # Check if it is possible to make change for target cents with exactly k coins
    return dp[k][target]
