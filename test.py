data = None

while data != None:
    try:
        exel = input("Nombre del archivo de exel")
        data = pd.read_excel(exel)
        break
    except:
        print("error")
