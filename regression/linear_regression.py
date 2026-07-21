
# Linear Regression
# Numerical Methods
# Author: Claudio Yévenes Rojas

import matplotlib.pyplot as plt

# Sample data
x = [10,20,30,40]
y = [22, 19, 33, 41]

print("Values of x:", x)
print("Values of y:", y)

# Means Values
x_mean = sum(x) / len(x)
y_mean = sum(y) / len(y)

print("Mean of x:", x_mean)
print("Mean of y:", y_mean)

# Slope calculation

numerator = 0
denominator = 0

for i in range(len(x)):
    numerator += (x[i]- x_mean)* (y[i]- y_mean)
    denominator += (x[i]- x_mean) ** 2


print("Numerator:", numerator)
print("Denominator:", denominator)

# Slope (m)

m = numerator / denominator

print("Slope (m):", m)

# Intercept (b)

b = y_mean - (m * x_mean)

print("Intercept (b):", b)

print(f"Regression equation:")
print(f"y = {m:.2f}x + {b:.2f}")

print("Predictions:")

for i in range(len(x)):
    prediction = m * x[i] + b
    print(f"x = {x[i]:>3} -> predicted y = {prediction:.2f} | actual y = {y[i]}")


print("Residuals:")

for i in range(len(x)):
    prediction = m * x[i] + b
    residual = y[i] - prediction
    print(
    f"x = {x[i]:>3} | "
    f"Actual = {y[i]:>5.2f} | "
    f"Predicted = {prediction:>5.2f} | "
    f"Residual = {residual:>6.2f}"
    )


# Mean Squared Error (MSE)

mse = 0

for i in range(len(x)):

    prediction = m * x[i] + b

    mse += (y[i] - prediction) ** 2

mse = mse / len(x)

print(f"\nMean Squared Error (MSE): {mse:.4f}")


# Total Sum of Squares (SST)

sst = 0

for value in y:

    sst += (value - y_mean) ** 2

print(f"Total Sum of Squares (SST): {sst:.4f}")


# Sum of Squared Residuals (SSR)

ssr = 0

for i in range(len(x)):

    prediction = m * x[i] + b

    ssr += (y[i] - prediction) ** 2

print(f"Sum of Squared Residuals (SSR): {ssr:.4f}")


# Coefficient of Determination

r2 = 1 - (ssr / sst)

print(f"R²: {r2:.4f}")


def plot_regression(x, y, m, b):
    # Scatter plot (original data)
    plt.scatter(x, y, label="Original Data")

    # Regression line
    y_line = []

    for value in x:
        y_line.append(m * value + b)

    plt.plot(x, y_line, label="Regression Line")

    plt.title("Linear Regression")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.grid(True)
    plt.legend()

    plt.show()


plot_regression(x, y, m, b)


plt.figure(figsize=(8, 5))

plt.scatter(
    x,
    y,
    color="royalblue",
    s=70,
    label="Original Data"
)

plt.plot(
    x,
    y_line,
    color="crimson",
    linewidth=2.5,
    label="Regression Line"
)

plt.title("Linear Regression from Scratch")
plt.xlabel("X")
plt.ylabel("Y")

plt.grid(alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()