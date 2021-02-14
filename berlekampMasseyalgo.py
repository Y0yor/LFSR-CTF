def berlekamp_Massey_algorithm(s):
    N = len(s)
    for k in range(N):
        if s[k] == 1:
            break
    f = set([k+1, 0])
    lo = k + 1
    g = set([0])
    a = k
    b = 0
    for n in range(k+1, N):
        d = 0
        for ele in f:
            d ^= s[ele+n-lo]
        if d == 0:
            b += 1
        else:
            if 2 * lo > n:
                f ^= set([a-b + ele for ele in g])
                b += 1
            else:
                temp = f.copy()
                f = set([b-a+ele for ele in f]) ^ g
                lo = n+1-lo
                g = temp
                a = b
                b = n-lo+1

    return list(f)
