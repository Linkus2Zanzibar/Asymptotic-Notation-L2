def pn(n):
    a=0
    for i in range(0,n):
        for j in range(0,n):
            print("*", end=" ")
            a=a+1
        print("")
    print("when n is ",n," iterations=",a)
pn(5)
pn(3)
pn(4)