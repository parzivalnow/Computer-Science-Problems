def largestUniqueNumber(A):
    freq = list(filter(lambda x: x[1] == 1, {key: A.count(key) for key in set(A)}.items()))
    if len(freq) > 0:
        freq.sort()
        return freq[-1][0]
    return -1
