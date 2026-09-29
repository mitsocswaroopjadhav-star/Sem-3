import pandas as pd
import numpy as np

# Generate 10 random numbers
numbers = np.random.randint(10, 100, 10)

# Create Pandas Series with custom index
data = pd.Series(numbers, index=['a','b','c','d','e','f','g','h','i','j'])

print("Series:")
print(data)

# Indexing
print("\nValue at index 'c':")
print(data['c'])

# Filtering
print("\nNumbers greater than 50:")
print(data[data > 50])

# Statistical operations
print("\nMean =", data.mean())
print("Median =", data.median())
print("Minimum =", data.min())
print("Maximum =", data.max())

'''Series:
a    72
b    35
c    91
d    48
e    63
f    27
g    84
h    56
i    42
j    76
dtype: int64

Value at index 'c':
91

Numbers greater than 50:
a    72
c    91
e    63
g    84
h    56
j    76
dtype: int64

Mean = 59.4
Median = 59.5
Minimum = 27
Maximum = 91'''