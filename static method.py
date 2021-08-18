class Math:
    def add_5(x):
        return x + 5

    def add_10(y):
        return y + 10


print("Memory management")

x = 10
print(id(x))
y = 12
print(id(y))

string = "cool"
print(id(string))

import sys
print(sys.getsizeof(x))

print(sys.getsizeof(string))

list_e = [1,2,3,4]
print(sys.getsizeof(list_e))
