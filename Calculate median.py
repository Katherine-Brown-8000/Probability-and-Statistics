data = [2, 4, 6, 8]

sorted_data = sorted(data)
n = len(sorted_data)
if n % 2 == 1:
    median = sorted_data[n // 2]
else:
    mid1 = sorted_data[n // 2 - 1]
    mid2 = sorted_data[n // 2]
    median = (mid1 + mid2) / 2

print(f"The median is {median}")
