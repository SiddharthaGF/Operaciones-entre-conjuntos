from asyncio.windows_events import NULL
from os import system
import string
from conjutos import Conjuntos


def ImprimirConjuntos(conjuntos: list[set]) -> None:
    i = 65
    for conjunto in conjuntos:
        print(f'Conjunto {chr(i)} = {conjunto}')
        i += 1
    print('\n')


def IntentarConvertir(cadena: string) -> int or string or NULL:
    try:
        return int(cadena)
    except:
        if len(cadena) == 0:
            return NULL
        return cadena


def ComprovarRepeticion(conjunto: set, elemento) -> bool:
    return elemento in conjunto


def LeerConjunto(letra: string) -> set:
    n = CantidadElementos(letra)
    conjunto = set()
    i = 1
    while len(conjunto) < n:
        aux = input(f'\nIngrese el elemento {i} del conjunto {letra} >> ')
        elemento = IntentarConvertir(aux)
        if not elemento:
            print('No puede ingresar datos en blanco.')
        elif ComprovarRepeticion(conjunto, elemento):
            print('El elemento ya existe en el conjunto.')
        else:
            conjunto.add(elemento)
            i += 1
    return conjunto


def CantidadElementos(letra: string):
    while True:
        try:
            n = int(
                input(f'\nIngrese la cantidad de elementos del conjunto {letra} >> '))
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
                print("Se requieren al menos 2 conjuntos para operar.")
            elif n > 5:
                print("La cantidad maxima de conjuntos permitida es 5.")
            else:
                return n
        except:
            print("Solo se adminten valores enteros.")


def SelecionarOperacion(opc: int) -> None:
    lista_conjuntos = list()
    match opc:
        case 1:
            system('cls')
            n = CantidadConjuntos()
            for i in range(1, n+1):
                conjunto = LeerConjunto(chr(i+64))
                lista_conjuntos.append(conjunto)
            conjunto_union = Conjuntos.Union(*lista_conjuntos)
            system('cls')
            ImprimirConjuntos(lista_conjuntos)
            print(f'Unión = {conjunto_union}')
        case 2:
            system('cls')
            n = CantidadConjuntos()
            for i in range(1, n+1):
                conjunto = LeerConjunto(chr(i+64))
                lista_conjuntos.append(conjunto)
            conjunto_interseccion = Conjuntos.Intersecion(*lista_conjuntos)
            system('cls')
            ImprimirConjuntos(lista_conjuntos)
            print(f'Interseción = {conjunto_interseccion}')
        case 3:
            system('cls')
            print("  Dos conjuntos oblgatorio")
            conjuntoA = LeerConjunto(chr(65))
            conjuntoB = LeerConjunto(chr(66))
            system('cls')
            ImprimirConjuntos(lista_conjuntos)
            conjunto_suma = Conjuntos.Suma(conjuntoA, conjuntoB)
            print(f'Suma A + B = {conjunto_suma}')
        case 4:
            system('cls')
            print("  Dos conjuntos oblgatorio")
            conjuntoA = LeerConjunto(chr(65))
            conjuntoB = LeerConjunto(chr(66))
            system('cls')
            ImprimirConjuntos(lista_conjuntos)
            conjunto_diferencia_ab = Conjuntos.Diferencia(conjuntoA, conjuntoB)
            print(f'Diferencia A - B = {conjunto_diferencia_ab}')
            conjunto_diferencia_bc = Conjuntos.Diferencia(conjuntoB, conjuntoA)
            print(f'Diferencia B - A = {conjunto_diferencia_bc}')
        case _:
            system('cls')
            print("\t\tNos vemos!\n\n")


def LeerOpcion() -> int:
    while True:
        try:
            opc = int(input("\nIngrese su opcion >> "))
            if opc >= 0 and opc < 5:
                return opc
            else:
                print("Opción no valida.")
        except:
            print("Solo se adminten valores enteros.")


def PreguntarContinuar() -> bool:
    print("\nDesea realiar otra operacion?")
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


Inicio()
