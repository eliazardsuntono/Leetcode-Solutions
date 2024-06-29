def solution1(nums, val):
    count = nums.count(val)
    for i in range(count):
        nums.remove(val)
        print(nums)
    
    return len(nums)

# My solution
def solution2(nums, val):
    k = 0
        
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = 101
        else:
            k += 1
    nums.sort()
    return k

if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    print(solution1(nums, val))
    
    