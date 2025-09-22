def multiplication_table(n):
    for i in range (1,n+1):
        for r in range (1, n+1):
            print(str(i) + " x " + str(r) + " = " + str(i * r))

multiplication_table(5)