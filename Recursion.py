
n = 0 
def sum_list(nums):

	if nums == []: 
		return 0

	return nums[n] + sum_list(nums[n+1:])
    

    	

   



nums = [4, 2, 7, 1, 9, 1]

print(sum_list(nums))