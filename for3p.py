import math

players = [382, 266, 233, 234, 154, 250]

# вычисление кол-ва матчей
matches = int(math.factorial(len(players)) / 2 / (math.factorial(len(players) - 2)))

possib = 4 ** matches

def for3():
    alls = []
    pts = []
    k1 = 0
    k2 = 0
    k3 = 0
    #u1 vs u2, u1 vs u3, u2 vs u3
    for i in range(4):
        for j in range(4):
            for z in range(4):
                nowpts = [i + j, 3 - i + z, 3 - j + 3 - z]
                if max(nowpts) == nowpts[0]:
                    k1 += players[0] / nowpts.count(nowpts[0])
                if max(nowpts) == nowpts[1]:
                    k2 += players[1] / nowpts.count(nowpts[1])
                if max(nowpts) == nowpts[2]:
                    k3 += players[2] / nowpts.count(nowpts[2])
                alls.append([[i, 3 - i],[j, 3 - j],[z, 3 - z]])
                pts.append(nowpts)

    print(alls, len(alls))
    print(pts, len(pts), k, k/(possib*sum(players)/3))

def for4():
    alls = []
    pts = []
    k1 = 0
    k2 = 0
    k3 = 0
    k4 = 0
    # u1 vs u2, u3 vs u4, u1 vs u3, u2 vs u4, u1 vs u4, u2 vs u3.
    for i in range(4):
        for j in range(4):
            for z in range(4):
                for x in range(4):
                    for y in range(4):
                        for w in range(4):
                            nowpts = [i + z + y, 
                                      3 - i + x + w, 
                                      j + 3 - z + 3 - w,
                                      3 - j + 3 - x + 3 - y]
                            if max(nowpts) == nowpts[0]:
                                k1 += players[0] / nowpts.count(nowpts[0])
                            if max(nowpts) == nowpts[1]:
                                k2 += players[1] / nowpts.count(nowpts[1])
                            if max(nowpts) == nowpts[2]:
                                k3 += players[2] / nowpts.count(nowpts[2])
                            if max(nowpts) == nowpts[3]:
                                k4 += players[3] / nowpts.count(nowpts[3])

                            alls.append([[i, 3 - i], [j, 3 - j], [z, 3 - z], [x, 3 - x], [y, 3 - y], [w, 3 - w]])
                            pts.append(nowpts)
                    
    print(alls, len(alls))
    print(pts, len(pts), k, k/(possib*sum(players)/4))

def for5():
    alls = 0
    pts = []
    k1 = 0
    k2 = 0
    k3 = 0
    k4 = 0
    k5 = 0
    # u2 vs u3, u4 vs u1, u3 vs u4, u1 vs u5, u4 vs u2, u5 vs u3, u3 vs u1, u2 vs u5, u5 vs u4, u1 vs u2
    for m1 in range(4):
        for m2 in range(4):
            for m3 in range(4):
                for m4 in range(4):
                    for m5 in range(4):
                        for m6 in range(4):
                            for m7 in range(4):
                                for m8 in range(4):
                                    for m9 in range(4):
                                        for m10 in range(4):
                                            nowpts = [3 - m2 + m4 + 3 - m7 + m10,
                                                      m1 + 3 - m5 + m8 + 3 - m10,
                                                      3 - m1 + m3 + 3 - m6 + m7,
                                                      m2 + 3 - m3 + m5 + 3 - m9,
                                                      3 - m4 + m6 + 3 - m8 + m9]

                                            if max(nowpts) == nowpts[0]:
                                                k1 += players[0] / nowpts.count(nowpts[0])
                                            if max(nowpts) == nowpts[1]:
                                                k2 += players[1] / nowpts.count(nowpts[1])
                                            if max(nowpts) == nowpts[2]:
                                                k3 += players[2] / nowpts.count(nowpts[2])
                                            if max(nowpts) == nowpts[3]:
                                                k4 += players[3] / nowpts.count(nowpts[3])
                                            if max(nowpts) == nowpts[4]:
                                                k5 += players[4] / nowpts.count(nowpts[4])

                                            alls += 1             
    print(alls)
    print(k1/(possib*sum(players)/5), k2/(possib*sum(players)/5), k3/(possib*sum(players)/5), k4/(possib*sum(players)/5), k5/(possib*sum(players)/5), (k1+k2+k3+k4+k5)/(possib*sum(players)/5))

def for6():
    alls = 0
    pts = []
    k1 = 0
    k2 = 0
    k3 = 0
    k4 = 0
    k5 = 0
    k6 = 0
    #1 6 - 1
    #2 5 - 2
    #3 4 - 3
    #4 1 - 5
    #5 6 - 3
    #6 2 - 4
    #7 5 - 6
    #8 4 - 1
    #9 3 - 2
    #10 1 - 2
    #11 6 - 4
    #12 3 - 5
    #13 4 - 5
    #14 2 - 6
    #15 3 - 1
    for m1 in range(4):
        print("m1 " + str(m1))
        for m2 in range(4):
            for m3 in range(4):
                for m4 in range(4):
                    for m5 in range(4):
                        for m6 in range(4):
                            for m7 in range(4):
                                for m8 in range(4):
                                    for m9 in range(4):
                                        for m10 in range(4):
                                            for m11 in range(4):
                                                for m12 in range(4):
                                                    for m13 in range(4):
                                                        for m14 in range(4):
                                                            for m15 in range(4):
                                                                nowpts = [3 - m1 + m4 + 3 - m8 + m10 + 3 - m15,
                                                                          3 - m2 + m6 + 3 - m9 + 3 - m10 + m15,
                                                                          3 - m3 + 3 - m5 + m9 + m12 + m15,
                                                                          m3 + 3 - m6 + m8 + 3 - m11 + m13,
                                                                          m2 + 3 - m4 + m7 + 3 - m12 + 3 - m13,
                                                                          m1 + m5 + 3 - m7 + m11 + 3 - m14]

                                                                if max(nowpts) == nowpts[0]:
                                                                    k1 += players[0] / nowpts.count(nowpts[0])
                                                                if max(nowpts) == nowpts[1]:
                                                                    k2 += players[1] / nowpts.count(nowpts[1])
                                                                if max(nowpts) == nowpts[2]:
                                                                    k3 += players[2] / nowpts.count(nowpts[2])
                                                                if max(nowpts) == nowpts[3]:
                                                                    k4 += players[3] / nowpts.count(nowpts[3])
                                                                if max(nowpts) == nowpts[4]:
                                                                    k5 += players[4] / nowpts.count(nowpts[4])
                                                                if max(nowpts) == nowpts[5]:
                                                                    k5 += players[5] / nowpts.count(nowpts[5])

                                                                alls += 1         
    print(alls)
    print(k1/(possib*sum(players)/6), k2/(possib*sum(players)/6), k3/(possib*sum(players)/6), k4/(possib*sum(players)/6), k5/(possib*sum(players)/6), k6/(possib*sum(players)/6), (k1+k2+k3+k4+k5+k6)/(possib*sum(players)/6))

if len(players) == 3:
    for3()
elif len(players) == 4:
    for4()
elif len(players) == 5:
    for5()
elif len(players) == 6:
    for6()
