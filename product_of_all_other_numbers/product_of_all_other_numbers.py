'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # make a new list with the length of given list to hold our products
    new_list = [None] * len(arr)

    # For each index, find the product of all other integers before it, storing the total
    # product as new index
    product_so_far = 1
    for i in range(len(arr)):
        new_list[i] = product_so_far
        product_so_far *= arr[i]

    product_so_far = 1
    for i in range(len(arr) - 1, -1, -1):
        new_list[i] *= product_so_far
        product_so_far *= arr[i]

    return new_list


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
