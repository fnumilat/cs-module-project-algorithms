'''
Input: a List of integers
Returns: a List of integers
'''
# First Pass Solution
# def moving_zeroes(arr):
#     # Your code here
#     # create two arrays, (left and right) to hold the numbers when they are separated
#     left = []
#     right = []
#     # iterate through the array of the numbers and 
#     # see if the number is equal to zero then add it to the right array
#     # and if not add it to the left array
#     for num in arr:
#         if num == 0:
#             right.append(num)
#             print(left, "left", right, "right")
#         else:
#             left.append(num)
#             print(left, "left", right, "right")
#     # return both (left and right) arrays merged
#     return left + right

# Better Solution
def moving_zeroes(arr):
    start = 0
    end = len(arr)-1
    for _i in range(end):
        if arr[start] == 0:
            arr.append(0)
            del arr[start]
            end -=1
        else:
            start+=1
    
    return arr

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")