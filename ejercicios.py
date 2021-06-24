def run():
    numero = int(input("Elige un numero del 1 al 10: "))
    if numero <= 10:
        if numero < 5:
            print("es menor a 5")
        if numero > 5:
            print("es mayor a 5")
        if numero == 5:
            print("es igual a 5")
    else:
        print("elige otro numero")

if __name__ == "__main__":
    run()