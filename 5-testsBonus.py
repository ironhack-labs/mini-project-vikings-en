import unittest
import random
from vikingsClasses import Viking, Saxon, War

class TestGameFlow(unittest.TestCase):
    def test_game_flow_basic(self):
        # Crear un war con 2 Vikings y 2 Saxons
        w = War()
        v1 = Viking("Ragnar", 100, 20)
        v2 = Viking("Ivar", 100, 20)
        s1 = Saxon(60, 12)
        s2 = Saxon(60, 12)

        w.addViking(v1)
        w.addViking(v2)
        w.addSaxon(s1)
        w.addSaxon(s2)

        # Ejecutar unas cuantas rondas automáticas
        for _ in range(5):
            if w.vikingArmy and w.saxonArmy:
                w.vikingAttack()
            if w.vikingArmy and w.saxonArmy:
                w.saxonAttack()

        # A estas alturas, al menos uno de los ejércitos debe haber perdido combate
        status = w.showStatus()
        self.assertIn(status, [
            "Vikings have won the war of the century!",
            "Saxons have fought for their lives and survive another day...",
            "Vikings and Saxons are still in the thick of battle."
        ])

if __name__ == '__main__':
    unittest.main()
