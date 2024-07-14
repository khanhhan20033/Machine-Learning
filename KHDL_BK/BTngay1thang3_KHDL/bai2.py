import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import pandas as pd
# Định nghĩa hàm số phức tạp với ít nhất 3 biến và dạng phân số cùng các hàm siêu việt
def f(x, y, z):
    return (np.log(x) * np.exp(y)) / (z**2)

# Vẽ đồ thị hàm số 2D
x = np.linspace(0.1, 5, 100)
y = f(x, 1, 1)  # Giả sử y = 1, z = 1
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Đồ thị hàm số 2D')
plt.show()

# Vẽ đồ thị hàm số 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.linspace(0.1, 5, 100)
x, y = np.meshgrid(x, y)
z = f(x, y, 1)  # Giả sử z = 1
ax.plot_surface(x, y, z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Đồ thị hàm số 3D')
plt.show()

# Vẽ scatter plot
data = np.random.rand(100, 3)  # Tạo dữ liệu ngẫu nhiên với 3 biến
df = pd.DataFrame(data, columns=['x', 'y', 'z'])
sns.set(style="ticks")
sns.pairplot(df)
plt.title('Scatter Plot')
plt.show()
