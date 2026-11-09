umr = int(input("Yoshingizni kiriting: "))
if umr > 0 and umr < 18:
    print("Siz o'qishingiz kerak.")
elif umr > 18 and umr < 60:
    print("Siz ishlashingiz kerak")
elif umr > 60:
    print("Siz nafaqadasiz!")
else:
    print("Bunday yosh mavjud emas!")