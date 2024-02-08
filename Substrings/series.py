def slices(series, length):
    if len(series) == 0:
        raise ValueError('series cannot be empty')
    elif length < 0:
        raise ValueError('slice length cannot be negative')
    elif length == 0:
        raise ValueError('slice length cannot be zero')
    elif len(series) > 0:
        s = list(series)
        if len(series) >= length:
            a = []
            if length == 1:
                return s
            elif length == len(s):
                return [series]
            else:
                count = len(s) - length + 1
                while count > 0:
                    for i in range(count):
                        a.append(series[i:length+i])
                        count -= 1
                return a
        else:
            raise ValueError('slice length cannot be greater than series length')
