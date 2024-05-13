from random import *
def can_chain(dominoes):
    flag = True
    love = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }
    for i in dominoes:
        for j in i:
            love[j] += 1
    for i in love.values():
        if i % 2 != 0:
            flag = False
            break
        elif len(dominoes) == 0:
            return []
    if flag:
        a = [list(i) for i in dominoes]
        a.sort()
        sp = []
        sp1 = []
        n = 0
        flag1 = True
        while n != len(dominoes):
            for i in a:
                if flag:
                    sp.append(i)
                    a.remove(i)
                    flag = False
                    love[i[0]] -= 1
                    love[i[1]] -= 1
                    break
                elif flag1:
                    if sp[0][0] == i[0] and love[i[0]] == 1:
                        i.reverse()
                        sp1.append(i)
                        a.remove(i)
                        flag1 = False
                        love[i[0]] -= 1
                        love[i[1]] -= 1
                        break
                    elif sp[0][0] == i[1] and love[i[1]] == 1:
                        sp1.append(i)
                        a.remove(i)
                        flag1 = False
                        love[i[0]] -= 1
                        love[i[1]] -= 1
                        break
                    elif sp[0][0] == i[0]:
                        i.reverse()
                        sp1.append(i)
                        a.remove(i)
                        flag1 = False
                        love[i[0]] -= 1
                        love[i[1]] -= 1
                        break
                    elif sp[0][0] == i[1]:
                        sp1.append(i)
                        a.remove(i)
                        flag1 = False
                        love[i[0]] -= 1
                        love[i[1]] -= 1
                        break


                else:
                        if sp[-1][1] == i[1] and love[i[1]] == 1:
                            i.reverse()
                            sp.append(i)
                            a.remove(i)
                            love[i[0]] -= 1
                            love[i[1]] -= 1
                            break
                        elif sp[-1][1] == i[0] and love[i[0]] == 1:
                            sp.append(i)
                            a.remove(i)
                            love[i[0]] -= 1
                            love[i[1]] -= 1
                            break

                        elif sp1[0][0] == i[0] and love[i[0]] == 1:
                            i.reverse()
                            sp1.insert(0, i)
                            a.remove(i)
                            love[i[0]] -= 1
                            love[i[1]] -= 1
                            break

                        elif sp1[0][0] == i[1] and love[i[1]] == 1:
                            sp1.insert(0, i)
                            a.remove(i)
                            love[i[0]] -= 1
                            love[i[1]] -= 1
                            break

                        elif sp[-1][1] == i[0]:
                            sp.append(i)
                            a.remove(i)
                            love[i[0]] -= 1
                            love[i[1]] -= 1
                            break


            n += 1
        sp.extend(sp1)

        if len(dominoes) == len(sp):
            if sp[0][0] == sp[-1][1]:
                return sp


