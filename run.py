import os

# Access Jenkins parameters using environment variables
param1 = os.environ.get('NUM_THREADS')
param2 = os.environ.get('BOOL_PARAM_1')
param3 = os.environ.get('BOOL_PARAM_2')
param4 = os.environ.get('FRUIT')

# Now you can use these parameters in your script
print("Parameter 1:", param1, type(param1))
print("Parameter 2:", param2, type(param2))
print("Parameter 3:", param3, type(param3))
print("Parameter 4:", param4, type(param4))

print(os.environ)