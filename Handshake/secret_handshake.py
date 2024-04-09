def commands(binary_str):
    sp = ["wink", "double blink", "close your eyes", "jump"]
    rdy = []
    result = []
    if '1' not in binary_str:
        return rdy
    else:
        count = 0
        binary_str = reversed(binary_str)
        sp.append('jump')
        for i in binary_str:
            count += 1
            if i == '1' and count < 5:
                rdy.append(sp[0])
            if i == '1' and count == 5:
                rdy = reversed(rdy)
            del sp[0]
    for i in rdy:
        if i not in result:
            result.append(i)

    return result