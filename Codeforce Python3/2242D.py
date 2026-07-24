def solve():
    s = input().strip()
    t = input().strip()

    n = len(s)
    m = len(t)

    ps = [0] * (n + 1)
    pt = [0] * (m + 1)

    for i in range(n):
        ps[i + 1] = (ps[i] + int(s[i])) % 10

    for i in range(m):
        pt[i + 1] = (pt[i] + int(t[i])) % 10

    n += 1
    m += 1

    if ps[-1] != pt[-1]:
        print(-1)
        return

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i < n:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j < m:
                dp[i][j + 1] = max(dp[i][j + 1], dp[i][j])
            if i < n and j < m and ps[i] == pt[j]:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)

    print(dp[n][m] - 1)


T = int(input())
for _ in range(T):
    solve()