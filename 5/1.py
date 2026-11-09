list = []

while True:
    command = input("Komandani kiriting: ")

    if command == "stop":
        print("Dastur to'xtatildi!")
        break
    elif command == "list":
        print("list = ",list)
    elif len(command.split(" ")) == 2:
        com,number = command.split(" ")
        if com == "add":
            list.append(number)