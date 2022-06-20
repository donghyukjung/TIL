# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# 왼쪽, 오른쪽으로부터의 곱셈 결과를 저장
def sol(nums:list[int]):
    answer=[]
    p=1
    for i in range(0,len(nums)):
        answer.append(p)
        p=p*nums[i]
    p=1
    for i in range(len(nums)-1,0-1,-1):
        answer[i]=answer[i]*p
        p=p*nums[i]
    return answer

nums=[1,2,3,4]
print(sol(nums))