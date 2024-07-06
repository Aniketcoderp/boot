def somosa(n,k,shops):
    shops.sort()
    s=0
    count=0
    for i in range(n):
        if s>=k:
            break
        s+=shops[i]
        count+=1
    return count
n,k=4,10
shops=[5,4,2,4]
print(somosa(n,k,shops))