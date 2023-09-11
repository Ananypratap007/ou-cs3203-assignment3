def sum_list(numbers):
    return sum(numbers)

def product_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

def reverse_list(numbers):
    return numbers[::-1]

def main():
    # Get user input for a list of numbers
    input_numbers = input("Enter numbers separated by spaces: ")
    numbers = [float(x) for x in input_numbers.split()]

    # Calculate and print the sum
    result_sum = sum_list(numbers)
    print("Sum of the numbers:", result_sum)

    # Calculate and print the product
    result_product = product_list(numbers)
    print("Product of the numbers:", result_product)
    
     # Reverse the list and print
    reversed_numbers = reverse_list(numbers)
    print("Reversed list of numbers:", reversed_numbers)

if __name__ == "__main__":
    main()
    