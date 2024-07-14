import numpy as np


def f(x):
    return -(0.2 * np.sin(x) + (np.exp(x) - np.exp(-x)) / 2) ** 2


def grad_f(x):
    return -2 * (0.2 * np.sin(x) + (np.exp(x) - np.exp(-x)) / 2) * (0.2 * np.cos(x) + (np.exp(x) + np.exp(-x)) / 2)


def gradient_descent_with_momentum(f, grad_f, initial_x, learning_rate=0.01, momentum=0.9, max_iterations=10000,
                                   epsilon=1e-8):
    x = initial_x
    velocity = np.zeros_like(x)

    for i in range(max_iterations):
        gradient = grad_f(x)
        velocity = momentum * velocity - learning_rate * gradient
        x = x + velocity

        if np.linalg.norm(gradient) < epsilon:
            break

    return x, f(x)


# Thử nghiệm
initial_x = 0.0  # Giá trị khởi tạo của x
min_x, min_f = gradient_descent_with_momentum(f, grad_f, initial_x)

print("Giá trị nhỏ nhất của hàm f(x):", min_f)
print("Điểm x tương ứng:", min_x)
