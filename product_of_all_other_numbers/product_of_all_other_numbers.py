'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    # create an array that will contain the numbers product
    products = []
    # iterate through array
    for i in range(len(arr)):
        # use placeholder value
        value = 1
        # iterate through the array again for the current index, then multiply all other values together
        for j in range(len(arr)):
            # check if the index is a different number
            if i is not j:
                value *= arr[j]
        products.append(value)

    return products

    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
