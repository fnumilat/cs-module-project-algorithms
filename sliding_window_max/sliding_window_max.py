'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # iterate through array with two pointers
        # start is going to be 0
        # end is going to be k-1
        # find the max in that range
        # push max to a new array
        # increment start and end until end is equal to end of the array
    start = 0
    end = k-1
    maxes_array = []

    for i in range(len(nums)):
        if end < len(nums):
            start = i
            greatest = nums[i]
            for j in range(start, end+1):
                if nums[j] > greatest:
                    greatest = nums[j]
            maxes_array.append(greatest)
            end +=1
        print('one loop complete',i)
    return maxes_array


    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
