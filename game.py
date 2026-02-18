import vikingsClasses as game

def game_loop():
    pass


if __name__ == '__main__':
    user_input = ""
    war = game.War()

    print("How many vikings are in the army?")
    vikings_count = int(input())
    for i in range(vikings_count):
        name = input("Input name: ")
        health = int(input("Input health: "))
        strength = int(input("Input strength: "))
        war.addViking(game.Viking(name, health, strength))

    print("How many saxons are in the army?")
    saxons_count = int(input())
    for i in range(saxons_count):
        health = int(input("Input health: "))
        strength = int(input("Input strength: "))
        war.addSaxon(game.Saxon(health, strength))
    
    round = 0
    while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        try:
            war.vikingAttack()
        except Exception as e: 
            print(e)
        try:
            war.saxonAttack()
        except Exception as e: 
            print(e)
        print(f"round: {round} // Viking army: {len(war.vikingArmy)} warriors",f"and Saxon army: {len(war.saxonArmy)} warriors")
        print(war.showStatus())
        round += 1