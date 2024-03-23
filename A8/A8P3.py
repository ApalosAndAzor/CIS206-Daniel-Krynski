# Create a tuple and a list
test_tuple = (1, 2, 3, 4, 5)
test_list = [1, 2, 3, 4, 5]

# Test which is faster
import time

start_time = time.time()
for x in range(1000000):
    if 5 in test_tuple:
        pass
end_time = time.time()
tuple_time = end_time - start_time

start_time = time.time()
for x in range(1000000):
    if 5 in test_list:
        pass
end_time = time.time()
list_time = end_time - start_time

print(f"Tuple took {tuple_time} seconds to execute.")
print(f"List took {list_time} seconds to execute.")

# Test which uses less memory
import sys

tuple_size = sys.getsizeof(test_tuple)
list_size = sys.getsizeof(test_list)

print(f"Size of tuple: {tuple_size} bytes")
print(f"Size of list: {list_size} bytes")