arr = [1, 3, 5, 7, 9, 11, 15, 20]



# BINARY SEARCH 


def binary_search(arr, target): 

	Min = 0 
	Max = len(arr)  - 1 



	while Min <= Max:
		mid = (Max + Min) // 2

		if arr[mid] == target: 
			return mid
			break

		elif arr[mid] > target: 
			Max = mid - 1  

		elif arr[mid] < target: 
			Min = mid + 1
		else: 
			return -1
			break 





print(binary_search(arr, 15))