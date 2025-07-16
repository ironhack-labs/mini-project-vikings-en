from vikingsClasses import War, Viking, Saxon
import random

def createTeams():
    """Create and return two lists, one of Vikings and one of Saxons."""
    viking_names = ["Olaf", "Ivar", "Erik", "Leif"]
    saxon_health = 100
    saxon_strength = 50

    vikings = [Viking(name, health=100, strength=50) for name in viking_names]
    saxons = [Saxon(saxon_health, saxon_strength) for _ in range(4)]  # Create a team of 4 Saxons

    return vikings, saxons

def setupWar(vikings, saxons):
    """Initialize the War class and add the Vikings and Saxons."""
    battle = War()
    for viking in vikings:
        battle.addViking(viking)
    for saxon in saxons:
        battle.addSaxon(saxon)
    return battle

def runGame(war):
    """Simulate the war until one army is completely defeated."""
    while len(war.vikingArmy) > 0 and len(war.saxonArmy) > 0:
        if random.choice([True, False]):
            print(war.vikingAttack())
        else:
            print(war.saxonAttack())

        # Print the current status
        print(war.showStatus())

    # Final Status
    print(war.showStatus())

if __name__ == '__main__':
    vikings, saxons = createTeams()
    war = setupWar(vikings, saxons)
    runGame(war)
