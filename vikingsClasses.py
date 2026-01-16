import random

# Soldier

class Soldier:
    """
    Base class that represents a generic soldier in the game.

    Attributes:
        health (int): Current health points of the soldier.
        strength (int): Damage points the soldier deals when attacking.
    """
    def __init__(self, health:int, strength:int):
        # your code here
        
        # Initialize the soldier's health points
        self.health = health

        # Initialize the soldier's attack strength
        self.strength = strength
    
    def attack(self) -> int:
        # your code here
        """
        returns the strength attribute of the soldier (Damage points the soldier deals when attacking).

        Parameters:
            None

        Returns:
            int: Amount of damage dealt by the soldier.
        """
        return self.strength

    def receiveDamage(self, damage:int) -> None:
        """
        Applies incoming damage to the soldier.

        Parameters:
            damage (int): Amount of damage received.

        Returns:
            None
        """
        # your code here
        self.health -= damage

# Viking

class Viking(Soldier):
    """
    Represents a Viking warrior.

    Inherits from Soldier and adds:
        name (str): The Viking's name.
    """
    def __init__(self, name, health:int, strength:int):
        # your code here
        super().__init__(health, strength)
        self.name = name
    
    def battleCry(self) -> str:
        """
        Returns the Viking's battle cry.

        Parameters:
            None

        Returns:
            str: A battle cry string.
        """
        # your code here
        return "Odin Owns You All!"

    def receiveDamage(self, damage) -> str:
        """
        Applies damage to the Viking and returns a combat message.

        Parameters:
            damage (int): Amount of damage received.

        Returns:
            str: Message describing the result of the attack
                 (damage taken or death).
        """

        # your code here
        super().receiveDamage(damage)
        if(self.health>0):
            return "{} has received {} points of damage".format(self.name, damage)
        else:
            return "{} has died in act of combat".format(self.name)

# Saxon

class Saxon(Soldier):
    """
    Represents a Saxon warrior.

    Inherits from Soldier.
    """

    def __init__(self, health:int, strength:int):
        super().__init__(health, strength)

    def receiveDamage(self, damage:int) -> str:
        """
        Applies damage to the Saxon and returns a combat message.

        Parameters:
            damage (int): Amount of damage received.

        Returns:
            str: Message describing the result of the attack.
        """
        # your code here
        super().receiveDamage(damage)
        if(self.health>0):
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"


# Davicente

class War():
    """
    Controls the war between Vikings and Saxons.

    Attributes:
        vikingArmy (list[Viking]): List of all Viking warriors.
        saxonArmy (list[Saxon]): List of all Saxon warriors.
    """
    def __init__(self):
        # your code here
        self.vikingArmy:list = []
        self.saxonArmy:list = []

    def addViking(self, viking:Viking):
        """
        Adds a Viking to the Viking army.

        Parameters:
            viking (Viking): Viking instance to be added.

        Returns:
            None
        """
        # your code here
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon:Saxon):
        """
        Adds a Saxon to the Saxon army.

        Parameters:
            saxon (Saxon): Saxon instance to be added.

        Returns:
            None
        """
        # your code here
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        """
        Executes a Viking attack on a random Saxon.

        Parameters:
            None

        Returns:
            str: Combat message describing the result of the attack.
        """
        # your code here
        Saxon_w = random.choice(self.saxonArmy)
        Viking_w = random.choice(self.vikingArmy)
        output_msg = Saxon_w.receiveDamage(Viking_w.strength)

        for s_w in self.saxonArmy:
            if(s_w.health<=0):
                self.saxonArmy.remove(s_w)

        return output_msg
    
    def saxonAttack(self):
        """
        Executes a Saxon attack on a random Viking.

        Parameters:
            None

        Returns:
            str: Combat message describing the result of the attack.
        """
        # your code here
        Saxon = random.choice(self.saxonArmy)
        Viking = random.choice(self.vikingArmy)
        output_msg = Viking.receiveDamage(Saxon.strength)

        for v_w in self.vikingArmy:
            if(v_w.health<=0):
                self.vikingArmy.remove(v_w)

        return output_msg

    def showStatus(self):
        """
        Returns the current status of the war.

        Parameters:
            None

        Returns:
            str: Description of which army is winning or if the war continues.
        """
        # your code here
        if(len(self.saxonArmy)==0):
            return "Vikings have won the war of the century!"
        
        elif(len(self.vikingArmy)==0):
            return "Saxons have fought for their lives and survive another day..."
        
        else:
            return "Vikings and Saxons are still in the thick of battle."