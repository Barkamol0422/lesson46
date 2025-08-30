def fun1(n):
    sum=0
    for j in range(1,n+1):
        for i in range(1,j+1):
            sum+=1
    return sum
print(fun1(4))
