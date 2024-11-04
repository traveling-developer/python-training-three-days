# 1. Calculate annual premiums from monthly premium
premiums = [100, 200, 300, 400]

annual_premiums_for_loop = []
for premium in premiums:
    annual_premiums_for_loop.append(premium * 12)

annual_premiums_lambda = list(map(lambda premium: premium * 12, premiums))  # answer here, hint: use map()
# Output: annual_premiums = [1200, 2400, 3600, 4800]
print("Annual Premiums (for loop):", annual_premiums_for_loop)
print("Annual Premiums (lambda with map):", annual_premiums_lambda)

# 2. Filter high premiums using a threshold
premiums = [100, 200, 300, 400]
threshold = 250

high_premiums_for_loop = []
for premium in premiums:
    if premium > threshold:
        high_premiums_for_loop.append(premium)

high_premiums_lambda = list(filter(lambda premium: premium > threshold, premiums))  # answer here, hint: use filter()
# Output: high_premiums = [300, 400]
print("High Premiums (for loop):", high_premiums_for_loop)
print("High Premiums (lambda with filter):", high_premiums_lambda)


# 3. Square each number in the list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))  # answer here, hint: use map()
# Output: squared_numbers = [1, 4, 9, 16, 25]
print("Squared Numbers (lambda with map):", squared_numbers)


# 4. Sort Premiums by Amount (Descending Order)
premiums = [("CU001", 1000), ("CU002", 4500), ("CU003", 2000), ("CU004", 1500), ("CU005", 3000)]
premiums_sorted_lambda = list(sorted(premiums, key=lambda x: x[1]))  # answer here, hint: use sorted()
# Output: [('CU001', 1000), ('CU004', 1500), ('CU003', 2000), ('CU005', 3000), ('CU002', 4500)]
print("Premiums Sorted by Amount (lambda with sorted):", premiums_sorted_lambda)


# 5. Policies, Sort by coverage value
policies = [
    {"policy_id": "P001", "coverage": 100000},
    {"policy_id": "P002", "coverage": 250000},
    {"policy_id": "P003", "coverage": 50000},
    {"policy_id": "P004", "coverage": 150000}
]
policies_sorted = list(sorted(policies, key=lambda policy: policy["coverage"], reverse=True))  # answer here, hint: use sorted()
# Output: policies sorted by lowest coverage first
# [
# {'policy_id': 'P002', 'coverage': 250000}
# {'policy_id': 'P004', 'coverage': 150000},
# {'policy_id': 'P001', 'coverage': 100000},
# {'policy_id': 'P003', 'coverage': 50000},
# ]
print("Policies Sorted by Coverage (lambda with sorted):", policies_sorted)

