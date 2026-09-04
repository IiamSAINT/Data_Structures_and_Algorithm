
string = "abcabcdbb"

letter = []




def main(): 

	isRunning = True 
	while isRunning:

		for i in string: 
			if letter.count(i) <1:
				letter.append(i)
			
		break


	print(len(letter) )



if __name__ == "__main__": 
	main()