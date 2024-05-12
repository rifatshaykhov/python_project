for i in a:
    if len(sp) == 0:
        sp.append(i)
    elif i[0] == a[0][0]:
        i.reverse()
        sp.append(i)
    else:
        sp.append(i)