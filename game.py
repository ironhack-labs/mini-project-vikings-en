"""
Game rules
  We're gonna use random values for each stat but in
  a limit for each ´race´, meaning the races are ´Viking´ and ´Saxon´.

  Assuming the Vikings are gonna invade Saxons, the're are less
  vikings on the battlefield than saxons.

  Stats
  Viking's Stats            :
           Health           : [80 -  102]
           Strength         : [8  -   13]
           Viking's Army    : [100 - 160]
           Battle Cry       : "Odin Owns You All!"

  Saxon's Stats             :
          Health            : [60 -  126]
          Strength          : [4  -    9]
          Saxon's Army      : [200 - 260]
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

SAXON_HEALTH_RANGE=     [61,   86]
SAXON_STRENGTH_RANGE=   [4,     7]
SAXON_ARMY_RANGE=       [200, 260]

def generate_random_viking():
  name=     random.choice(VIKING_NAMES)
  health=   random.randint(*VIKING_HEALTH_RANGE)
  strength= random.randint(*VIKING_STRENGTH_RANGE)

  return Viking(name, health, strength)

def generate_random_saxon():
  health=   random.randint(*SAXON_HEALTH_RANGE)
  strength= random.randint(*SAXON_STRENGTH_RANGE)

  return Saxon(health, strength)

def create_armies():
  num_vikings= random.randint(VIKING_ARMY_RANGE[0], VIKING_ARMY_RANGE[1])
  num_saxon=   random.randint(SAXON_ARMY_RANGE[0], SAXON_ARMY_RANGE[1])


  war= War()
  # Adding Vikings
  for _ in range(num_vikings):
    war.addViking(generate_random_viking)
  # Adding Saxons
  for _ in range(num_saxon):
    war.addSaxon(generate_random_saxon)

  return war, num_vikings, num_saxon

def simulate_battle(war, initial_vikings, initial_saxons):
  round_count= 0

  while war.vikingArmy and war.saxonArmy:
    war.vikingAttack()

    if war.saxonArmy:
      war.saxonAttack()
    round_count+= 1

    if round_count% 10== 0:
      vikings_left= len(war.vikingArmy)
      saxons_left= len(war.saxonArmy)
      print(f"Round {round_count}:{20*" "} {vikings_left} Vikings | {saxons_left} Saxons")

    # !!! Dump check
    if round_count> 5000:
      print("Rounds over 5000. Ending simulation")
      break
  
  final_results= war.showStatus()
  print(f"\n{'='*60}")
  print(final_results)
  print("Final results:")
  print(f"Initial vikings: {initial_vikings}")
  print(f"Initial Saxons: {initial_saxons}")
  print(f"Total rounds: {round_count}")

def main():
  war, vk, sx= create_armies()
  simulate_battle(war, vk, sx)

if __name__== "__main__":
  main()