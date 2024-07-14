import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x * x + 10 * np.sin(x)


def gradient(x):
    return 2 * x + 10 * np.cos(x)


def momentum_GD(x, momentum=0.9, leaning_rate=0.1):
    velocity = np.zeros_like(x)
    print("Momentum GD:")
    lst = [x[0][0]]
    iter = 0
    for i in range(100):
        x_old = x
        iter += 1
        #print(x)

        # print(gradient(x))
        velocity = momentum * velocity + leaning_rate * gradient(x)
        #print(f'gradient:{gradient(x)}')
        #print(f'velocity:{velocity}')


        x = x_old - velocity
        lst = np.row_stack((lst, x))

        if np.linalg.norm(gradient(x)) / np.array(x).size < 1e-3:
            break
    print(lst)
    print("iteration:{}".format(iter))
    return x
def NAG(x,momentum=0.9,learning_rate=0.1):
    velocity=np.zeros_like(x)
    print("NAG:")
    lst = [x[0][0]]

    iter=0
    for i in range(100):
        velocity=momentum*velocity+learning_rate*gradient(x-momentum*velocity)
        x=x-momentum*velocity
        lst = np.row_stack((lst, x))

        iter+=1
        if np.linalg.norm(gradient(x)) / np.array(x).size < 1e-3:
            break
    print(lst)
    print("iteration:{}".format(iter))
    return x

def GD(x, learning_rate=0.1):
    print("GD:")
    lst = [x[0][0]]
    iter=0
    for i in range(100):
        x_old = x
        iter+=1
        x = x_old - learning_rate * gradient(x)
        # print(x)
        lst = np.row_stack((lst, x))

        if np.linalg.norm(gradient(x)) / np.array(x).size < 1e-3:
            break
    #print(lst)
    print(f"iteration:{iter}")
    return x


xx = np.linspace(-5, 5, 1000).reshape(-1, 1)
y = f(xx)
plt.plot(xx, y, lw=2)
x = np.array([[5.5]])
print(x.shape)
x = momentum_GD(x)
plt.plot(x, f(x), 'ro', markersize=8)
plt.title("Momentum gradient descent")
plt.show()
x = np.array([[5.5]])

x = GD(x)
xx = np.linspace(-5, 5, 1000).reshape(-1, 1)
y = f(xx)
plt.plot(xx, y, lw=2)
plt.title("Gradient descent")
plt.plot(x, f(x), 'bo', markersize=8)

plt.show()
x = np.array([[5.5]])

x = NAG(x)
xx = np.linspace(-5, 5, 1000).reshape(-1, 1)
y = f(xx)
plt.plot(xx, y, lw=2)
plt.title("Nesterov Accelerated Gradient descent")
plt.plot(x, f(x), 'go', markersize=8)

plt.show()
