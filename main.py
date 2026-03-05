# main.py

from usuario_b import primos_en_rango , es_primo#,factorial, mcd
from usuario_a import fibonacci, es_capicua, es_numero_perfecto


def mostrar_menu():
    print("\n===== TALLER GIT & PYTHON =====")
    print("1. Serie Fibonacci")
    print("2. Número capicúa")
    print("3. Número perfecto")
    print("4. Números primos en un rango")
    print("5. Verificar si un número es primo")
    print("6. Factorial")
    print("7. Máximo Común Divisor (MCD)")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("⚠️ Debe ingresar un número válido.")
            continue

        if opcion == 1:
            n = int(input("Ingrese la cantidad de términos: "))
            print("Resultado:", fibonacci(n))

        elif opcion == 2:
            numero = int(input("Ingrese un número: "))
            if es_capicua(numero):
                print("El número es capicúa.")
            else:
               print("El número NO es capicúa.")

        elif opcion == 3:
           numero = int(input("Ingrese un número: "))
           if es_numero_perfecto(numero):
               print("El número es perfecto.")
           else:
               print("El número NO es perfecto.")

        elif opcion == 4:
            primos_en_rango()

        elif opcion == 5:
            numero = int(input("Ingrese un número: "))
            if es_primo(numero):
                print("El número es primo.")
            else:
                print("El número NO es primo.")

        elif opcion == 6:
           n = int(input("Ingrese un número: "))
           print("Factorial:", factorial(n))

        elif opcion == 7:
           a = int(input("Ingrese el primer número: "))
           b = int(input("Ingrese el segundo número: "))
           print("MCD:", mcd(a, b))

        elif opcion == 0:
            print("Saliendo del programa...")
            break

        else:
            print("⚠️ Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
