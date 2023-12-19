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
        elif operateur == "*":
            return self.multiplication(a, b)
        elif operateur == "/":
            return self.division(a, b)
        else:
            return print("Valeur(s) non valide!")

    def calculatrice(self, npi):
        npiList = npi.split()
        pile = []

        for i in npiList:
            if i.isnumeric():
                pile.append(int(i))
            else:
                nouveauChiffre = self.calcul(pile[-2], pile[-1], i)
                pile.pop(-1)
                pile[-1] = nouveauChiffre
        return pile[0]
