"""
VIKINGS VS SAXONS - Game Simulation

Description:
    This script controls the full simulation of a battle between Vikings and Saxons.
    It randomly generates armies, manages their encounters through the War class,
    and displays the outcome after each phase of combat.

Game Rules:
    - All stats (health, strength, and army size) are generated randomly within
      predefined ranges for each faction.
    - Vikings are stronger but fewer in number.
    - Saxons are weaker individually but have larger armies.
    - The battle continues until one army is completely defeated or the round limit is reached.

Statistics:
    Viking's Stats:
        Health Range   : [83 - 117]
        Strength Range : [11 - 13]
        Army Size      : [100 - 160]
        Battle Cry     : "Odin Owns You All!"

    Saxon's Stats:
        Health Range   : [61 - 136]
        Strength Range : [4 - 7]
        Army Size      : [200 - 260]

Main Components:
    - generate_random_viking() : Creates and returns a Viking instance with random stats.
    - generate_random_saxon()  : Creates and returns a Saxon instance with random stats.
    - create_armies()          : Builds both armies, adds them to the War instance, and returns it.
    - battle_simulation()      : Executes the round-by-round battle until one side wins.
    - main()                   : Initializes the simulation and starts the battle.
"""

from vikingsClasses import *
import random

VIKING_NAMES= [
  "Leif", "Bjorn", "Ragnar", "Erik", "Sigurd", "Olaf", "Thorfinn", "Ivar",
  "Helga", "Astrid", "Freydis", "Gunnar", "Magnus", "Sven", "Ingrid"
]

VIKING_HEALTH_RANGE=    [83,  117]
VIKING_STRENGTH_RANGE=  [11,   13]
VIKING_ARMY_RANGE=      [100, 160]

SAXON_HEALTH_RANGE=     [61,  136]
SAXON_STRENGTH_RANGE=   [4,     7]
SAXON_ARMY_RANGE=       [200, 260]

def generate_random_viking():
  """
  Function generate_random_viking:
      Creates and returns a Viking instance with randomized attributes.

  Process:
      - Selects a random name from the predefined Viking list.
      - Generates random health and strength values within the Viking stat ranges.
      - Returns a new Viking object ready to be added to the army.

  Returns:
      Viking : A Viking object initialized with random name, health, and strength.
  """
  name=     random.choice(VIKING_NAMES)
  health=   random.randint(*VIKING_HEALTH_RANGE)
  strength= random.randint(*VIKING_STRENGTH_RANGE)

  return Viking(name, health, strength)

def generate_random_saxon():
  """
  Function generate_random_saxon:
      Creates and returns a Saxon instance with randomized attributes.

  Process:
      - Generates random health and strength values within the Saxon stat ranges.
      - Returns a new Saxon object ready to be added to the army.

  Returns:
      Saxon : A Saxon object initialized with random health and strength.
  """
  health=   random.randint(*SAXON_HEALTH_RANGE)
  strength= random.randint(*SAXON_STRENGTH_RANGE)

  return Saxon(health, strength)

def create_armies():
  """
  Function create_armies:
      Initializes both Viking and Saxon armies and adds them to a War instance.

  Process:
      - Randomly determines the number of Vikings and Saxons based on army size ranges.
      - Creates a new War instance.
      - Fills each army with randomly generated units.
      - Returns the War instance and the initial army sizes for tracking.

  Returns:
      tuple : (War instance, int number of Vikings, int number of Saxons)
  """
  num_vikings= random.randint(VIKING_ARMY_RANGE[0], VIKING_ARMY_RANGE[1])
  num_saxon=   random.randint(SAXON_ARMY_RANGE[0], SAXON_ARMY_RANGE[1])


  war= War()
  # Adding Vikings
  for _ in range(num_vikings):
    war.addViking(generate_random_viking())
  # Adding Saxons
  for _ in range(num_saxon):
    war.addSaxon(generate_random_saxon())

  return war, num_vikings, num_saxon

def battle_simulation(war, initial_vikings, initial_saxons):
  """
  Function battle_simulation:
      Runs the full simulation of the war between the Viking and Saxon armies.

  Process:
      - Repeats rounds where Vikings and Saxons alternately attack each other.
      - Displays progress every 10 rounds (showing how many soldiers remain).
      - Stops when one army is wiped out or after 5000 rounds to prevent infinite loops.
      - Prints a summary of results, including final outcome and statistics.

  Args:
      war              : War instance containing both armies.
      initial_vikings  : Initial count of Viking soldiers.
      initial_saxons   : Initial count of Saxon soldiers.

  Returns:
      None : Prints the battle results and final statistics.
  """
  round_count= 0
  while war.vikingArmy and war.saxonArmy:
    war.vikingAttack()

    if war.saxonArmy:
      war.saxonAttack()
    round_count+= 1

    if round_count% 10== 0:
      vikings_left= len(war.vikingArmy)
      saxons_left= len(war.saxonArmy)
      print(f"Round {round_count}:{10*" "} {vikings_left} Vikings | {saxons_left} Saxons")

    # !!! round check
    if round_count> 5000:
      print("Rounds over 5000. Ending simulation")
      break
  
  final_results= war.showStatus()
  print(f"\n{'-'*60}")
  print(final_results)
  print(f"Initial vikings: {initial_vikings}")
  print(f"Initial Saxons: {initial_saxons}")
  print("\nFinal results:")
  print(f"Total rounds: {round_count}")

def main():
  war, vk, sx= create_armies()
  battle_simulation(war, vk, sx)

if __name__== "__main__":
  main()