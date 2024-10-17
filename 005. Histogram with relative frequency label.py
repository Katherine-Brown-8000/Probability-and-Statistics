import matplotlib.pyplot as plt
import numpy as np

data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5]

value, counts = np.unique(data, return_counts=True)
relative_freq = counts / len(data)

plt.hist(data, bins=np.arange(min(data) - 0.5, max(data) + 1.5, 1), edgecolor='black', alpha=0.7)
plt.title("Histogram with relative frequency labels")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.xticks(range(min(data), max(data) + 1))
plt.grid(axis="y", linestyle="--", alpha=0.7)

for value, count, rel_freq in zip(value, counts, relative_freq):
    plt.text(value, count, f'freq={count}\nrel.freq={rel_freq:.3f}', ha='center', va='bottom')

plt.show()
