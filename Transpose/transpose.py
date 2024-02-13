def transpose(lines):
    if len(lines) <= 0:
        return lines
    else:
        lines_b = lines.split('\n')
        a = []

        if len(lines_b) == 1:
            [a.append(i) for i in lines]
            return '\n'.join(a)

        else:
            for i in lines_b:
                if len(i) == 1:
                    a.append(i)
                else:
                    for j in i:
                        pass
            return ''.join(a)
