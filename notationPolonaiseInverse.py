class NotationPolonaiseInverse:
    def addition(self, a, b):
        return a + b

    def soustraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

    def calcul(self, a, b, operateur):
        if operateur == "+":
            return self.addition(a, b)
        elif operateur == "-":
            return self.soustraction(a, b)
        else:
            return self.multiplication(a, b)
