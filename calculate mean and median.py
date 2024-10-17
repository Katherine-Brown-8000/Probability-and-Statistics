data = [1, 2, 3, 4]

mean = sum(data)/ len(data)

data.sort()

n = len(data)
if n % 2 == 1:
    median = data[n//2]
else:
    median = (data[(n // 2) - 1] + data[n // 2]) / 2

print(f"The mean is {mean}")
print(f"The median is {median}")
