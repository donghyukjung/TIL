def solver(nums:list[int]):
    nums.sort()
    sum=0
    for i in range(len(nums)):
        if i%2==0:
            sum+=nums[i]
    return sum

def sol(nums:list[int]):
    return sum(sorted(nums)[::2])
    #[::2] : 2칸씩 건너뜀(슬라이싱)
nums=[1,4,3,2]
print(sol(nums))