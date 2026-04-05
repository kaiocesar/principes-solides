from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Commande:
    identifiant: str
    montant:     float
    est_urgent:  bool = False


class TraiteurDeCommande(ABC):
    """
    Contrat de base : tout traiteur doit pouvoir
    traiter une commande et annuler une commande.
    """

    @abstractmethod
    def traiter(self, commande: Commande) -> str:
        """Traite la commande. Retourne un message de confirmation."""
        pass

    @abstractmethod
    def annuler(self, commande: Commande) -> str:
        """Annule la commande. Retourne un message de confirmation."""
        pass


class TraiteurStandard(TraiteurDeCommande):
    def traiter(self, commande: Commande) -> str:
        return f"[Standard] Commande {commande.identifiant} traitée."

    def annuler(self, commande: Commande) -> str:
        return f"[Standard] Commande {commande.identifiant} annulée."


class TraiteurUrgent(TraiteurDeCommande):
    def traiter(self, commande: Commande) -> str:
        if not commande.est_urgent: # ceci est spécifique à cette classe.
            raise ValueError("Ce traiteur n'accepte que les commandes urgentes.")
        return f"[Urgent] Commande {commande.identifiant} traitée en priorité."

    def annuler(self, commande: Commande) -> str:
        raise NotImplementedError("Commandes urgentes ne peuvent pas être annulées.")


class TraiteurGratuit(TraiteurDeCommande):
    def traiter(self, commande: Commande) -> str:
        if commande.montant > 0: #
            raise ValueError("Ce traiteur n'accepte que les commandes gratuites.")
        return f"[Gratuit] Commande {commande.identifiant} traitée sans frais."

    def annuler(self, commande: Commande) -> str:
        return f"[Gratuit] Commande {commande.identifiant} annulée."


def pipeline_de_commandes(
    traiteur: TraiteurDeCommande,
    commandes: list[Commande]
) -> None:
    """
    Função cliente: espera que QUALQUER TraiteurDeCommande
    possa tratar e annuler qualquer Commande sem surpresas.
    """
    for commande in commandes:
        print(traiteur.traiter(commande))
        print(traiteur.annuler(commande))


# --- Programme principal ---
if __name__ == "__main__":
    commandes = [
        Commande("C-001", 150.0, est_urgent=False),
        Commande("C-002", 320.0, est_urgent=True),
        Commande("C-003", 0.0,   est_urgent=False),
    ]

    for traiteur in [TraiteurStandard(), TraiteurUrgent(), TraiteurGratuit()]:
        print(f"\n--- {type(traiteur).__name__} ---")
        pipeline_de_commandes(traiteur, commandes)