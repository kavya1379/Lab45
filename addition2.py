import sys

def add(a, b):
    return a + b

if _name_ == "_main_":
    x = int(sys.argv[1])   # Convert first argument to integer
    y = int(sys.argv[2])   # Convert second argument to integer
    print("sum:",add(x, y))
