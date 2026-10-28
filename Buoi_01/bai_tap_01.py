import numpy as np
import matplotlib.pyplot as plt

x = np.array([8, 12])
y = np.array([700, 1100])
y_pred = np.array([720, 1080])

# Tính MSE
mse = np.mean((y - y_pred) ** 2)
print("MSE =", mse)

# Vẽ điểm thực tế
plt.scatter(
    x, y,
    color="blue",
    label="Actual"
)

# Vẽ điểm dự đoán
plt.scatter(
    x, y_pred,
    color="red",
    label="Predicted"
)

# Nối các điểm dự đoán
plt.plot(
    x, y_pred,
    color="green",
    linestyle="-",
    label="Prediction Line"
)

plt.xlabel("Operating Hours")
plt.ylabel("USD")
plt.title(f"Dự đoán MSE = {mse:.2f}")
plt.legend()
plt.show()