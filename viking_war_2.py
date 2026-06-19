from vikingsClasses import Viking, Saxon, War


# Berserker (for polymorphism test)

class Berserker(Viking):
    def attack(self):
        return self.strength * 2
    
    
# Archer (for polymorphism test)

class Archer(Viking):
    def attack(self):
        return self.strength + 10
    

#Great War

# Great War

if __name__ == "__main__":

    ragnar = Berserker("Ragnar", 100, 20)
    bjorn = Archer("Bjorn", 80, 25)

    great_war = War()

    great_war.addViking(ragnar)
    great_war.addViking(bjorn)

    great_war.addSaxon(Saxon(50, 10))
    great_war.addSaxon(Saxon(60, 15))
    great_war.addSaxon(Saxon(40, 8))

    print("Vikings:", len(great_war.vikingArmy))
    print("Saxons:", len(great_war.saxonArmy))

    round_number = 1

    while len(great_war.vikingArmy) > 0 and len(great_war.saxonArmy) > 0:
        print(f"\n--- Round {round_number} ---")

        print(great_war.vikingAttack())

        if len(great_war.saxonArmy) == 0:
            break

        print(great_war.saxonAttack())
        print(great_war.showStatus())

        round_number += 1

    print("\n--- Final Result ---")
    print(great_war.showStatus())