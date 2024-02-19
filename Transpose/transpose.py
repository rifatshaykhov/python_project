def transpose(lines):
    if len(lines) <= 0:
        return lines
    else:
        lines_a = list(lines.replace('\n', ''))
        lines_b = lines.split('\n')
        a = []

        if len(lines_b) == 1:
            [a.append(i) for i in lines]
            return '\n'.join(a)

        elif len(lines_b) == len(lines_a):
            [a.append(i) for i in lines_b]
            return ''.join(a)

        elif len(lines_b) > 1:
            sp = []
            for i in lines_b:
                sp.append(len(i))
            b = []
            d = []
            if len(lines_a) % len(lines_b) != 0:
                if len(lines_b) == 6:
                    for i in lines_b:
                        if len(i) < len(lines_b):
                            i += ' ' * (len(lines_b) - len(i))
                            d.append(i)
                            lines_a.append((' ' * (len(lines_b) - len(i))))
                        else:
                            d.append(i)

                    for j in range(len(lines_b)):
                        for k in range(len(d)):
                            a.append(d[k][j])

                    for i in range(0, len(a), len(lines_b)):
                        c = ''.join(a[i:i + len(lines_b)])
                        b.append(c)

                elif len(lines_b) == 2:
                    for i in lines_b:
                        if len(i) < round(len(lines_a) / len(lines_b)):
                            i += ' '
                            d.append(i)
                            lines_a.append(' ')
                        else:
                            d.append(i)

                    for j in range(round((len(lines_a) / len(lines_b)))):
                        for k in range(len(d)):
                            a.append(d[k][j])

                    for i in range(0, len(a), len(lines_b)):
                        c = ''.join(a[i:i + len(lines_b)])
                        b.append(c)
                else:
                    i = 0
                    c = 0
                    z = 0
                    minn = min(sp)
                    while c != len(lines_b):
                        if minn < sp[-1]:
                            index = sp.index(min(sp))
                            lines_b[index] += (' ' * (sp[-1] - minn))
                            minn = sp[-1]
                        while minn-i != 0:
                            j = 0
                            while j != len(sp):
                                a.append(lines_b[j][i])
                                j += 1
                            for w in range(1):
                                g = ''.join(a[z:z + len(sp)])
                                b.append(g)
                                z += len(sp)
                            i += 1
                        sp.remove(min(sp))
                        c += 1

            elif len(lines_a) % len(lines_b) == 0:
                for i in range(len(lines_a)//len(lines_b)):
                    for j in range(len(lines_b)):
                        a.append(lines_b[j][i])

                for i in range(0, len(a), len(lines_b)):
                    c = ''.join(a[i:i+len(lines_b)])
                    b.append(c)

            return '\n'.join(b).strip()
