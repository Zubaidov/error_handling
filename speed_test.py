import timeit

code_to_measure1 = """
numbers = list(range(1, 100000))
increment = 20

for i in range(len(numbers)):
    numbers[i] += increment
"""

code_to_measure2 = """
numbers = list(range(1, 100000))
increment = 20

new_list = list(map(lambda a: a+increment, numbers))
"""

execution_time1 = timeit.timeit(
    stmt=code_to_measure2,  # The code to measure
    number=1000,           # Number of times to repeat
    globals=globals()      # Pass the global namespace
)

execution_time2 = timeit.timeit(
    stmt=code_to_measure2,  # The code to measure
    number=1000,           # Number of times to repeat
    globals=globals()      # Pass the global namespace
)

print(f"Execution Time: {execution_time1} seconds")
print(f"Execution Time: {execution_time2} seconds")