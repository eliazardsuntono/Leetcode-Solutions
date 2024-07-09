def solution1(nums):
        for i in range (len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

if __name__ == "__main__":
	test = [0,1,3,-1,2]
	solution1(test)
	print(test)
