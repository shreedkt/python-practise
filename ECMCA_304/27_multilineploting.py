import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, label='Line 2')

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Multi-Line Plot")
plt.legend()
plt.show()
