"""
2. Open/Closed Principle (OCP)
Le réponse se base sur le fichier 2-ocp-exercice.py
"""
from abc import ABC, abstractmethod

"""
    Attention:
   Nouveaux types à ajouter (sans modifier la classe actuelle). Chacun avec sa propre régle de notation -- à implémenter sans ouvrir CalculateurDeRecompense
   
   Les nouveaux types sont:
   - entreprise
   - etudiant
   - partenaire
"""


class CalculateurDeRecompenseInterface(ABC):
    @abstractmethod
    def calculer_points(self, montant_achat: float) -> float:
        pass


class CalculateurDeRecompenseBasique(CalculateurDeRecompenseInterface):
    def calculer_points(self, montant_achat: float) -> float:
        return montant_achat * 0.05


class CalculateurDeRecompensePremium(CalculateurDeRecompenseInterface):
    def calculer_points(self, montant_achat: float) -> float:
        return (montant_achat * 0.10) + 20


class CalculateurDeRecompenseVip(CalculateurDeRecompenseInterface):
    def calculer_points(self, montant_achat: float) -> float:
        return montant_achat * 0.20


class CalculateurDeRecompenseEntreprise(CalculateurDeRecompenseInterface):
    def calculer_points(self, montant_achat: float) -> float:
        return montant_achat * 0.45


class CalculateurDeRecompenseEtudiant(CalculateurDeRecompenseInterface):
    def calculer_points(self, montant_achat: float) -> float:
        return montant_achat *  0.5


class CalculateurDeRecompensePartenaire(CalculateurDeRecompenseInterface):
    def calculer_points(self, montant_achat: float) -> float:
        return montant_achat * 0.4


if __name__ == "__main__":

    commandes = [
        (CalculateurDeRecompenseBasique, 100.00),
        (CalculateurDeRecompensePremium, 200.00),
        (CalculateurDeRecompenseVip, 300.00),
        (CalculateurDeRecompenseEtudiant, 300.00),
        (CalculateurDeRecompenseEntreprise, 300.00),
        (CalculateurDeRecompensePartenaire, 300.00),
    ]

    for classe, montant_achat in commandes:
        points = classe().calculer_points(montant_achat)
        print(f"Achat R${montant_achat:.2f} -> {points:2f} point")