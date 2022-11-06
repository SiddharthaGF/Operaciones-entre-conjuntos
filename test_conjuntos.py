from ctypes import Union
import unittest

from numpy import conj
from conjutos import Conjuntos


class TestConjuntos(unittest.TestCase):

    def test_union_1(self):

        conjutoA = set({2, 3})
        conjutoB = set({3, 4, (5, 0)})

        respuesta = Conjuntos.Union(conjutoA, conjutoB)
        esperado = {2, 3, 4, (5, 0)}

        self.assertEqual(respuesta, esperado)

    def test_union_2(self):

        conjutoA = set({1, 'a'})
        conjutoB = set({2, 'b'})

        respuesta = Conjuntos.Union(conjutoA, conjutoB)
        esperado = {'a', 'b', 1, 2}

        self.assertEqual(respuesta, esperado)

    def test_union_3(self):

        conjutoA = set({1, 2, 3})
        conjutoB = set({3, 4, 5})
        conjutoC = set({0})

        respuesta = Conjuntos.Union(conjutoA, conjutoB, conjutoC)
        esperado = {0, 1, 2, 3, 4, 5}

        self.assertEqual(respuesta, esperado)

    def test_union_5(self):

        conjutoA = set({True, 2, 3})
        conjutoB = set({3, 4, False})

        respuesta = Conjuntos.Union(conjutoA, conjutoB)
        esperado = {False, True, 2, 3, 4}

        self.assertEqual(respuesta, esperado)

    def test_union_conmutativa(self):

        conjutoA = set({1, 2, 3})
        conjutoB = set({3, 4, 5})

        respuesta1 = Conjuntos.Union(conjutoA, conjutoB)
        respuesta2 = Conjuntos.Union(conjutoB, conjutoA)
        esperado = {1, 2, 3, 4, 5}

        self.assertEqual(respuesta1, esperado)
        self.assertEqual(respuesta2, esperado)

    def test_union_asociativa(self):

        conjutoA = set({1, 2, 3})
        conjutoB = set({3, 4, 5})
        conjutoC = set({1, 2, 3, 4})

        unionAB = Conjuntos.Union(conjutoA, conjutoB)
        unionABC = Conjuntos.Union(unionAB, conjutoC)

        unionBC = Conjuntos.Union(conjutoB, conjutoC)
        unionBCA = Conjuntos.Union(unionBC, conjutoA)

        self.assertEqual(unionABC, unionBCA)

    def test_Intersecion_1(self):

        conjutoA = set({'a', 'b', 'c'})
        conjutoB = set({1, 2, 3, 4, 5})
        conjutoC = set({'by', 'de', 4})

        respuesta = Conjuntos.Intersecion(conjutoA, conjutoB, conjutoC)
        esperado = set()

        self.assertEqual(respuesta, esperado)

    def test_Intersecion_2(self):

        conjutoA = set({})
        conjutoB = set({0})

        respuesta = Conjuntos.Intersecion(conjutoA, conjutoB)
        esperado = set()

        self.assertEqual(respuesta, esperado)

    def test_Intersecion_3(self):

        conjutoA = set({1, 2, 3})
        conjutoB = set({3, 4, 5})
        conjutoC = set({0, 3})

        intersecionABC = Conjuntos.Intersecion(conjutoA, conjutoB, conjutoC)
        intersecionBCA = Conjuntos.Intersecion(conjutoB, conjutoC, conjutoA)

        self.assertEqual(intersecionABC, intersecionBCA)

    def test_interseccion_conmutativa(self):

        conjutoA = set({1, 2, 3})
        conjutoB = set({3, 4, 5})

        respuesta1 = Conjuntos.Intersecion(conjutoA, conjutoB)
        respuesta2 = Conjuntos.Intersecion(conjutoB, conjutoA)

        self.assertEqual(respuesta1, respuesta2)

    def test_Intersecion_asociativa(self):

        conjutoA = set({1, 2, 3})
        conjutoB = set({3, 4, 5})
        conjutoC = set({1, 2, 3, 4})

        intersecionAB = Conjuntos.Intersecion(conjutoA, conjutoB)
        intersecionABC = Conjuntos.Intersecion(intersecionAB, conjutoC)

        intersecionBC = Conjuntos.Intersecion(conjutoB, conjutoC)
        intersecionBCA = Conjuntos.Intersecion(intersecionBC, conjutoA)

        self.assertEqual(intersecionABC, intersecionBCA)

    def test_suma_1(self):

        conjutoA = set({1, 2, 3})
        conjutoB = set({3, 4, 5})

        respuesta = Conjuntos.Suma(conjutoA, conjutoB)
        esperado = {1, 2, 4, 5}

        self.assertEqual(respuesta, esperado)


    def test_diferencia_1(self):

        conjutoA = set({1, 2, 3})
        conjutoB = set({3, 4, 5})

        respuesta = Conjuntos.Diferencia(conjutoA, conjutoB)
        esperado = {1, 2}
        
        self.assertEqual(respuesta, esperado)

    def test_diferencia_1(self):

        conjutoA = set({1, 2, 3})
        conjutoB = set({3, 4, 5})

        diferenciaAB = Conjuntos.Diferencia(conjutoA, conjutoB)
        diferenciaBA = Conjuntos.Diferencia(conjutoB, conjutoA)

        self.assertNotEqual(diferenciaAB, diferenciaBA)

    def test_suma_2(self):

        conjutoA = set({'a', 'b', 'c'})
        conjutoB = set({'d', 'b'})

        respuesta = Conjuntos.Suma(conjutoA, conjutoB)
        esperado = {'a', 'c', 'd'}

        self.assertEqual(respuesta, esperado)

    def test_suma_3(self):

        conjutoA = set({1, 2, 3})
        conjutoB = set({3, 4, 5})

        suma = Conjuntos.Suma(conjutoA, conjutoB)
        intersecion = Conjuntos.Intersecion(conjutoA, conjutoB)
        union = Conjuntos.Union(conjutoA, conjutoB)

        diferencia = Conjuntos.Diferencia(union, intersecion)

        self.assertEqual(suma, diferencia)


if __name__ == '__main__':
    unittest.main()
