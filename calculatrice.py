
class Calculatrice:
    def __init__(self):
        pass

    def addition(self, a, b):
        return a + b

    def soustraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            return "Erreur : Division par zéro"
        return a / b
