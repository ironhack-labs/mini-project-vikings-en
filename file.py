import random
from vikingsClasses import Viking, Saxon, War

def create_war():
    war = War()

    # List of Viking names
    viking_names = ["Adam", "Lucy", "Ail", "Max", "Sarah", "Mona", "John", "Mary", "Daniel", "James"]

    # Create 5 Vikings with fixed health of 100
    for _ in range(5):
        name = random.choice(viking_names)  # Select a random name
        health = 100  # Fixed health
        strength = random.randint(30, 50)  # Strength between 30 and 50
        war.addViking(Viking(name, health, strength))

    # Create 5 Saxons with fixed health of 100
    for _ in range(5):
        health = 100  # Fixed health
        strength = random.randint(20, 40)  # Strength between 20 and 40
        war.addSaxon(Saxon(health, strength))

    return war

# Ask the user to enter the number of rounds
max_rounds = int(input("Enter the number of rounds: "))

# Create the war instance
war = create_war()

# Start the battle
round_num = 1
while war.vikingArmy and war.saxonArmy and round_num <= max_rounds:
    print(f"\n⚔️ Round {round_num} ⚔️")
    
    # Randomly choose which army will attack
    if random.choice([True, False]):
        print("🔥 Vikings Attack!")
        print(war.vikingAttack())  # Vikings attack
    else:
        print("⚔️ Saxons Attack!")
        print(war.saxonAttack())  # Saxons attack
    
    # Print the status of both armies after each round
    print(f"🏹 Vikings left: {len(war.vikingArmy)} | 🛡️ Saxons left: {len(war.saxonArmy)}")
    
    round_num += 1  # Increase the round number

# Display the final result
print("\n🏆 Game Over 🏆")
print(war.showStatus())
