def sol1(arr:list[int], target:int)->list[int]:
    for i in range(len(arr)):
        for j in range(i+1,len(arr)-1):
            if arr[i]+arr[j]==target:
                return [i,j]
    
def sol2(arr:list[int], target:int)->list[int]:
    nums_map={}
    for i,num in enumerate(arr):
        nums_map[num]=i
    for i ,num in enumerate(arr):
        if target-num in nums_map and i!=nums_map[target-num]:
            #자기자신인 경우 제외
            return [i,nums_map[target-num]]
    pass


arr=[2,7,11,15,3,8,5]
target = 9
print(sol1(arr,target))