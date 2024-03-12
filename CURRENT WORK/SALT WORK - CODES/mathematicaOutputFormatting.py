import re
data = """

"""

print("Volume Fraction")
# Extract m1 values using regex
m1_values = re.findall(r'm1->([\d.]+)', data)
# Print the m1 values
for m1_value in m1_values:
    print(m1_value)
print("Temperature")
# Extract temperture values using regex
values = re.findall(r'\}(\d+)', data)
# Print the values
for value in values:
    print(value)