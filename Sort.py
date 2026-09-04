nums = [0, 1, 0, 3, 12]


def move_zeroes(nums):
    write = 0 
    zeros = 0 


    for i in range(len(nums)): 

    	if nums[i] != 0 : 
    		nums[write] = nums[i]
    		write+=1

    	zeros = len(nums) - write 
    	nums[i] = 0 

    print(nums)
    	
    		






move_zeroes(nums)