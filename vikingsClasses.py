import random

# Soldier

class Soldier:
  """
  Class Soldier:
      Class that represents a generic soldier in battle, with health and strength attributes.
      It serves as the base class for more specific soldier types (Vikings and Saxons).

  Args                :
      health          : is the amount of life points the soldier has; when it reaches 0 or below, the soldier is defeated.
      strength        : is the strength of the soldier, which determines how much damage they deal when attacking.

  methods             :
      attack          : returns the soldier's strength as the damage they can inflict.
      receiveDamage   : reduces the soldier's health by the given damage amount.

  returns             : nothing because the class is meant to be inherited and extended by subclasses.
  """
  def __init__(self, health, strength):
    self.health= health
    self.strength= strength
  
  def attack(self):
    return self.strength

  def receiveDamage(self, damage):
    self.health-= damage

# Viking

class Viking(Soldier):
  """
  Class Viking:
      Class that represents a Viking warrior, inheriting from Soldier.
      Vikings have a name, can shout a battle cry, and provide specific messages when damaged.

  Args                :
      name            : is the name of the Viking warrior.
      health          : is the amount of life points the Viking has.
      strength        : is the strength of the Viking, used for attacking.

  methods             :
      battleCry       : returns the Viking's iconic battle cry.
      receiveDamage   : overrides the parent method to return a custom message when damaged or killed.
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
      Class that represents a Saxon soldier, inheriting from Soldier.
      Saxons do not have names and use generic messages when damaged.

  Args                :
      health          : is the amount of life points the Saxon has.
      strength        : is the strength of the Saxon, used for attacking.

  methods             :
      receiveDamage   : overrides the parent method to return a generic message when damaged or killed.
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
      Class that simulates a battle between two armies: Vikings and Saxons.
      It manages the armies, handles attacks, and reports the current status of the war.

  Args                :
      (none)          : the class initializes with empty Viking and Saxon armies.

  methods             :
      addViking       : adds a Viking instance to the Viking army.
      addSaxon        : adds a Saxon instance to the Saxon army.
      vikingAttack    : selects a random Viking to attack a random Saxon; removes dead Saxons.
      saxonAttack     : selects a random Saxon to attack a random Viking; removes dead Vikings.
      showStatus      : returns a string describing the current outcome of the war.
  """
  def __init__(self):
    self.vikingArmy= []
    self.saxonArmy= []

  def addViking(self, viking):
    self.vikingArmy.append(viking)

  def addSaxon(self, saxon):
    self.saxonArmy.append(saxon)
  
  def vikingAttack(self):
    viking= random.choice(self.vikingArmy)
    saxon= random.choice(self.saxonArmy)

    halved_health= saxon.receiveDamage(viking.strength)
    if saxon.health<= 0:
      self.saxonArmy.remove(saxon)
    
    return halved_health
  
  def saxonAttack(self):
    viking= random.choice(self.vikingArmy)
    saxon= random.choice(self.saxonArmy)

    halved_health= viking.receiveDamage(saxon.strength)
    if viking.health<= 0:
      self.vikingArmy.remove(viking)
    
    return halved_health

  def showStatus(self):
    if len(self.vikingArmy) == 0:
      return "Saxons have fought for their lives and survive another day..."
    elif len(self.saxonArmy) == 0:
      return "Vikings have won the war of the century!"
    else:
      return "Vikings and Saxons are still in the thick of battle."