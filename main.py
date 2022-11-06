from os import system
from conjutos import Conjuntos
import string

def ImprimirConjuntos(conjuntos: list[set]) -> None:

    i = 65

    for conjunto in conjuntos:
        letra = chr(i)
        print(f'{letra} = {conjunto}')
        i += 1

    print('\n')


def TryParseIntOrString(cadena: string) -> int or string or float or None:

    if cadena == "":
        return None

    try:
        if '.' not in cadena:
            return int(cadena)

        else:
            return float(cadena)

    except:
        return cadena


def LeerConjunto(letra: string) -> set:

    conjunto = set()
    n = CantidadElementosConjuntos(letra)
    i = 1

    while i <= n:

        elemento = input(f'\nIngrese el elemento {i} del conjunto {letra} >> ')
        aux = TryParseIntOrString(elemento)

        if aux == None:
            print('No puede ingresar datos en blanco.')

        elif aux in conjunto:
            print('El elemento ya existe en el conjunto.')

        else:
            conjunto.add(aux)
            i += 1

    return conjunto


def CantidadElementosConjuntos(letra: string) -> int:

    while True:

        try:
            n = int(input(f'Ingrese el número de elementos {letra} >> '))

            if n < 0:
                print("La cantidad de elementos del conjunto no puede ser 0")

            elif n > 10:
                print("La cantidad maxima de elementos permitida es 10.")

            else:
                return n

        except:
            print("Solo se adminten valores enteros.")


def CantidadConjuntos() -> int:

    while True:

        try:

            n = int(input("\nIngrese la cantidad de conjuntos >> "))

            if n < 2:
                print("Se requiere al menos 2 conjuntos para operar.")

            elif n > 5:
                print("La cantidad máxima de conjuntos permitida es 5.")

            else:
                return n

        except:

            print("Solo se adminten valores enteros.")


def CrearConjuntos(n: int) -> list[set]:

    lista_conjuntos = list()

    for i in range(0, n):
        letra = chr(i+65)
        conjunto = LeerConjunto(letra)
        lista_conjuntos.append(conjunto)

    return lista_conjuntos


def OperacionUnion(lista_conjuntos: list[set]) -> None:
    conjunto_union = Conjuntos.Union(*lista_conjuntos)
    ImprimirConjuntos(lista_conjuntos)
    print(f'Unión = {conjunto_union}')


def OperacionIntersccion(lista_conjuntos: list[set]) -> None:
    conjunto_interseccion = Conjuntos.Intersecion(*lista_conjuntos)
    ImprimirConjuntos(lista_conjuntos)
    print(f'Interseción = {conjunto_interseccion}')


def OperacionSuma(lista_conjuntos: list[set]) -> None:
    conjunto_suma = Conjuntos.Suma(*lista_conjuntos)
    ImprimirConjuntos(lista_conjuntos)
    print(f'Suma A + B = {conjunto_suma}')


def OperacionDiferencia(lista_conjuntos: list[set]) -> None:
    ImprimirConjuntos(lista_conjuntos)
    conjunto_diferencia_ab = Conjuntos.Diferencia(*lista_conjuntos)
    print(f'Diferencia A - B = {conjunto_diferencia_ab}')


def SelecionarOperacion(opc: int) -> None:

    system('cls')

    match opc:

        case 1:

            n = CantidadConjuntos()
            conjuntos = CrearConjuntos(n)
            OperacionUnion(conjuntos)

        case 2:

            n = CantidadConjuntos()
            conjuntos = CrearConjuntos(n)
            OperacionIntersccion(conjuntos)

        case 3:

            print("  Para esta operación se requiere exactamente 2 conjuntos (Suma)")
            conjuntos = CrearConjuntos(2)
            OperacionSuma(conjuntos)

        case 4:

            print("  Para esta operación se requiere exactamente 2 conjuntos (Diferencia)")
            conjuntos = CrearConjuntos(2)
            OperacionDiferencia(conjuntos)


def LeerOpcion() -> int:

    while True:

        try:

            opc = int(input("\nIngrese su opción >> "))

            if opc >= 0 and opc < 5:
                return opc

            else:
                print("Opción no válida.")

        except:

            print("Solo se adminten valores enteros.")


def PreguntarContinuar() -> bool:

    print("\nDesea realizar otra operacion?")
    print("  1.- Si")
    print("  2.- No")

    while True:

        try:

            opc = int(input("\nIngrese su opcion >> "))

            if opc >= 1 and opc <= 2:
                return opc == 1

            else:
                print("Opción no valida.")

        except:

            print("Solo se adminten valores enteros.")


def Inicio() -> None:

    continuar = True

    while continuar:
        system('cls')
        print("\t**** CALCULADORA DE CONJUNTOS ****\n")
        print("  1.- Unión")
        print("  2.- Interseccion")
        print("  3.- Suma")
        print("  4.- Diferencia")
        print("  0.- Salir")

        opc = LeerOpcion()
        SelecionarOperacion(opc)
        continuar = PreguntarContinuar()

    print("\t\tNos vemos!\n\n")


Inicio()
