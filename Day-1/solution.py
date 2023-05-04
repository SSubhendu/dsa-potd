def maxCoins(n, ranges):
    # sort the ranges by their start index
    ranges.sort(key=lambda x: x[0])
    
    # initialize max coins to 0
    max_coins = 0
    
    # loop through each range
    for i in range(n):
        # select the current range as the first range
        coins1 = ranges[i][2]
        
        # initialize the second range to None
        coins2 = 0
        j = i + 1
        
        # find the second range that doesn't overlap with the first range
        while j < n and ranges[j][0] <= ranges[i][1]:
            j += 1
        
        # if a second range was found, select it and update the maximum coins
        if j < n:
            coins2 = ranges[j][2]
            max_coins = max(max_coins, coins1 + coins2)
        
        # check for a second range that only touches the first range
        if j < n-1 and ranges[j+1][0] == ranges[i][1]+1:
            coins2 = ranges[j+1][2]
            max_coins = max(max_coins, coins1 + coins2)
            
    return max_coins
