import math

players = [234, 382, 266]

# вычисление кол-ва матчей
matches = int(math.factorial(len(players)) / 2 / (math.factorial(len(players) - 2)))

possib = 4 ** matches

alls = []
pts = []
k = 0
for i in range(4):
    for j in range(4):
        for z in range(4):
            nowpts = [i + j, 3 - i + z, 3 - j + 3 - z]
            if nowpts[0] > nowpts[1] and nowpts[0] > nowpts[2]:
                k+=players[0]
            elif (nowpts[0] == nowpts[1] and nowpts[1] > nowpts[2]) or (nowpts[0] == nowpts[2] and nowpts[2] > nowpts[1]):
                k+=players[0]/2
            elif nowpts[0] == nowpts[1] and nowpts[1] == nowpts[2]:
                k+=players[0]/3
            alls.append([[i, 3 - i],[j, 3 - j],[z, 3 - z]])
            pts.append(nowpts)

print(alls, len(alls))
print(pts, len(pts), k, k/(possib*sum(players)/3))
