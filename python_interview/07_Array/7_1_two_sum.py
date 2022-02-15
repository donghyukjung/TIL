def sol1(arr:list[int], target:int)->list[int]:
    for i in range(len(arr)):
        for j in range(i+1,len(arr)-1):
            if arr[i]+arr[j]==target:
                return [i,j]
    
def sol2(arr:list[int], target:int)->list[int]:
    pass

def sol3(arr:list[int], target:int)->list[int]:
    pass

def sol4(arr:list[int], target:int)->list[int]:
    pass


arr=[2,7,11,15,3,8,5]
target = 9
print(sol1(arr,target))