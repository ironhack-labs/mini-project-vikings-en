import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
       self.health -= damage
       
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
       self.name = name
       super().__init__(health, strength)

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f'{self.name} has died in act of combat'
# Saxon

class Saxon(Soldier):

     def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return 'A Saxon has died in combat'

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        
        result = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
             self.saxonArmy.remove(saxon)
        return result
        
        
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        
        result = viking.receiveDamage(saxon.strength)
            
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result    

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

# BONUS - Automatic Battle
        
import random
import time     # Import time module for adding delays between actions

def generate_viking():      # Function to create random Viking characters
    names = ["Ragnar", "Lagertha", "Bjorn", "Ivar", "Floki", "Harald", "Erik"]
    name = random.choice(names)  # Pick random name from list
    health = random.randint(80, 100)  # Random health between 80-100
    strength = random.randint(40, 70)  # Random strength between 40-70
    return Viking(name, health, strength)  # Create and return Viking object

def generate_saxon():      # Function to create random Saxon characters
    health = random.randint(50, 70)  # Random health between 50-70
    strength = random.randint(30, 50)  # Random strength between 30-50
    return Saxon(health, strength)  # Create and return Saxon object

def start_battle():     # Main function that runs the entire battle game
   
    war = War()     # Create a new War object to manage the battle
    
    viking_count = random.randint(2, 3)     # Random number of Vikings (2 or 3)
    saxon_count = random.randint(2, 4)      # Random number of Saxons (2, 3, or 4)
    
    for _ in range(viking_count):       # Create all Viking warriors
        war.addViking(generate_viking())  # Add random Viking to army
    for _ in range(saxon_count):        # Create all Saxon warriors
        war.addSaxon(generate_saxon())  # Add random Saxon to army
    
    print("BATTLE BEGIN!")
    print("Vikings vs Saxons!")
    print()

    print("VIKING ARMY:")       # Display Viking army stats
    for viking in war.vikingArmy:  # Loop through each Viking
        print(f"  {viking.name} - Health: {viking.health}, Strength: {viking.strength}")  # Show Viking info
    
    print("SAXON ARMY:")      # Display Saxon army stats
    for i, saxon in enumerate(war.saxonArmy, 1):  # Loop through Saxons with numbers
        print(f"  Saxon {i} - Health: {saxon.health}, Strength: {saxon.strength}")  # Show Saxon info
    print()
    
    round_number = 1        # Start counting rounds from 1
    
    # Loop until someone wins
    while war.saxonArmy and war.vikingArmy:  # Continue while both armies have warriors
        print(f"--- Round {round_number} ---")  # Show current round number
        
        # Viking attacks
        if war.vikingArmy and war.saxonArmy:  # Check if both armies still exist
            result = war.vikingAttack()  # Execute Viking attack
            print(f"Viking Attack: {result}")  # Show attack result
            time.sleep(1)  # Pause for 1 second for better readability
        
        # Saxon attacks  
        if war.saxonArmy and war.vikingArmy:  # Check if both armies still exist
            result = war.saxonAttack()  # Execute Saxon attack
            print(f"Saxon Attack: {result}")  # Show attack result
            time.sleep(1)  # Pause for 1 second for better readability
        
        print(f"Status: Vikings [{len(war.vikingArmy)}] vs Saxons [{len(war.saxonArmy)}]")  # Show remaining warriors
        print()
        
        # Wait for user to press Enter before next round
        if war.saxonArmy and war.vikingArmy:  # Only wait if battle continues
            input("Press ENTER for next round...")  # Pause until user presses Enter
            print()
        
        round_number += 1  # Increase round counter for next round
    
    # Final result
    print(war.showStatus())  # Display who won the battle
    print("BATTLE FINISHED!")  # End of game message

# Execute the battle
if __name__ == "__main__":  # Check if this file is being run directly
    start_battle()  # Start the battle game