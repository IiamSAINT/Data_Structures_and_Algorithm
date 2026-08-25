nums = [-5, -2, -8, -1, -3]

# Find the contiguoug subarray with the largest value 


def largest_sum(num): 


	currentsum = num[0]
	maxsum = num[0]

	bestStart = 0 

	currentstart = 0 
	bestEnd = 0 


	for i in range(1, len(nums) ): 
		Sum = currentsum + nums[i]
		

		if nums[i] > currentsum + nums[i]:
			currentstart = i 
		currentsum = max(nums[i], Sum)
		

		if currentsum > maxsum:

			maxsum = max(maxsum, currentsum)
			bestStart = currentstart
			bestEnd = i




	return maxsum , bestStart, bestEnd




print(largest_sum(nums))