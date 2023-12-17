import numpy as np
import matplotlib.pyplot as plt

# Set the parameters for the poisson distribution
mu= 200 #Avarage
samples=100000
#The distribution
random_poisson = np.random.poisson(mu,samples)  # 1000 samples
print(random_poisson)
# Plot the histogram of the random poisson distribution
plt.hist(random_poisson, bins=np.arange(0, mu*2) , density=True, color='skyblue', edgecolor='black')

# Add labels and title to the plot
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.title(f'Random Poisson Distribution (mu={mu}, samples={samples})')

# Show the plot
plt.show()
