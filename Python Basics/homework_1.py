import random


# Generate a list of 100 random numbers from 0 to 1000
def generate_random_numbers():
    return [random.randint(0, 1000) for i in range(100)]


# Bubble Sort implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):  # n - i represents the number of elements that still need to be compared in each pass, and we subtract 1 because we want to avoid accessing an out-of-range index.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # This swapping operation ensures that the larger elements goes to the end of the list with each pass through the list.


# Calculate the average for even and odd numbers
def calculate_averages(arr):
    sum_even = 0
    count_even = 0
    sum_odd = 0
    count_odd = 0

    for num in arr:
        if num % 2 == 0:  # Check if the number is even
            sum_even += num
            count_even += 1
        else:
            sum_odd += num
            count_odd += 1

    average_even = sum_even / count_even if count_even > 0 else 0  # Divide the sum of even numbers by the count of even numbers
    average_odd = sum_odd / count_odd if count_odd > 0 else 0  # Divide the sum of odd numbers by the count of odd numbers

    return average_even, average_odd


# Main function
def main():
    random_numbers = generate_random_numbers()
    print(f"Generated random numbers: {random_numbers}")

    bubble_sort(random_numbers)  # "pass by reference": when you pass a list to a function, you're actually passing a reference to the original list, not a copy of it. This means that any changes made to the list inside the function will affect the original list outside the function as well.
    print(f"Sorted random numbers: {random_numbers}")

    average_even, average_odd = calculate_averages(random_numbers)
    print(f"Average for even numbers: {average_even}")
    print(f"Average for odd numbers: {average_odd}")


if __name__ == "__main__":
    main()
