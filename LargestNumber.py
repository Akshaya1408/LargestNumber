def largest_number(arr):
    sd=[]
    for i in range(len(arr)):
        if arr[i]>9:
            while arr[i]>0:
                sd.append(str(arr[i]%10))
                arr[i]//=10
        else:
            sd.append(str(arr[i]))
            
    sd.sort(reverse=True)
    return "".join(sd)

arr=list(map(int, input().split()))
print(largest_number(arr))
