def baraabar(matn):
    if matn == matn[::-1]:
        return True
    else:
        return False


print(baraabar("kazak"))
print(baraabar("Riteish"))