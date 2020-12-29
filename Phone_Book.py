num_ent = int(input("How many entries? "))
phone_book = {}
for i in range(num_ent):
    a = input("Name Number?").split()
    name, number = a[0], a[1]
    phone_book[name] = number
while True:
    try:
        name = input()
        if name in phone_book:
            print("{}={}".format(name, phone_book[name]))
        else:
            print("Not found")
    except:
        break