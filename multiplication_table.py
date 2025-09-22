def multiplication_table(n):
    for i in range (1,n+1):
        for r in range (1, n+1):
            return (i, "x", r, i*r)