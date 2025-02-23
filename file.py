from vikingsClasses import Soldier, Viking, Saxon, War
import random

names = ["Layla","Lama","Hassan", "Roaa","Ahmed", "Ren"]
great_war = War()

def createVikingArmy(names: list):
    for i in range(len(names)):
        strength = random.randint(5,50)
        health = random.randint(50,100)
        viking = Viking(names[i], health, strength)
        great_war.addViking(viking)
    return great_war.vikingArmy

def createSaxonArmy():
    n = random.randint(3,7)
    for i in range(n):
        strength = random.randint(1,40)
        health = random.randint(50,100)
        saxon = Saxon(health, strength)
        great_war.addSaxon(saxon)
    return great_war.saxonArmy

def Battle():
    round = 1
    
    while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":   
        #print(great_war.vikingArmy[0].battleCry()) 
        great_war.vikingAttack()
        great_war.saxonAttack()
        print(f"\n\nIn round: {round} \n Viking army: {len(great_war.vikingArmy)} warriors",f"\n Saxon army: {len(great_war.saxonArmy)} warriors")
        print(great_war.showStatus())
        round += 1

def play():
    print("Welcome to the Viking vs Saxon game!")
    print("🔥🔥🔥 The game will start now! 🔥🔥🔥")
    createVikingArmy(names)
    createSaxonArmy()
    Battle()
    
    
play()