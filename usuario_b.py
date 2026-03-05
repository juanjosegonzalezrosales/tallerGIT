# funcion numeros primos

def primos_en_rango():
    inicio = int(input("Ingrese el número inicial: "))
    fin = int(input("Ingrese el número final: "))

    print("Primos encontrados:")

    for num in range(inicio, fin + 1):

        if num > 1:

            es_primo = True

            for i in range(2, num):
                if num % i == 0:
                    es_primo = False
                    break

            if es_primo:
                print(num)
                
# funcion verificar numero primo

# funcion verificar numero primo
def es_primo(numero):

    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True

# funcion factorial
def factorial(n):
    pass