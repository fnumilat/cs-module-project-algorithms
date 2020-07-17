'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# def single_number(arr):
#     # Your code here
#     # create an array to hold the single number
#     single = []
#     # iterate through numbers
#     for target in arr:
#         # check to see if the target is already in the created array
#         if target not in single:
#             single.append(target)
#         # if it is, remove it from array
#         else:
#             single.remove(target)
#     # when iteration is done, the only number in the array is the odd number out
#     # return odd number
#     return single[0]

# Better Solution
def single_number(arr):
    arr.sort()
    for i in range(0, len(arr), 2):
        if arr[i] + arr[i+1] - arr[i] != arr[i]:
            return arr[i]

   


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")