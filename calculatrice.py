class Calculatrice:
    def addition(self, a, b):
        return a + b

    def soustraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Division par zéro impossible")

    def puissance(self, a, b):
        return a ** b

    def racine_carree(self, a):
        if a >= 0:
            return a ** 0.5
        else:
            raise ValueError("Racine carrée d'un nombre négatif impossible")
