import numpy as np

w = np.array([1, -1, 0, 0.5])
w_aux = w
x = np.array([[1, -2, 1.5, 0], [1, -0.5, -2, -1.5], [0, 1, -1, 1.5]])
print("pentru exemplu 4")
for i in range(np.size(x, 0)):
    net = np.dot(x[i], w)
    print(net)
    w = w + np.sign(net) * x[i]
    print("w=", w)

print("  ")


def f(x):
    return 2 / (1 + np.exp(-x)) - 1


for i in range(np.size(x, 0)):
    net = np.dot(x[i], w_aux)
    w_aux = w_aux + f(net) * x[i]
    print("f(net)=", f(net))
    print("w=", w_aux)

print("pentru exemplu 7\n")
w = [1, -1]
w_aux = w
x = np.array([[1, -2], [0, 1], [2, 3], [1, -1], [1, -1]])
for i in range(np.size(x, 0)):
    net = np.dot(x[i], w)
    print(net)
    w = w + np.sign(net) * x[i]
    print("w=", w)


def f(x):
    return 2 / (1 + np.exp(-x)) - 1


for i in range(np.size(x, 0)):
    net = np.dot(x[i], w_aux)
    w_aux = w_aux + f(net) * x[i]
    print("f(net)=", f(net))
    print("w=", w_aux)
