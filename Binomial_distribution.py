import numpy as np
import matplotlib.pyplot as plt

# Set the parameters for the binomial distribution
n = 100  # Number of trials
p = 0.5  # Probability of success

# Generate random numbers following a binomial distribution
random_binomial = np.random.binomial(n, p, 50000)  # 1000 samples
print(random_binomial)
# Plot the histogram of the random binomial distribution
plt.hist(random_binomial, bins=np.arange(0, n+2) - 0.5, density=True, alpha=0.75, color='skyblue', edgecolor='black')

# Add labels and title to the plot
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.title(f'Random Binomial Distribution (n={n}, p={p})')

# Show the plot
plt.show()




