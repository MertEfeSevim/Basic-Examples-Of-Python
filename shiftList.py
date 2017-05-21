def shiftList(values):
    temp = values[0]
    for i in range(len(values)-1):
        values[i] = values[i+1]
    values[len(values)-1] = temp
    return values


if __name__ == '__main__':
    L = [1,2,3,4,5]
    print(L)
    print(shiftList(L))