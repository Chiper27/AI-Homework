import math

import numpy as np

klust = 3
P = np.array(
    [[45, 8], [50, 43], [40, 80], [55, 42], [200, 43], [48, 40], [195, 41], [43, 87], [190, 40]])
dist = []
Klustere = []

lungime = len(P)
ind_cent = np.random.choice(lungime, size=klust, replace=False)
centroizi = P[ind_cent, :]

print("Centroizi intiali sunt :", "\n", centroizi)


def DistantaPct(m, n):
    return abs(m[0] - n[0]) + abs(m[1] - n[1])


while 1:
    for i in range(lungime):
        for j in range(klust):
            dist.append(DistantaPct(P[i], centroizi[j]))
        poz_min = np.argmin(dist)
        dist.clear()
        Klustere.append(poz_min)

    Newcentroizi = []

    for i in range(klust):
        x = 0
        y = 0
        nr = 0
        print("Puncte asociate centroidului", i+1, "(", centroizi[i], ")", ":")
        for j in range(lungime):
            if Klustere[j] == i:
                print(P[j])
                x = x + P[j][0]
                y = y + P[j][1]
                nr = nr + 1
        punct = [round(x / nr, 2), round(y / nr, 2)]
        Newcentroizi.append(punct)

    if np.array_equal(centroizi, Newcentroizi): break
    print("Centroizi noi formati:", "\n", Newcentroizi, "\n")
    centroizi = Newcentroizi
    Klustere.clear()
