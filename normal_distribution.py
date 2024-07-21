import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def draw_curve(x_values, y_values):
    x = np.array([float(i) for i in x_values.split()])
    y = np.array([float(i) for i in y_values.split()])

    if len(x) != len(y):
        print("Error: x and y must have the same length.")
        return

    mu, std = norm.fit(y)

    xmin, xmax = min(x), max(x)
    x_fit = np.linspace(xmin, xmax, 100)
    y_fit = norm.pdf(x_fit, mu, std)

    plt.scatter(x, y, label="Data", color="blue")
    plt.plot(x_fit, y_fit, label=f"Normal fit: $\mu={mu:.2f}$, $\sigma={std:.2f}$", color="red")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Normal Distribution Fit")
    plt.legend()
    
    plt.show()

if __name__ == "__main__":
    x_values = input("Enter the x values separated by spaces: ")
    y_values = input("Enter the y values separated by spaces: ")
    draw_curve(x_values, y_values)
