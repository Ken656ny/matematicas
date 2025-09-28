from fractions import Fraction

def menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Resolver operaciones con enteros")
    print("2. Resolver comparaciones (> , < , =)")
    print("3. Ordenar lista de números")
    print("4. Resolver fracciones (usando Fraction)")
    print("5. Salir")

def resolver_enteros():
    print("\n Escribe la operación (ejemplo: -34 + (-12), 21 - 6*5 - (-3))")
    expresion = input("Operación: ")
    try:
        resultado = eval(expresion)
        print(f"Resultado: {resultado}")
    except Exception as e:
        print("Error:", e)

def comparaciones():
    print("\n Digita dos números para comparar:")
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    if a > b:
        simbolo = ">"
    elif a < b:
        simbolo = "<"
    else:
        simbolo = "="
    print(f"{a} {simbolo} {b}")

def ordenar_lista():
    print("\n Digita una lista de números separados por coma (ejemplo: -4, 12, -5, 0, 3)")
    entrada = input("Lista: ")
    try:
        numeros = [float(x.strip()) for x in entrada.split(",")]
        print("Ordenados de menor a mayor:", sorted(numeros))
    except:
        print("Error: asegúrate de digitar bien la lista.")

def fracciones():
    print("\n Digita una operación con fracciones (ejemplo: Fraction(1,2) + Fraction(3,4))")
    print(" Usa la forma Fraction(numerador, denominador)")
    expresion = input("Operación: ")
    try:
        resultado = eval(expresion)
        print(f"Resultado: {resultado}  (decimal: {float(resultado)})")
    except Exception as e:
        print("Error:", e)
        
if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            resolver_enteros()
        elif opcion == "2":
            comparaciones()
        elif opcion == "3":
            ordenar_lista()
        elif opcion == "4":
            fracciones()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print(" Opción inválida. Intenta de nuevo.")
