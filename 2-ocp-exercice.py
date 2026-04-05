"""
Les principles Solid
OCP - Open/closed principle
"""

class CalculateurDeRecompense:
    """
    Calcule la récompense d'un client selon son type d'abonnement
    Ce code viole le principle Open/Closed. À vous de corriger!
    """

    def calculer_points(self, type_abonnement: str, montant_achat: float) -> float:
        # Logique de récompense selon le type d'abonnement
        if type_abonnement == "basique":
            return montant_achat * 0.05
        elif type_abonnement == "premium":
            return (montant_achat * 0.10) + 20
        elif type_abonnement == "vip":
            return montant_achat * 0.20
        else:
            raise ValueError(f"Type d'abonnement inconnu : {type_abonnement}")


if __name__ == "__main__":
    calculateur = CalculateurDeRecompense()

    commandes = [
        ("basique", 100.00),
        ("premium", 200.00),
        ("vip", 300.00)
    ]

    for type_abo, montant_achat in commandes:
        points = calculateur.calculer_points(type_abo, montant_achat)
        print(f"[{type_abo}] Achat R${montant_achat:.2f} -> {points:2f} points")