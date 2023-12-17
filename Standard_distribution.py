import numpy as np
import matplotlib.pyplot as plt

# Set the parameters for the Gaussian distribution
mean = 0    # Mean (center of the distribution)
std_dev =10**100  # Standard deviation (spread of the distribution)

# Generate random numbers following a Gaussian distribution
random_gaussian = np.random.normal(mean, std_dev, 10000000)  # 1000 samples

# Plot the histogram of the random Gaussian distribution
plt.hist(random_gaussian, bins=300, density=True, color='skyblue', edgecolor='black')

# Add labels and title to the plot
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title(f'Random Gaussian Distribution (mean={mean}, std_dev={std_dev})')

# Show the plot
plt.show()