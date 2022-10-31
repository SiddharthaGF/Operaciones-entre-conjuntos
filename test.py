from ctypes import Union
import unittest

from numpy import conj
from conjutos import Conjuntos


class TestConjuntos(unittest.TestCase):

    def test_union_1(self):
        conjutoA = set({2, 3})
        conjutoB = set({3, 4, (5, 0)})
        self.assertEqual(Conjuntos.Union(
            conjutoA, conjutoB), {2, 3, 4, (5, 0)})

    def test_union_2(self):
        conjutoA = set({1, 'a'})

        conjutoB = set({2, 'b'})
        self.assertEqual(Conjuntos.Union(conjutoA, conjutoB), {'a', 'b', 1, 2})

    def test_union_3(self):
        conjutoA = set({1, 2, 3})
        conjutoB = set({3, 4, 5})
        conjutoC = set({0})
        self.assertEqual(Conjuntos.Union(
            conjutoA, conjutoB, conjutoC), {0, 1, 2, 3, 4, 5})

    def test_union_5(self):
        conjutoA = set({True, 2, 3})
        conjutoB = set({3, 4, False})
        self.assertEqual(Conjuntos.Union(conjutoA, conjutoB),
                         {False, True, 2, 3, 4})

    def test_union_conmutativa(self):
        conjutoA = set({1, 2, 3})
        conjutoB = set({3, 4, 5})
        self.assertEqual(Conjuntos.Union(conjutoA, conjutoB),
                         Conjuntos.Union(conjutoB, conjutoA))

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
        conjutoA = set({True, 2, 3})
        conjutoB = set({3, 4, False})
        self.assertEqual(Conjuntos.Intersecion(conjutoA, conjutoB),
                         {3})

    def test_Intersecion_2(self):
        conjutoA = set({})
        conjutoB = set({0})
        self.assertEqual(Conjuntos.Intersecion(conjutoA, conjutoB),
                         set())

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
        self.assertEqual(Conjuntos.Intersecion(conjutoA, conjutoB),
                         Conjuntos.Intersecion(conjutoB, conjutoA))

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
        self.assertEqual(Conjuntos.Suma(conjutoA, conjutoB), {1, 2, 4, 5})

    def test_diferencia_1(self):
        conjutoA = set({1, 2, 3})
        conjutoB = set({3, 4, 5})
        self.assertNotEqual(Conjuntos.Diferencia(conjutoA, conjutoB),
                            Conjuntos.Diferencia(conjutoB, conjutoA))

    def test_suma_2(self):
        conjutoA = set({1, 2, 3})
        conjutoB = set({3, 4, 5})
        self.assertEqual(Conjuntos.Suma(conjutoA, conjutoB), {1, 2, 4, 5})

    def test_suma_2(self):
        conjutoA = set({1, 2, 3})
        conjutoB = set({3, 4, 5})
        suma = Conjuntos.Suma(conjutoA, conjutoB)
        intersecion = Conjuntos.Intersecion(conjutoA, conjutoB)
        union = Conjuntos.Union(conjutoA, conjutoB)
        diferencia_union_interseccion = Conjuntos.Diferencia(
            union, intersecion)
        self.assertEqual(suma, diferencia_union_interseccion)


if __name__ == '__main__':
    unittest.main()
