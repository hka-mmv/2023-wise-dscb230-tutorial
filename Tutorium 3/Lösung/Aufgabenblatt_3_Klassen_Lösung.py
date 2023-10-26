class Rechteck:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rechteck_inhalt(self):
        return self.length * self.width


neuesRechteck = Rechteck(12, 10)
print(neuesRechteck.rechteck_inhalt())
