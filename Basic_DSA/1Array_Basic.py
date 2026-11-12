######## Basic Template to take input ############

# def get_integer(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print("Invalid input. Please enter a valid integer.")


# def get_input():
#     arr_len = get_integer("Enter the array length: ")

#     if arr_len < 0:
#         print("Array length cannot be negative.")
#         return get_input()

#     user_arr = []

#     for i in range(arr_len):
#         value = get_integer(f"Enter {i + 1} value: ")
#         user_arr.append(value)

#     print("Entered array:", user_arr)

#     k = get_integer("Enter the value of right shift: ")
#     print("Right shift:", k)

#     return user_arr, k



# 1. Find the maximum and minimum elements:
# Approaches:
# 1. sort then fetch first and last element = O(nlogn)
# 2. While iterating use two variable for max and min = O(n)
# 3. using built in min() and max() = O(nlogn)


# 2. Reverse an array:
# Approaches:
# 1. Using two pointer = O(n/2) = o(n)
# 2. using reverse slicing = O(n)
# 3. Using list.reverse() = O(n) = in-place
# 4. Using Reversed(list) class = O(1) because it yield the values and return an iterator.Although while consuming O(n).


# 3. Check if an array is sorted:
# Approach:
# 1. While iterating Keep checking the next element , if any of them is smaller not sorted. 


# 4. Rotate an array by k positions to right side:
# 4. Rotate an array by k positions:
# Approaches:
# 1. Remove the last element of the array one by one and insert it at the beginning, repeating this process k times. This effectively performs a right rotation by k positions.use insert and pop methods.

