def quick(arr,l,h):
    if l<h:
        pi=parti(arr,l,h)
        quick(arr,l,pi-1)
        quick(arr,pi+1,h)
def parti(arr,l,h):
    pivot=arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1
n=5
arr=[3,5,0,9,8]
quick(arr,0,n-1)
print(arr)