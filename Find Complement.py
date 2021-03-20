def findComplement(num, base):
    binNum = bin(num)[2:]
    length = len(binNum)
    ans = 0
    for i in range(length-1,-1,-1):
        ans += (1 ^ int(binNum[i])) * 2**(length-i-1)
    if base == "10":
        return ans
    elif base == "8":
        return oct(ans)[2:]
    elif base == "16":
        return hex(ans)[2:]
