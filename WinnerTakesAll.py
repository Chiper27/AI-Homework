import numpy as np
x = np.array([
    [45, 85], [50, 43], [40, 80], [55, 42], [200, 43], [48, 40], [195, 41], [43, 87], [190, 40]])
w = np.array([
    [np.random.randint(0, 100), np.random.randint(0, 100)],
    [np.random.randint(0, 100), np.random.randint(0, 100)],
    [np.random.randint(0, 100), np.random.randint(0, 100)]])
c = 0.01
epoci = 5
prototipuri = []
print("w=", w, "\n")
for e in range(epoci):
    for i in range(np.size(x, 0)):
        for j in range(np.size(w, 0)):
            prot = abs(x[i][0]-w[j][0])+abs(x[i][1]-w[j][1])
            prototipuri.append(prot)
        pozitia_minima = np.argmin(prototipuri)
        w[pozitia_minima] = w[pozitia_minima]+c*(x[i]-w[pozitia_minima])

        prototipuri.clear()
print("w nou=", w,  "\n")


for i in range(np.size(x, 0)):
    for j in range(np.size(w, 0)):
        prot = abs(x[i][0]-w[j][0])+abs(x[i][1]-w[j][1])
        prototipuri.append(prot)
    pozitia_minima=np.argmin(prototipuri)
    prototipuri.clear()
    print(x[i], "Ii este asociat lui", w[pozitia_minima], "\n")
