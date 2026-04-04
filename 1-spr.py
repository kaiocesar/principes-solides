
"""
Les principes Solid
SPR - Single Responsability Principle
"""


""" 1. la classe sans principles solid """
# class Livre:
#     def __init__(self, nom):
#         self.nom = nom
#
#     def enregistrer(self):
#         print(f"Enregistrement du livre {self.nom} dans la base de données")
#
#     def afficher(self):
#         print(f"Affichage du livre {self.nom}")


""" 2. la classe avec principles solid """
class Livre:
    def __init__(self, nom):
        self.nom = nom


class LivreEnregistreur:
    def enregistrer(self, livre):
        print(f"Enregistrement du livre {livre.nom} dans la base de données")


class LivreAfficheur:
    def afficher(self, livre):
        print(f"Affichage du livre {livre.nom}")
