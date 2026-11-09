def on_besh(list):
    list1 = []
    for i in list:
        if i % 15 == 0:
            list1.append(i)
    return list1


print(on_besh([1,2,30,45,32,115]))