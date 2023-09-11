def sum_list(numbers):
    return sum(numbers)

def product_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Example usage:
ex_numbers = [1, 2, 3, 4, 5]
result = sum_list(ex_numbers)
print("Sum of the numbers:", result)

result_product = product_list(ex_numbers)
print("Product of the numbers:", result_product)