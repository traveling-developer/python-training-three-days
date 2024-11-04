# 1. Calculate annual premiums from monthly premium
premiums = [100, 200, 300, 400]

annual_premiums_for_loop = []
for premium in premiums:
    annual_premiums_for_loop.append(premium * 12)

annual_premiums_list_comp = [premium * 12 for premium in premiums]  # answer here
# Output: annual_premiums = [1200, 2400, 3600, 4800]
print("Annual Premiums (for loop):", annual_premiums_for_loop)
print("Annual Premiums (list comprehension):", annual_premiums_list_comp)


# 2. Filter high premiums using a threshold
premiums = [100, 200, 300, 400]
threshold = 250

high_premiums_for_loop = []
for premium in premiums:
    if premium > threshold:
        high_premiums_for_loop.append(premium)

high_premiums_list_comp = [premium for premium in premiums if premium > threshold]  # answer here
# Output: high_premiums = [300, 400]
print("High Premiums (for loop):", high_premiums_for_loop)
print("High Premiums (list comprehension):", high_premiums_list_comp)


# 3. Square each number in the list
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]  # answer here
# Output: [1, 4, 9, 16, 25]
print("Squared numbers", squared_numbers)


# 4. Filter Numbers Divisible by 3 or 5
numbers = [15, 30, 45, 22, 33, 60, 73, 90]
divisible_by_3_and_5 = [x for x in numbers if x % 3 == 0 or x % 5 == 0]  # answer here
# Output: [15, 30, 45, 33, 60, 90]
print("Divisible by 3 or 5", squared_numbers)


# 5. Generate a List of Tuples
numbers = [1, 2, 3, 4, 5]
doubles = [(x, x * 2) for x in numbers]  # answer here
# Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
print("Doubles", doubles)
