import numpy as np
import matplotlib.pyplot as plt

e0 = 1
theta = 0
resolution = 100  # Resolution for the grid

class Body:
    def __init__(self, q, rho, theta, label):
        """
        Initializes the body (charge) with the given charge, position, and label.
        """
        self.q = q
        self.x = np.array([rho * np.cos(theta), rho * np.sin(theta)])
        self.label = label  # Add label for the charge

    def e_potential(self, p):
        """
        Returns the electric potential at point `p`.
        """
        r_vec = p - self.x
        r_mag = np.sqrt(np.sum(r_vec**2))  # Magnitude of r
        if r_mag == 0:
            return 0  # Avoid division by zero at the charge's position
        V = (1 / (4 * np.pi * e0)) * self.q / r_mag
        return V

# Create the bodies (charges)
radius = 1.5
d_real = 2
d_im = (radius**2) / d_real

q_real = 1
q_tot = -q_real
q_im = -q_real * radius / d_real

# Define the charges with labels
central_image_charge = Body(q_tot - q_im, 0, theta, f"Image Charge 1 Q={q_tot - q_im}[a.u.], d={0}[a.u.]")
side_image_charge = Body(q_im, d_im, theta, f"Image Charge 2 Q={q_im}[a.u.], d={d_im}[a.u.]")
real_charge = Body(q_real, d_real, theta, f"Real Charge Q={q_real}[a.u.], d={d_real}[a.u.]")

bodies = [central_image_charge, side_image_charge, real_charge]

# Generate a grid of points where the electric potential will be calculated
xx, yy = np.linspace(-1.5 * d_real, 1.5 * d_real, resolution), np.linspace(-1.5 * d_real, 1.5 * d_real, resolution)
px, py = np.meshgrid(xx, yy)
points = np.stack((px, py), axis=2)  # Shape (resolution, resolution, 2)

# Initialize the electric potential grid
V_total = np.zeros((resolution, resolution))

# Calculate the total electric potential at each grid point from all charges
for ix in range(points.shape[0]):
    for iy in range(points.shape[1]):
        p = points[ix, iy]  # Current grid point
        for b in bodies:
            V_total[ix, iy] += b.e_potential(p)

# Calculate the logarithm of the potential for better visualization
V_magnitude = np.log10(np.abs(V_total))

# Plot the electric potential as a colormap
plt.figure(figsize=(6,6))

# Plot charge positions and add labels
for b in bodies:
    plt.plot(*b.x, "o", label=b.label)

# Plot the colormap of the electric potential
plt.contourf(px, py, V_magnitude, cmap='inferno', levels=75)

# Plot the circle containing the charges
tt = np.linspace(0, 2 * np.pi, 20)
plt.plot(np.cos(tt) * radius, np.sin(tt) * radius, "xk")

plt.title("Electric Potential and Positions of Charges")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar(label="Logarithms of Electric Potential")
plt.grid(True)
plt.legend()  # Show legend for charge labels
plt.show()
