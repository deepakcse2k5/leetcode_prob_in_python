nums =[1,2,2,3,4,4]

# print(nums.remove(2))


def remove_duplicates(nums):
    if not nums:
        return 0
    slow =0
    for fast in range(1,len(nums)):
        if nums[slow]!=nums[fast]:
            slow+=1
            nums[slow]= nums[fast]
        
    return slow+1


print(remove_duplicates(nums))