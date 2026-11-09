def kopaytir(list):
    k = 1
    for i in list:
        k *= i
    return k


print(kopaytir([1,2,3,4,5]))