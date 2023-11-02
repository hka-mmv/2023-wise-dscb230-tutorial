# Übungsblatt 3 für Python Klassen

"""
Ziel: In diesem Übungsblatt werdet Ihr eine Klasse in Python erstellen und Methoden innerhalb dieser Klasse definieren.
"""

# Übung: Klasse Kreis

# Anweisung:
# 1. Erstellen Sie eine Python-Klasse namens "Kreis", die durch einen Radius konstruiert wird.
# 2. Definieren Sie zwei Methoden innerhalb dieser Klasse:
#    - Eine Methode namens "flaeche", die die Fläche des Kreises berechnet.
#    - Eine Methode namens "umfang", die den Umfang des Kreises berechnet.
# 3. Erstellen Sie ein Objekt dieser Klasse und rufen Sie beide Methoden auf, um die Fläche und den Umfang des Kreises zu berechnen.
# 4. Geben Sie die berechneten Werte aus.


class Kreis:
    def __init__(self, radius):
        self.radius = radius

    def flaeche(self):
        return 3.14 * self.radius**2

    def umfang(self):
        return 2 * 3.14 * self.radius


# Erstellen eines Kreis-Objekts mit einem Radius von 8
meinKreis = Kreis(10)

# Berechnen und Ausgeben der Fläche und des Umfangs des Kreises
print("Fläche des Kreises:", meinKreis.flaeche())
print("Umfang des Kreises:", meinKreis.umfang())
