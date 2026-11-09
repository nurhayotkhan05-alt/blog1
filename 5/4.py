names = ['ali', 'vali', 'sardor'] 

while True:
    ism = input("Ism kiriting: ").lower()

    if ism in names:
        print("Topildi!")
    else:
        print("Topilmadi")