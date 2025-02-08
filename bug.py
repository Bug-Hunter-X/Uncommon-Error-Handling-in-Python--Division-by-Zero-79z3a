def function_with_uncommon_error(a, b):
    if a == 0:
        return 0  # Correct handling of division by zero
    elif b == 0:
        return float('inf')  # Represents infinity
    else:
        return a / b

result = function_with_uncommon_error(10, 0)
print(result)  # Output: inf
result = function_with_uncommon_error(0, 10)
print(result) # Output: 0
result = function_with_uncommon_error(10,2)
print(result) #Output: 5.0