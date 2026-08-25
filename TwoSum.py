nums = [2, 7, 11, 15]

target = 26



def Two_Sum(nums, target): 

	seen= {}


	for i, num in enumerate(nums): 

		Sum = target - num 


		if Sum in seen: 

			print(f"Found -> {i} {seen[Sum]}") 

		seen[num] = i 

	print(list(seen.items()))


Two_Sum(nums, target)




