# Two-pointer
def sol1(arr:list[int])->int:
    left,right=0,len(arr)-1
    left_max, right_max=arr[left],arr[right]
    vol=0
    while left<right:
        left_max,right_max=max(left_max,arr[left]),max(right_max,arr[right])
        if left_max<right_max:
            vol+=left_max-arr[left]
            left+=1
        else:
            vol+=right_max-arr[right]
            right-=1
    return vol

# Stack
def sol2(arr:list[int])->int:
    stack=[]
    vol=0
    for i in range(len(arr)):
        while stack and arr[i]>arr[stack[-1]]:
            top=stack.pop()
            
            if not len(stack):
                break

            dist=i-stack[-1]-1
            waters=min(arr[i],arr[stack[-1]])-arr[top]
            vol+=dist*waters
        stack.append(i)
    return vol

arr=[0,1,0,2,1,0,1,3,2,1,2,1]
volume=sol2(arr)
print(volume)