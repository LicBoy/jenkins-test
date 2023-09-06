import os

# Access Jenkins parameters using environment variables
param1 = os.environ.get('asdsadsa')
param2 = os.environ.get('browsername')
param3 = os.environ.get('long string')

# Now you can use these parameters in your script
print("Parameter 1:", param1)
print("Parameter 2:", param2)
print("Parameter 3:", param3)