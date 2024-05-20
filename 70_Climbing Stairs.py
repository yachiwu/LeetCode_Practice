def climbStairs(n: int) -> int:
    steps = [0] * (n+1)
    if n<=2:
        return n
    # 1 steps have one way
    steps[1] = 1
    # two step have two way
    steps[2] = 2
    for i in range(3,n+1):
          # 走到n階的方法，就相當於走到n-1階的方法和走到n-2階的方法和
        steps[i] = steps[i-1]+ steps[i-2]
    return steps[n]    