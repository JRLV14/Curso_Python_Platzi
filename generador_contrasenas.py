import random
from string import punctuation, ascii_uppercase, ascii_lowercase, digits

def generar_contrasena():
    caracteres = ascii_uppercase + ascii_lowercase + digits + punctuation

    contrasena = []

    for i in range(18):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    print("Contraseña generada " + contrasena)



if __name__ == "__main__":
    run()
    
