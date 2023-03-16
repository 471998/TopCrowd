def connect_ropes(arr):
    arr.sort()
    sum=0
    for i in range(len(arr)-1):
        b=arr[i]+arr[i+1]
        sum+=b
        arr[i+1]=b
    return sum
arr=[5,4,2,8]
print(connect_ropes(arr))
