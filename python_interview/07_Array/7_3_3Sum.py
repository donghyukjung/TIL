# 정렬 후,기준(i)를 잡고 left, right를 잡고 
# 합이 0보다 작으면 left++, 0보다 크면 right--를 한다
# 찾은 경우에는, 두 포인터 동시에 움직인다
def sol(nums:list[int])->list[list[int]]:
    nums.sort()
    print(nums)
    answer=[]
    for i in range(len(nums)-2):
        # 중복된 숫자는 건너뛴다
        if i>0 and nums[i]==nums[i-1]:
            continue
        target=-nums[i]
        left,right=i+1, len(nums)-1
        while left<right:
            if nums[left]+nums[right]==target:
                answer.append([nums[i],nums[left],nums[right]])
                left+=1
                right-=1
            elif nums[left]+nums[right]>target:
                right-=1
            elif nums[left]+nums[right]<target:
                left+=1
    return answer
nums=[-1,0,1,2,-1,-4]
print(sol(nums))