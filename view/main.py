import controller.fieldController

# initialization
fieldController = controller.fieldController
b = False

while not b:
    print("1. Tampilkan lapangan yang tersedia")
    print("2. Pilih lapangan")
    print("3. Buat lapangan")
    print("4. Delete lapangan")
    m = int(input("Pilih menu : "))
    if m == 1:
        print(fieldController.get_all())
    elif m == 2:
        print(fieldController.get_all().split())
        line = int(input("pilih lapangan"))
        print(fieldController.get_line(line))
    elif m == 3:
        args = input("buat nama lapangan: ")
        fieldController.write_line(args)
    elif m == 4:
        print(fieldController.get_all().split())
        line = int(input("pilih lapangan"))
        print(fieldController.delete_line(line))

    v = input("Apakah anda ingin mengulang lagi? y/n ")

    if v == "n":
        b = True
    elif v == "y":
        b = False
    else:
        print("invalid answer, rebooting...")
