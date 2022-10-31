class Conjuntos:

    @staticmethod
    def Union(*conjuntos: set) -> set:
        conjunto = set.union(*conjuntos)
        return conjunto

    @staticmethod
    def Intersecion(*conjuntos: set) -> set:
        conjunto = set.intersection(*conjuntos)
        return conjunto

    @staticmethod
    def Suma(*conjuntos: set) -> set:
        conjunto = set.symmetric_difference(*conjuntos)
        return conjunto

    @staticmethod
    def Diferencia(*conjuntos: set) -> set:
        conjunto = set.difference(*conjuntos)
        return conjunto
