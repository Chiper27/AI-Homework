import numpy as np

x = np.array([[2, 1, -1], [0, -1, -1]])
w = np.array([0, 1, 0])
test1 = np.array([-1, -1, 1.5, 0])
test2 = np.array([-1, -2, 0, 0.5])
c = 0.1
FinalArray = np.array([-1,  1])
net_array = [0, 0]
i = 0
j=0
s = np.dot(test1, test2)
print(s)
y = np.sign(s)
print(y)
while 1:
    net = np.dot(w, x[i])
    sign_net = np.sign(net)
    net_array[i] = sign_net
    if net_array[i] == FinalArray[i]:
        pass
    else:
        w = w + c * (FinalArray[i] - net_array[i]) * x[i]
    print("w=", w)
    print("net=", net)
    print("sign_net=", sign_net)
    print("net_array=", net_array)
    print("\n")
    i = i + 1
    j=j+1
    if i == 2: i = 0
    if np.array_equal(FinalArray, net_array): break


print(j)