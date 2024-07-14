import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Đọc dữ liệu từ file CSV
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
data = pd.read_csv('iris.csv')

# Thực hiện trực quan dữ liệu từ 3 đến 5 chiều
# Ví dụ: Giả sử bạn muốn tạo đồ thị 3 chiều từ 3 cột đầu tiên của dữ liệu
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
x = data.iloc[:, 0]
y = data.iloc[:, 1]
z = data.iloc[:, 2]
ax.scatter(x, y, z)

# Đặt tên cho các trục và đồ thị
ax.set_xlabel('Trục X')
ax.set_ylabel('Trục Y')
ax.set_zlabel('Trục Z')
ax.set_title('Đồ thị 3 chiều')

# Thêm chiều mới vào đồ thị
# Ví dụ: Giả sử bạn muốn thêm cột thứ tư vào đồ thị
w = data.iloc[:, 3]

# Tạo đồ thị 4 chiều bằng seaborn
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(x, y, z, c=w, cmap='viridis')
plt.colorbar(scatter, label='Trục W')

# Đặt tên cho các trục và đồ thị
ax.set_xlabel('Trục X')
ax.set_ylabel('Trục Y')
ax.set_zlabel('Trục Z')
ax.set_title('Đồ thị 4 chiều')

plt.show()

