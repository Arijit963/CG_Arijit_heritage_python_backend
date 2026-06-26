import sys
from array import array
numbers = list(range(1000))
arr = array('i', range(1000))
print("List Memory :", sys.getsizeof(numbers))
print("Array Memory:", sys.getsizeof(arr))
