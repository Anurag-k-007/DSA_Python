ex=[5,3,3,2,1,1,3]
out=[0]*len(ex)
ci=[0]*(m+1)
cf=[0]*(m+1)
m=max(ex)

#counting the ocuurences of each element
for elem in set(ex):
    ci[elem]=ex.count(elem)

#cumulative frequency of each element
for i in range (0,m+1):
    for j in range(0,i+1):
        cf[i]=cf[i]+ci[j]

# updating the position of elements based on cumulative frequency
while m>0:
    c=ci[m]
    while c>0: # Checks if element is present more than once
        out[cf[m]-1]=m
        c=c-1
        cf[m]=cf[m]-1
    m=m-1
print(out)

