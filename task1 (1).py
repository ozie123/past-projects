#Task1 Description: Number statistics  by osman tourey 29007048


# Function to prompt the user to input numbers. Checks should be perform so that the numbers are positive ints
def get_positive_numbers():
    
     
   
    positive_ints = []
    print("Please enter a positive integer. Type 'done' when completed")
    while True:
        user_input = input("> ")
        if user_input == 'done' or user_input == 'Done' or user_input == 'DONE': #checks if the user is done
            break
        if not user_input.isdigit():
            print("invalid input.please enter a valid integer.") #Check if the input is a digit
        elif int(user_input) <= 0: #checks if the input is a positive integer
            print("invalid input. Please enter a positive integer")
        else:
            positive_ints.append(int(user_input)) #Add the valid input to the list
    return positive_ints 

# Function to remove duplicates from the list, prints the duplicted numbers and returns a list with no duplicates
def remove_duplicates(numbers):
    # Create a list of unique numbers
    unique_numbers = []
    duplicates = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num) #adds the unique numbers to the list
        else:
            duplicates.append(num) #adds the duplicates to the list
    if duplicates:
        print(f"Duplicates removed: {list(set
            (duplicates))}")#prints the duplicates removed from the list
    return unique_numbers

# Function to count the number of unique numbers
def count_unique_numbers(numbers): # counts the number of unique numbers
    ammount_unique_nums = 0 #initializes the count of unique numbers
    for _ in numbers:
        ammount_unique_nums += 1 
    return ammount_unique_nums #returns the count of unique numbers

# Function to calculate the product of numbers
def calculate_product(numbers):
    #calculates the product of the numbers
    nums_product = 0 #initializes the product of the numbers
    if numbers:
        nums_product = 1
        for num in numbers:
            nums_product += num #calculates the product of the numbers
    return nums_product

# Function to calculate the range of numbers
def calculate_range(numbers):
    # Calculates the range (difference between largest and smallest) of the numbers.
    nums_range = 0
    if numbers:
        largest = numbers[0]
        smallest = numbers[0]
        for num in numbers:
            if num > largest:
                largest = num
            if num < smallest: #calculates the range of the numbers
                smallest = num
        nums_range = largest - smallest
    return nums_range

# Function to calculate the variance of numbers
def calculate_variance(numbers):
    nums_var = 0
    if numbers:
        total = 0
        for num in numbers:
            total += num
        mean = total / len(numbers)#calculates the mean of the numbers
        sum_diff_sq = 0
        for num in numbers:
            diff = num - mean
            sum_diff_sq += diff * diff 
        nums_var = sum_diff_sq / len(numbers)#calculates the variance of the numbers
    return nums_var

# Function to separate even and odd numbers
def separate_even_odd(numbers):
    even_numbers = []
    odd_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num) #separates the even numbers from the list
        else:
            odd_numbers.append(num) #separates the odd numbers from the list
    return even_numbers, odd_numbers

# Function to display the results
def display_results(unique_numbers, removed_duplicates, even_numbers, odd_numbers, count, product, range_val, variance):
    print("\n", "Results:")
    print(f"Unique numbers: {unique_numbers}")
    print(f"Count of unique numbers:{count}")
    print(f"Product of unique numbers:{product}")
    print(f"Range of unique numbers: {range_val}")
    print(f"Variance of unique numbers: {variance}")
    if even_numbers:
        print(f"Even numbers:{even_numbers}") 
    else:
        print("No even numbers were provided.")
    if odd_numbers:
        print(f"Odd number: {odd_numbers}")
    else:
        print("No odd numbers were provided")

# Main function to control the flow of the program
def main():
    numbers= get_positive_numbers()
    if not numbers:
        print("No positive numbers entered. Exiting program.")
        return

    unique_numbers =  remove_duplicates(numbers)
    count = count_unique_numbers(unique_numbers)
    product = calculate_product (unique_numbers)
    range_val = calculate_range (unique_numbers)
    variance = calculate_variance (unique_numbers)
    even_numbers, odd_numbers = separate_even_odd(unique_numbers)

    display_results(unique_numbers, numbers, even_numbers, odd_numbers, count, product, range_val, variance)

if __name__ == "__main__":
    main()