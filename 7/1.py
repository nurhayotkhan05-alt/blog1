def max_son(a,b,c):
    max = a
    if max < b:
        max = b
    elif max < c:
        max=c

    return max

print(max_son(10,25,7))