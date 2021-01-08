usr = {
        'saldo': 0,
        'contactos': []
        }

y = 0

while y == 0:
    w = input('qué desea hacer? 1) ver su saldo 2) ver sus contactos 3) agregar saldo 4) agregar contacto 5) buscar un contacto 6) salir ') 
    if w == "1":
        print(usr["saldo"])

    if w == "2":
        print(usr["contactos"])

    if w == "3":
        x = input('cuánto quiere agregar? ')
        z = usr["saldo"] + int(x)
        print(z)
        usr.update({"saldo": z})

    if w == "4":
        r = input('ingrese el nombre de la persona que quiere agendar: ')
        t = usr["contactos"]
        t.append(r)
        print(t)

    if w == "5":
        a = input('a quién quiere buscar? ')
        if a in usr["contactos"]:
            print(a, 'existe entre sus contactos')
        else:
            print(a, 'no se encuentra entre sus contactos')

    if w == "6":
        print("Bye!")
        y = 1

