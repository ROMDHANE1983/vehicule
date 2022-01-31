"""
Module test_type_vehicule

Ce module est dédié au test unitaire de la classe Container.
"""
import unittest
# Modification du lien relatif (remonter dans le dossier parent)
import sys

sys.path.append("..")

from src.type_vehicule import TypeVehicule
from src.camion import Camion
from src.moto import Moto
from src.voiture import Voiture


class TestTypeVehicule(unittest.TestCase):
    """
    Classe de test dédiée à la classe
    """

    def setUp(self):
        self.tv = TypeVehicule(3, "Forcycle")

    def test_type_vehicule_is_instance(self):
        self.assertIsInstance(self.tv, TypeVehicule)

    def test_type_vehicule_attributes(self):
        self.assertEqual(self.tv.nb_roues, 4)
        self.assertEqual(self.tv.nom, "Forcycle")


class TestCamion(unittest.TestCase):
    """
    Classe de test dédiée à  la classe
    """

    def setUp(self):
        self.tv = Camion()

    def test_type_vehicule_is_instance(self):
        self.assertIsInstance(self.tv, Camion)

    def test_type_vehicule_attributes(self):
        self.assertEqual(self.tv.nb_roues, 6)
        self.assertEqual(self.tv.nom, "Camion")


class TestVoiture(unittest.TestCase):
    """
    Classe de test dédiée à  la classe
    """

    def setUp(self):
        self.tv = Voiture()

    def test_type_vehicule_is_instance(self):
        self.assertIsInstance(self.tv, Voiture)

    def test_type_vehicule_attributes(self):
        self.assertEqual(self.tv.nb_roues, 4)
        self.assertEqual(self.tv.nom, "Voiture")



class TestMoto(unittest.TestCase):
    """
    Classe de test dédiée à  la classe
    """

    def setUp(self):
        self.tv = Moto()

    def test_type_vehicule_is_instance(self):
        self.assertIsInstance(self.tv, Moto)

    def test_type_vehicule_attributes(self):
        self.assertEqual(self.tv.nb_roues, 2)
        self.assertEqual(self.tv.nom, "Moto")


if __name__ == "__main__":
    """
    Procédure main pour lancer les tests sur la classe Container.
    """
    unittest.main()
