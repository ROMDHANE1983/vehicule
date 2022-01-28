"""
Module test_vehicules

Ce module est dédié au test unitaire de la classe Container.
"""
import unittest
# Modification du lien relatif (remonter dans le dossier parent)
import sys

sys.path.append("..")

from src.vehicules import Vehicule
from src.voiture import Voiture


class TestVehicule(unittest.TestCase):
    """
    Classe de test dédiée à la classe Vehicule
    """

    v1_type = Voiture()
    v1_modele = "Cayenne"
    v1_marque = "Porsche"
    v1_type_carburant = "Essence 95 E10"
    v1_couleur = "Jaune"
    v1_cylindree = 300
    v1_age = 3
    v1_kmtrage = 27000
    v1_prix = 400000
    v1_est_neuf = False
    v1_boite_de_vitesse = "5 vitesses"

    def setUp(self):
        """
        Méthode setUp, avec l'instantiation d'un parc de vehicules.
        """
        self.v1 = Vehicule(type=self.v1_type, modele=self.v1_modele,
                           marque=self.v1_marque,
                           type_carburant=self.v1_type_carburant,
                           couleur=self.v1_couleur,
                           cylindree=self.v1_cylindree,
                           age=self.v1_age, kmtrage=self.v1_kmtrage,
                           prix=self.v1_prix, est_neuf=self.v1_est_neuf,
                           boite_de_vitesse=self.v1_boite_de_vitesse)

    def test_type_vehicule(self):
        """
        Méthode pour tester le type de véhicule.
        """
        self.assertIsInstance(self.v1.type, Voiture)

    def test_est_neuf(self):
        """
        Méthode pour tester est_neuf.
        """
        self.assertFalse(self.v1.est_neuf)

    def test_repeindre_vehicule(self):
        """
        Méthode pour tester le changement de peinture pour le véhicule.
        """
        ancienne_couleur = self.v1.couleur
        self.assertEqual(ancienne_couleur, self.v1_couleur)
        nouvelle_couleur = "Rouge"

        self.v1.repeindre_vehicule(nouvelle_couleur)

        self.assertNotEqual(self.v1.couleur, ancienne_couleur)
        self.assertEqual(self.v1.couleur, nouvelle_couleur)

    def test_changer_prix(self):
        """
        """
        self.assertEqual(self.v1.prix, self.v1_prix)
        nouveau_prix = 450000
        self.v1.changer_prix(nouveau_prix)

        self.assertEqual(self.v1.prix, nouveau_prix)

    def test_anniversaire(self):
        """
        """
        age_precedent = self.v1.age
        self.assertEqual(age_precedent, self.v1_age)
        self.v1.anniversaire()
        self.assertEqual(self.v1.age, age_precedent+1)

    def test_ajouter_kilometrage(self):
        """
        """
        kmtrage_precedent = self.v1.kmtrage
        self.assertEqual(kmtrage_precedent, self.v1_kmtrage)
        kms_parcourus = 30
        self.v1.ajouter_kilometrage(kms_parcourus)
        self.assertEqual(self.v1.kmtrage, kmtrage_precedent + kms_parcourus)

    def test_changer_cylindree(self):
        """
        """
        self.assertEqual(self.v1.cylindree, self.v1_cylindree)
        nouvelle_cylindree = 400
        self.v1.changer_cylindree(nouvelle_cylindree)
        self.assertEqual(self.v1.cylindree, nouvelle_cylindree)

    def test_changer_boite_de_vitesse(self):
        """
        """
        self.assertEqual(self.v1.boite_de_vitesse, self.v1_boite_de_vitesse)
        nouvelle_boite = "6 vitesses automatique"
        self.v1.changer_boite_de_vitesse(nouvelle_boite)
        self.assertEqual(self.v1.boite_de_vitesse, nouvelle_boite)


if __name__ == "__main__":
    """
    Procédure main pour lancer les tests sur la classe Container.
    """
    unittest.main()
