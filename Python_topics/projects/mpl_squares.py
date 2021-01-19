import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares)

ax.plot(squares, linewidth=3)
# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
ax.scatter(x_values, y_values, c='red', s=10)
ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)


ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
plt.show()