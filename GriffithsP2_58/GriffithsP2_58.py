import numpy as np
import matplotlib.pyplot as plt

num_q = 5
e0 = 1
rho = 1
q = 1
resolution = 100  # Resolution for the grid

class Body:
    def __init__(self, q, rho, theta):
        """
        Initializes the body (charge) with the given charge and polar coordinates.
        """
        self.q = q
        self.x = np.array([rho * np.cos(theta), rho * np.sin(theta)])

    def e_field(self, p):
        """
        Returns the electric field vector at point `p`.
        """
        r_vec = p - self.x
        r_mag = np.sum(r_vec**2)**0.5
        E = (1 / (4 * np.pi * e0)) * self.q * r_vec / r_mag**3
        return E

# Create the bodies (charges)
bodies = []
for i in range(num_q):
    theta = 2 * np.pi * i / num_q  # Evenly distribute the charges
    bodies.append(Body(q, rho, theta))

# Generate a grid of points where the electric field will be calculated
xx, yy = np.linspace(-1.5*rho, 1.5*rho, resolution), np.linspace(-1.5*rho, 1.5*rho, resolution)
px, py = np.meshgrid(xx, yy)
points = np.stack((px, py), axis=2)  # Shape (resolution, resolution, 2)

# Initialize the electric field grid
E_total = np.zeros_like(points)

# Calculate the total electric field at each grid point from all charges
for ix in range(points.shape[0]):
    for iy in range(points.shape[1]):
        p = points[ix, iy]  # Current grid point
        for b in bodies:
            E_total[ix, iy] += b.e_field(p)

# Get the components of the electric field
Ex, Ey = E_total[:, :, 0], E_total[:, :, 1]

# Calculate the electric field magnitude for colormap
E_magnitude = np.log10(np.sqrt(Ex**2 + Ey**2))

# Plot the electric field vectors and the colormap
plt.figure(figsize=(6,6))

# Plot charge positions
for b in bodies:
    plt.plot(*b.x, "o")



# Plot the colormap of the electric field magnitude
plt.contourf(px, py, E_magnitude, cmap='inferno', levels=75)

# Plot the circle containing the charges
tt = np.linspace(0, 2 * np.pi, 2000)
plt.plot(np.cos(tt) * rho, np.sin(tt) * rho, "-r")

plt.title("Electric Field and Positions of Charges with Colormap")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar(label="Logarithms of Electric Field Magnitude")
plt.grid(True)
plt.show()
