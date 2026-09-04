nums = [2, 7, 11, 15]
target = 13

def main(): 
    left = 0 
    right = len(nums)-1 

    while left<right : 
        TotalSum = nums[left] + nums[right]

        if TotalSum == target : 
            print(f"[{left}, {right}]")
            break

        elif TotalSum<target: 
            left+=1

        else: 
            right-=1











if __name__ == "__main__": 
    main()
