def encode(message, rails):
    sp = []
    k = 1
    c = rails - 2
    for i in range(rails):
        if i == 0 or i == (rails - 1):
            [sp.append(message[j]) for j in range(i, len(message), (rails - 1) * 2)]
        else:
            count = 0
            st, st_1 = i, i
            while count != (len(message) // (rails - 1)):
                if count % 2 == 0:
                    for j in range(st, len(message), (rails - 1 - k) * 2):
                        sp.append(message[j])
                        count += 1
                        st += ((rails - 1 - k) * 2) + ((rails - 1 - c) * 2)
                        break
                elif count % 2 != 0:
                    for j in range(st_1 + ((rails - 1 - k) * 2), len(message), (rails - 1 - c) * 2):
                        sp.append(message[j])
                        st_1 += ((rails - 1 - k) * 2) + ((rails - 1 - c) * 2)
                        count += 1
                        break
            k += 1
            c -= 1

    return ''.join(sp)


def decode(encoded_message, rails):
    count = 0
    a = 0
    b = len(encoded_message)
    c = 0
    k = 0
    d = 0
    sp = []
    flag = True
    flag1 = True
    while count != len(encoded_message) // (rails - 1):
        if count % 2 == 0:
            for i in range(rails):
                if i == 0:
                    sp.append(encoded_message[a])
                    a += 1
                elif i == (rails - 1):
                    if count == 0:
                        for j in range(i, len(encoded_message), ((rails - 1) * 2)):
                            b -= 1
                    while b != len(encoded_message):
                        sp.append(encoded_message[b])
                        b += 1
                        break
                else:
                    while flag:
                        for _ in range(c, len(encoded_message), (rails - 1) * 2):
                            c += 1
                        flag = False
                        c += count
                    for j in range(c, len(encoded_message)):
                        sp.append(encoded_message[j])
                        c += (rails - 1)
                        break
            flag = True
            c = 0
            k += 1

        else:
            sp1 = ''
            '''while flag1:
                for _ in range(d, len(encoded_message), (rails - 1)):
                    d += 1
                flag1 = False
            d -= count
            for i in reversed(range(rails)):
                if i != 0 and i != (rails - 1):
                    for j in range(d, len(encoded_message)):
                        sp.append(encoded_message[::-1][j])
                        d += (rails - 1)
                        break'''
            while flag1:
                for _ in range(d, len(encoded_message), (rails - 1) * 2):
                    d += 1
                flag1 = False
                d += count
            for i in reversed(range(rails)):
                if i != 0 and i != (rails - 1):
                    for j in range(d, len(encoded_message)):
                        sp1 += encoded_message[j]
                        d += (rails-1)
                        break
            sp1 = sp1[::-1]
            sp.append(sp1)
            flag1 = True
            d = 0

        count += 1
    if count % 2 == 0:
        sp.append(encoded_message[-1])
    return ''.join(sp)