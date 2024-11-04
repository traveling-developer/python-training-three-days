### Exercise: Error Handling in Python with Custom Exceptions

## Background

In this exercise, you will learn to effectively handle errors in Python, including creating and raising custom exceptions. Custom exceptions allow you to define application-specific error handling, making your code more readable and manageable. You’ll learn to use `try`, `except`, `else`, and `finally` blocks, along with custom exceptions, to manage and control the flow of errors.

## Instructions for Creating `divide_numbers()` Function and `InvalidInputError` Class

This guide will help you implement a Python function that handles division with error checking, including custom exception handling.

#### Step 1: Create a Custom Exception Class

1. Define a custom exception class, `InvalidInputError`, which will inherit from `TypeError`.
2. This custom exception will be used to handle cases where non-numeric values are passed to the function.

#### Step 2: Define the `divide_numbers` Function

1. Create a function `divide_numbers` that takes two parameters: `numerator` and `denominator`.
2. Within the function, use a `try` block to perform the following:

    - **Type Check**: Check if both `numerator` and `denominator` are either integers or floats.
        - If either parameter is non-numeric, raise `InvalidInputError` with the message `"Numerator and denominator must be numbers."`
    - **Division Operation**: Attempt to divide `numerator` by `denominator`.
        - If the division is successful, store the result in a variable `result`.
        - If a `ZeroDivisionError` occurs (e.g., `denominator` is zero), print `"Error: Cannot divide by zero."` and return `None`.

3. Add an `else` block that will only execute if no exceptions are raised, printing `"Division successful."` and returning `result`.

4. Add a `finally` block that always executes, printing `"Execution completed."`

### Step 3: Define Test Cases

Write a few example test cases to validate the functionality of the `divide_numbers` function:

- **Case 1**: A division with valid numbers, where both the numerator and denominator are integers. This should return the correct result without errors.
- **Case 2**: A division where the denominator is zero, which should trigger a `ZeroDivisionError` and return `None`.
- **Case 3**: A division where the numerator is non-numeric (e.g., a string), which should raise the custom `InvalidInputError`.
- **Case 4**: A division where the denominator is non-numeric (e.g., a string), which should raise the custom `InvalidInputError`.
- **Case 5**: A division where both the numerator and denominator are non-numeric (e.g., strings), which should raise the custom `InvalidInputError`.
