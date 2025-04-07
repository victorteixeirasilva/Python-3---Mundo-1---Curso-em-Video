def leiaDinheiro(msg=""):
    while True:
        i = input(msg).strip().upper()
        i = i.replace(",",".")
        if i != "":
            if not i.isalnum() or not i.isalpha():
                if not i in ".,":
                    i = float(i)
                    return i
                else:
                    i = int(i)
                    return i
