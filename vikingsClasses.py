import random

"""
VIKINGS VS SAXONS - Battle Simulation
[[DOCUMENT<>! MADE WITH COPILOT<>!]]
    ⣠⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀
⠀⠀⡜⠁⠀⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠋⠷⠶⠱⡄
⠀⢸⣸⣿⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠫⢀⣖⡃⢀⣸⢹
⠀⡇⣿⣿⣶⣤⡀⠀⠀⠙⢆⠀⠀⠀⠀⠀⣠⡪⢀⣤⣾⣿⣿⣿⣿⣸
⠀⡇⠛⠛⠛⢿⣿⣷⣦⣀⠀⣳⣄⠀⢠⣾⠇⣠⣾⣿⣿⣿⣿⣿⣿⣽
⠀⠯⣠⣠⣤⣤⣤⣭⣭⡽⠿⠾⠞⠛⠷⠧⣾⣿⣿⣯⣿⡛⣽⣿⡿⡼
⠀⡇⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣮⡛⢿⠃
⠀⣧⣛⣭⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣷⣎⡇
⠀⡸⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣷⣟⡇
⣜⣿⣿⡧⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⣸⣿⡜⡄
⠉⠉⢹⡇⠀⠀⠀⢀⣞⠡⠀⠀⠀⠀⠀⠀⡝⣦⠀⠀⠀⠀⢿⣿⣿⣹
⠀⠀⢸⠁⠀⠀⢠⣏⣨⣉⡃⠀⠀⠀⢀⣜⡉⢉⣇⠀⠀⠀⢹⡄⠀⠀
⠀⠀⡾⠄⠀⠀⢸⣾⢏⡍⡏⠑⠆⠀⢿⣻⣿⣿⣿⠀⠀⢰⠈⡇⠀⠀
⠀⢰⢇⢀⣆⠀⢸⠙⠾⠽⠃⠀⠀⠀⠘⠿⡿⠟⢹⠀⢀⡎⠀⡇⠀⠀
⠀⠘⢺⣻⡺⣦⣫⡀⠀⠀⠀⣄⣀⣀⠀⠀⠀⠀⢜⣠⣾⡙⣆⡇⠀⠀
⠀⠀⠀⠙⢿⡿⡝⠿⢧⡢⣠⣤⣍⣀⣤⡄⢀⣞⣿⡿⣻⣿⠞⠀⠀⠀
⠀⠀⠀⢠⠏⠄⠐⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠳⢤⣉⢳⠀⠀⠀
⢀⡠⠖⠉⠀⠀⣠⠇⣿⡿⣿⡿⢹⣿⣿⣿⣿⣧⣠⡀⠀⠈⠉⢢⡀⠀
⢿⠀⠀⣠⠴⣋⡤⠚⠛⠛⠛⠛⠛⠛⠛⠛⠙⠛⠛⢿⣦⣄⠀⢈⡇⠀
⠈⢓⣤⣵⣾⠁⣀⣀⠤⣤⣀⠀⠀⠀⠀⢀⡤⠶⠤⢌⡹⠿⠷⠻⢤⡀
⢰⠋⠈⠉⠘⠋⠁⠀⠀⠈⠙⠳⢄⣀⡴⠉⠀⠀⠀⠀⠙⠂⠀⠀⢀⡇
⢸⡠⡀⠀⠒⠂⠐⠢⠀⣀⠀⠀⠀⠀⠀⢀⠤⠚⠀⠀⢸⣔⢄⠀⢾⠀
⠀⠑⠸⢿⠀⠀⠀⠀⢈⡗⠭⣖⡒⠒⢊⣱⠀⠀⠀⠀⢨⠟⠂⠚⠋⠀
⠀⠀⠀⠘⠦⣄⣀⣠⠞⠀⠀⠀⠈⠉⠉⠀⠳⠤⠤⡤⠞⠀  
This program simulates an epic battle between two armies: Vikings and Saxons.
It demonstrates the principles of Object-Oriented Programming (OOP) using Python,
including class inheritance, encapsulation, and interaction between objects.

Main components:
  - Soldier: Base class representing a generic warrior with health and strength.
  - Viking:  A subclass of Soldier with a name, a battle cry, and custom messages.
  - Saxon:   A subclass of Soldier representing a nameless enemy.
  - War:     A class that manages both armies, executes attacks, and reports battle status.

The simulation creates random armies, lets them fight turn by turn, and announces the final outcome.
"""


# Soldier

class Soldier:
  """
  Class Soldier:
      Represents a basic soldier with health and strength attributes.

      This class serves as the foundation for specialized types of soldiers,
      such as Vikings and Saxons, which inherit from it and extend its behavior.

  Attributes:
      health (int): The soldier's current life points. When it reaches 0 or below, the soldier is defeated.
      strength (int): The amount of damage the soldier can inflict when attacking.

  Methods:
      attack():
          Returns the soldier's strength value, representing the damage dealt during an attack.

      receiveDamage(damage):
          Reduces the soldier's health by the specified damage amount.
          Does not return any message, as this method is meant to be overridden by subclasses.
  """
  def __init__(self, health, strength):
    self.health, self.strength= health, strength
  
  def attack(self):
    return self.strength

  def receiveDamage(self, damage):
    self.health-= damage

# Viking

class Viking(Soldier):
  """
  Class Viking:
      Represents a Viking warrior, inheriting from Soldier.

      Each Viking has a name, can shout a battle cry, and displays unique messages
      when receiving damage or dying in combat.

  Attributes:
      name (str): The Viking’s personal name.
      health (int): The Viking’s life points.
      strength (int): The Viking’s attack strength.

  Methods:
      battleCry():
          Returns the Viking's iconic battle cry: "Odin Owns You All!".

      receiveDamage(damage):
          Subtracts the given damage from the Viking's health.
          Returns a specific message depending on whether the Viking survives or dies.
  """
  def __init__(self, name, health, strength):
    super().__init__(health, strength)
    self.name= name

  def battleCry(self):
    return "Odin Owns You All!"

  def receiveDamage(self, damage):
    self.health-= damage
    
    if self.health<= 0:
      return f"{self.name} has died in act of combat"
    else:
      return f"{self.name} has received {damage} points of damage"
      

# Saxon

class Saxon(Soldier):
  """
  Class Saxon:
      Represents a Saxon fighter, inheriting from Soldier.

      Saxons are anonymous warriors with no personal names and provide
      generic messages when taking or receiving fatal damage.

  Attributes:
      health (int): The Saxon’s current life points.
      strength (int): The Saxon’s attack strength.

  Methods:
      receiveDamage(damage):
          Subtracts the given damage from the Saxon’s health.
          Returns a general message based on whether the Saxon survives or dies.
  """
  def __init__(self, health, strength):
     super().__init__(health, strength)

  def receiveDamage(self, damage):
    self.health-= damage
    if self.health<= 0:
      return f"A Saxon has died in combat"
    else:
      return f"A Saxon has received {damage} points of damage"

# Davicente

class War():
  """
  Class War:
      Represents the battlefield where Vikings and Saxons fight.

      This class coordinates the interaction between both armies. It manages the
      addition of soldiers, executes attacks between them, and reports the current
      status of the ongoing war.

  Attributes:
      vikingArmy (list): A list containing all Viking instances currently in the army.
      saxonArmy (list): A list containing all Saxon instances currently in the army.

  Methods:
      addViking(viking):
          Adds a Viking object to the Viking army.

      addSaxon(saxon):
          Adds a Saxon object to the Saxon army.

      vikingAttack():
          Selects a random Viking and a random Saxon.
          The chosen Viking attacks the chosen Saxon.
          Removes the Saxon from the army if their health reaches zero or below.
          Returns the result message from the Saxon’s receiveDamage() method.

      saxonAttack():
          Selects a random Saxon and a random Viking.
          The chosen Saxon attacks the chosen Viking.
          Removes the Viking from the army if their health reaches zero or below.
          Returns the result message from the Viking’s receiveDamage() method.

      showStatus():
          Returns a string describing the current state of the war:
              - If all Saxons are dead → Vikings have won.
              - If all Vikings are dead → Saxons have survived.
              - Otherwise → the battle continues.
  """

  def __init__(self):
    self.vikingArmy, self.saxonArmy= [], []

  def addViking(self, viking):
    self.vikingArmy.append(viking)

  def addSaxon(self, saxon):
    self.saxonArmy.append(saxon)
  
  def vikingAttack(self):
    viking, saxon= random.choice(self.vikingArmy), random.choice(self.saxonArmy)

    damage_report= saxon.receiveDamage(viking.strength)
    if saxon.health<= 0:
      self.saxonArmy.remove(saxon)
    
    return damage_report
  
  def saxonAttack(self):
    viking, saxon= random.choice(self.vikingArmy), saxon= random.choice(self.saxonArmy)

    damage_report= viking.receiveDamage(saxon.strength)
    if viking.health<= 0:
      self.vikingArmy.remove(viking)
    
    return damage_report

  def showStatus(self):
    if len(self.vikingArmy) == 0:
      return "Saxons have fought for their lives and survive another day..."
    elif len(self.saxonArmy) == 0:
      return "Vikings have won the war of the century!"
    else:
      return "Vikings and Saxons are still in the thick of battle."