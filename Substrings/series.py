def slices(series, length):
    if len(series) == 0:
        raise ValueError('series cannot be empty')
    elif length < 0:
        raise ValueError('slice length cannot be negative')
    elif length == 0:
        raise ValueError('slice length cannot be zero')
    elif len(series) > 0:
        if len(series) >= length:
            a = []
            [a.append(series[i:length + i]) for i in range(len(series) - length + 1)]
            return a
        else:
            raise ValueError('slice length cannot be greater than series length')