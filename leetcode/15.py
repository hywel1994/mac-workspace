def new21Game(N, K, W):
    """
    :type N: int
    :type K: int
    :type W: int
    :rtype: float
    """
    dp = [0.0] * (N + W + 1)
    # dp[x] = the answer when Alice has x points
    for k in range(K, N + 1):
        dp[k] = 1.0

    S = min(N - K + 1, W)
    # S = dp[k+1] + dp[k+2] + ... + dp[k+W]
    for k in range(K - 1, -1, -1):
        print (S)
        dp[k] = S / float(W)
        S += dp[k] - dp[k + W]
        print (dp)
        

    return dp[0]


new21Game(9,6,5)