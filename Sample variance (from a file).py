# your_username is what your computers name is
# If your having trouble finding the name of your file, right click on the file and go to properties the location will be listed
file_path = 'C:/Users/your_username/Desktop/sample_variance_example.txt'

def sample_variance(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / (n - 1)
    return variance

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        data = list(map(float, content.split(",")))
    return data

data = read_file(file_path)

squared_variance = sample_variance(data)

print((f"The sample variance is {squared_variance}"))