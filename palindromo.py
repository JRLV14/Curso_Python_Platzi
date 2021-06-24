def palindromo(frase):
    frase = frase.replace(" ", "")
    frase = frase.lower()
    frase_invertida = frase[::-1]
    if frase == frase_invertida:
        return True
    else :
        return False


def run():
    frase = input("Escribe una frase: ")
    es_palindromo = palindromo(frase)
    if es_palindromo == True:
        print("es palindromo")
    else:
        print("no es palindromo")


if __name__ =="__main__":
    run()