
"""
    Get value of a list of dictionary matching key.
"""
employees = [
    {'name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'name': 'John Hopkins', 'age': 19, 'salary': 2000},
    {'name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]
# Return only one:
employee_by_name = next((
    employee for employee in employees if employee["name"] == "John Hopkins"), None)

print(employee_by_name, end='\n\n')

# ---------------------------------------

# Return all matching values:
employee_by_name = filter(lambda e: (e["name"] == "John Hopkins"), employees)
print(list(employee_by_name))
