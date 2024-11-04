class InvalidInputError(TypeError):
    """Custom exception for invalid input."""
    pass

def divide_numbers(numerator, denominator):
    try:
        if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
            raise InvalidInputError("Numerator and denominator must be numbers.")
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except InvalidInputError as e:
        print(f"Error: {e}")
        return None
    else:
        print("Division successful.")
        return result
    finally:
        print("Execution completed.")
