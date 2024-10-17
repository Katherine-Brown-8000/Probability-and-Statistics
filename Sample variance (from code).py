data = [3, 7, 13, 18, 21]

def sample_variance(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / (n - 1)

    return variance

squared_variance = sample_variance(data) 

print((f"The sample variance is {squared_variance}"))