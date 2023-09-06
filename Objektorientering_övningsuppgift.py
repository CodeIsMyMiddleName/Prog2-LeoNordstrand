class Elev:
    def __init__(self, namn, ålder, godkänd):
        self.namn = namn
        self.ålder = ålder
        self.godkänd = godkänd
        self.glad = False

        if self.godkänd:
            self.glad = True
    
    def presentera(self):
        return f"Hej! Jag heter {self.namn}."


hej = Elev("Simon", 55, True)
då = Elev("Johan", 77, False)


print(hej.namn)
print(hej.ålder)
print(hej.glad)
print(hej.presentera())
print(då.presentera())
