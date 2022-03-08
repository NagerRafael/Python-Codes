def longest_consec(strarr, k):
    n = len(strarr)
    if (n == 0) | (k > n) | (k <= 0):
        return ""
    else:
        x = 0
        list = []
        ind = []
        while x+k <= n:
            list.append(''.join(strarr[x:x+k]))
            ind.append(len(list[x]))
            x += 1
        return list[ind.index(max(ind))]