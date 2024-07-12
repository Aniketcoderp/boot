def marge(a,b,n):
    i=0
    j=0
    r=[]
    while i<n and j<n:
        if a[i]<=b[j]:
            r.append(a[i])
            i+=1
        else:
            r.append(b[j])
            j+=1
    while i<n:
        r.append(a[i])
        i+=1
    while j<n:
        r.append(b[j])
        j+=1
    print(*r)

n=4
a=[1,5,7,9]
b=[2,4,6,8]
marge(a,b,n)

         