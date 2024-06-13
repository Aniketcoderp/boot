def quick(arr,low,high):
    if low<high:
        pi=parti(arr,low,high)
        quick(arr,low,pi-1)
        quick(arr,pi+1,high)
def parti(arr,low,high):
    pv=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j] <=pv:
            i+=1
            arr[i],arr[j]=arr[j],[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
arr=[3,5,0,9,8]
n=5
quick(arr,0,n-1)
print(arr)
