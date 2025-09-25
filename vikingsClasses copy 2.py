import random
import time as time
import math
# Soldier


class Soldier:

    BASE_HEALTH = 100
    BASE_STRENGTH = 50
    BASE_MOVEMENT = 3
    BASE_SHIELD = 10
    BASE_RANGE = 10
    BASE_ATCK_SPEED = 1.0
    BASE_CRITICAL_HIT = 1
    
    
    
    ## Define the stats that will be unique to every special soldier unit

    def __init__(self, health, strength, movement, shield, range, atck_speed, crit, position_x, position_y):
        self.health = health or self.BASE_HEALTH
        self.strength = strength or self.BASE_STRENGTH
        self.shield = shield or self.BASE_SHIELD
        self.movement = movement or self.BASE_MOVEMENT
        self.range = range or self.BASE_RANGE
        self.atck_speed = atck_speed or self.BASE_ATCK_SPEED
        self.last_atck_time = 0
        self.crit = crit or self.BASE_CRITICAL_HIT
        self.position_x = position_x
        self.position_y = position_y

        
        
    ## We define the last attack 

    def can_attack(self, target_unit):
        
        current_time = time.time()
        cooldown = 1.0 / self.atck_speed
        distance = self.calculate_distance(target_unit)
        return ((current_time - self.last_atck_time) >= cooldown) and (distance <= self.range)
        
    def attack(self, target_unit):
        
        if self.can_attack(target_unit):
            self.last_atck_time = time.time()
            return self.strength * self.crit
        return 0

    ## We don't need to return anything, we just susbtract the damage from the health

    def receiveDamage(self, damage):
        # first, we use the shield as a extra health bar
        if self.shield > 0:
            if damage <= self.shield:
                self.shield -= damage
                damage = 0
            else:
                damage -= self.shield
                self.shield = 0

        # the remaining damage made, is substracted from the health bar
        self.health -= damage

        # AÑADIR RETURN PARA QUE FUNCIONEN LOS MÉTODOS vikingAttack y saxonAttack
        if self.health <= 0:
            return f"Unit has been eliminated!"
        else:
            return f"Unit took {damage} damage, {self.health:.1f} health remaining"
        
    def calculate_distance(self, other_unit):
        
        x_diff = other_unit.position_x - self.position_x
        y_diff = other_unit.position_y - self.position_y
        distance = math.sqrt((x_diff ** 2) + (y_diff ** 2))
        return distance        
        
        
    def move_to_enemy(self, enemy_units):
        if not enemy_units:
            return
        
        closest_enemy = None
        shortest_distance = float("inf")
        
        for enemy in enemy_units:
            distance = self.calculate_distance(enemy)
            if distance < shortest_distance:
                shortest_distance = distance
                closest_enemy = enemy
        
        # if unit is already too close don't move
        if shortest_distance <= self.range:
            return
        
        x_diff = closest_enemy.position_x - self.position_x
        y_diff = closest_enemy.position_y - self.position_y
        
        direction_x = x_diff / shortest_distance  
        direction_y = y_diff / shortest_distance
        
        self.position_x += direction_x * self.movement
        self.position_y += direction_y * self.movement
        
        # supposing the field is 2000 x 500
        if self.position_x < 0: self.position_x = 0
        if self.position_x > 2000: self.position_x = 2000
        if self.position_y < 0: self.position_y = 0
        if self.position_y > 800: self.position_y = 800

    

# These are the regular viking slodiers, they will have the standard stats for vikings

class Viking(Soldier):
    
    BASE_HEALTH = 140
    BASE_STRENGTH = 60
    
    ## We define viking's properties as the constructor
    
    def __init__(self, name, health, strength, movement, shield, range, atck_speed, crit, position_x, position_y):
        super().__init__(health, strength, movement, shield, range, atck_speed, crit, position_x, position_y)
        self.name = name
        

        
        
    ## Berserk, higher strength, life and movement speed

class berserk(Viking):
    
    BASE_HEALTH = 160
    BASE_STRENGTH = 130
    BASE_MOVEMENT = 8
    BASE_SHIELD = 5
    
    
    def __init__(self, name, health, strength, movement, shield, range, atck_speed, crit, position_x, position_y):
        super().__init__(name, health, strength, movement, shield, range, atck_speed, crit, position_x, position_y)
    
    ## Skjafmlaer, heavy units, higher shield and less movement
    
class skjadmlaer(Viking):
    
    BASE_SHIELD = 40
    BASE_MOVEMENT = 1
    
    def __init__(self, name, health, strength, movement, shield, range, atck_speed, crit, position_x, position_y):
        super().__init__(name, health, strength, movement, shield, range, atck_speed, crit, position_x, position_y)
        
        
    ## Ulfhednar, wolf units, lower health, but lots of attack speed and movement
    
class ulfhednar(Viking):
    
    BASE_HEALTH = 70
    BASE_MOVEMENT = 9
    BASE_ATCK_SPEED = 2
    BASE_RANGE = 5
    BASE_CRITICAL_HIT = 1.6

    def __init__(self, name, health, strength, movement, shield, range, atck_speed, crit, position_x, position_y):
        super().__init__(name, health, strength, movement, shield, range, atck_speed, crit, position_x, position_y)
        
# Saxon

class Saxon(Soldier):
    
    ## We define saxon's constructor, saxons has no names
    
    def __init__(self, health, strength, movement, shield, range, atck_speed,crit, position_x, position_y):
        super().__init__(health, strength, movement, shield, range, atck_speed, crit, position_x, position_y)
        
    ## We define saxon's properties
    

        
    ## Spear units, higher attack speed, range and shield, lower strength

class spear_soldier(Saxon):
    
    BASE_STRENGTH = 30
    BASE_RANGE = 17
    BASE_ATCK_SPEED = 1.3
    BASE_SHIELD = 20
    
    def __init__(self, health, strength, movement, shield, range, atck_speed, crit, position_x, position_y):
        super().__init__(health, strength, movement, shield, range, atck_speed, crit, position_x, position_y)
        
    ## Archers, lots of range, lower strength
    
class archer(Saxon):
    
    BASE_HEALTH = 60
    BASE_STRENGTH = 20
    BASE_RANGE = 150
    BASE_MOVEMENT = 0
    
    def __init__(self, health, strength, movement, shield, range, atck_speed, crit, position_x, position_y):
        super().__init__(health, strength, movement, shield, range, atck_speed, crit, position_x, position_y)
        
class assasin(Saxon):
    
    BASE_HEALTH = 70
    BASE_ATCK_SPEED = 1.8
    BASE_RANGE = 7
    BASE_CRITICAL_HIT = 1.30
    
    def __init__(self, health, strength, movement, shield, range, atck_speed, crit, position_x, position_y):
        super().__init__(health, strength, movement, shield, range, atck_speed, crit, position_x, position_y)

class War():
    
    ## The war constructor sholdn't recieve any arguments, we create the army of both sides
    
    def __init__(self):  
       self.vikingArmy = []
       self.saxonArmy = []

## We define army generators, first, define the size that we want the special units as well as the regular soldiers (max = 1, so if we wannt 800 out of 1000 the size is 0.8)
## We create loops for each unit, and append it to the army list, each of them with they're own stats, as we want them to have the stats that we already defined, we setthem at None



    def vikings_army_generator(self, size=1000):
        regulars_count = int(size * 0.45)
        berserk_count = int(size * 0.25)
        heavys_count = int(size * 0.10)
        wolfs_count = int(size * 0.20)
    
        for i in range(regulars_count):
            name = f"Viking warrior{i+1}"
            pos_x = random.randint(200, 1800)
            pos_y = random.randint(0, 300)
        # USAR LAS ESTADÍSTICAS BASE EN LUGAR DE None
            viking = Viking(name, 
                       Viking.BASE_HEALTH, Viking.BASE_STRENGTH, Viking.BASE_MOVEMENT,
                       Viking.BASE_SHIELD, Viking.BASE_RANGE, Viking.BASE_ATCK_SPEED,
                       Viking.BASE_CRITICAL_HIT, pos_x, pos_y)
            self.vikingArmy.append(viking)
        
        for f in range(berserk_count):
            name = f"Viking berserk {f+1}"
            pos_x = random.randint(0, 2000)
            pos_y = random.randint(0, 300)
        # USAR LAS ESTADÍSTICAS BASE EN LUGAR DE None
            viking2 = berserk(name,
                         berserk.BASE_HEALTH, berserk.BASE_STRENGTH, berserk.BASE_MOVEMENT,
                         berserk.BASE_SHIELD, berserk.BASE_RANGE, berserk.BASE_ATCK_SPEED,
                         berserk.BASE_CRITICAL_HIT, pos_x, pos_y)
            self.vikingArmy.append(viking2)
        
        for j in range(heavys_count):
            name = f"Viking skjadmlaer {j+1}"
            pos_x = random.randint(0, 2000)  # AÑADIR pos_x que faltaba
            pos_y = random.randint(0, 300)   # AÑADIR pos_y que faltaba
        # USAR LAS ESTADÍSTICAS BASE EN LUGAR DE None
            viking3 = skjadmlaer(name,
                           skjadmlaer.BASE_HEALTH, skjadmlaer.BASE_STRENGTH, skjadmlaer.BASE_MOVEMENT,
                           skjadmlaer.BASE_SHIELD, skjadmlaer.BASE_RANGE, skjadmlaer.BASE_ATCK_SPEED,
                           skjadmlaer.BASE_CRITICAL_HIT, pos_x, pos_y)
            self.vikingArmy.append(viking3)
        
        for k in range(wolfs_count):
            name = f"Viking ulfhednar {k+1}"
            pos_x = random.choice([random.randint(0, 200), random.randint(1800, 2000)])
            pos_y = random.randint(0, 300)
        # USAR LAS ESTADÍSTICAS BASE EN LUGAR DE None
            viking4 = ulfhednar(name,
                          ulfhednar.BASE_HEALTH, ulfhednar.BASE_STRENGTH, ulfhednar.BASE_MOVEMENT,
                          ulfhednar.BASE_SHIELD, ulfhednar.BASE_RANGE, ulfhednar.BASE_ATCK_SPEED,
                          ulfhednar.BASE_CRITICAL_HIT, pos_x, pos_y)
            self.vikingArmy.append(viking4)

    def saxons_army_generator(self, size=1000):
        regulars_count = int(size * 0.50)
        spears_count = int(size * 0.25)
        archers_count = int(size * 0.15)
        assasins_count = int(size * 0.10)
    
        for i in range(regulars_count):
            pos_x = random.randint(0, 2000)
            pos_y = 700
        # USAR LAS ESTADÍSTICAS BASE EN LUGAR DE None
            saxon = Saxon(Saxon.BASE_HEALTH, Saxon.BASE_STRENGTH, Saxon.BASE_MOVEMENT,
                     Saxon.BASE_SHIELD, Saxon.BASE_RANGE, Saxon.BASE_ATCK_SPEED,
                     Saxon.BASE_CRITICAL_HIT, pos_x, pos_y)
            self.saxonArmy.append(saxon)
        
        for f in range(spears_count):
            pos_x = random.randint(0, 2000)
            pos_y = 600
        # USAR LAS ESTADÍSTICAS BASE EN LUGAR DE None
            saxon2 = spear_soldier(spear_soldier.BASE_HEALTH, spear_soldier.BASE_STRENGTH, spear_soldier.BASE_MOVEMENT,
                              spear_soldier.BASE_SHIELD, spear_soldier.BASE_RANGE, spear_soldier.BASE_ATCK_SPEED,
                              spear_soldier.BASE_CRITICAL_HIT, pos_x, pos_y)
            self.saxonArmy.append(saxon2)
        
        for j in range(archers_count):
            pos_x = random.randint(0, 2000)
            pos_y = 800
        # USAR LAS ESTADÍSTICAS BASE EN LUGAR DE None
            saxon3 = archer(archer.BASE_HEALTH, archer.BASE_STRENGTH, archer.BASE_MOVEMENT,
                       archer.BASE_SHIELD, archer.BASE_RANGE, archer.BASE_ATCK_SPEED,
                       archer.BASE_CRITICAL_HIT, pos_x, pos_y)
            self.saxonArmy.append(saxon3)
        
        for k in range(assasins_count):
            pos_x = random.choice([random.randint(0, 300), random.randint(1700, 2000)])
            pos_y = 600
        # USAR LAS ESTADÍSTICAS BASE EN LUGAR DE None
            saxon4 = assasin(assasin.BASE_HEALTH, assasin.BASE_STRENGTH, assasin.BASE_MOVEMENT,
                        assasin.BASE_SHIELD, assasin.BASE_RANGE, assasin.BASE_ATCK_SPEED,
                        assasin.BASE_CRITICAL_HIT, pos_x, pos_y)
            self.saxonArmy.append(saxon4)

            
    def massive_army_battle(self, min_size=500, max_size=2000):
        army_size = random.randint(min_size, max_size)

    def move_viking(self):
        for viking in self.vikingArmy:
            viking.move_to_enemy(self.saxonArmy)
            
    def move_saxon(self):
        for saxon in self.saxonArmy:
            saxon.move_to_enemy(self.vikingArmy)
        

    ## We return the saxon's missing health from the vikings attack
    
    def vikingAttack(self):
        if not self.vikingArmy:
            return "No Vikings left alive to fight!!"
        
        if not self.saxonArmy:
            return "No Saxons left to attack!"
        
        viking = random.choice(self.vikingArmy)
        
        targets_in_range = []
        for saxon in self.saxonArmy:
            if viking.can_attack(saxon):
                targets_in_range.append(saxon)

        # If no targets in range, move towards closest enemy
        if not targets_in_range:
            # Find closest saxon with a simple loop
            closest_saxon = self.saxonArmy[0]
            shortest_distance = viking.calculate_distance(closest_saxon)
            
            for saxon in self.saxonArmy:
                distance = viking.calculate_distance(saxon)
                if distance < shortest_distance:
                    shortest_distance = distance
                    closest_saxon = saxon
            
            viking.move_to_enemy([closest_saxon])
            return f"{viking.name} moved closer to the enemy!"
        
        # Attack a random target in range
        target = random.choice(targets_in_range)
        damage = viking.attack(target)
        result = target.receiveDamage(damage)
        
        if target.health <= 0:
            self.saxonArmy.remove(target)
            
        return result
        
    ## We return viking's missing health fromn the saxon's attack
    
    def saxonAttack(self):
        if not self.saxonArmy:
            return "No Saxons left alive to fight!!"
        
        if not self.vikingArmy:
            return "No Vikings left to attack!"
        
        saxon = random.choice(self.saxonArmy)
        
        targets_in_range = []
        for viking in self.vikingArmy:
            if saxon.can_attack(viking):
                targets_in_range.append(viking)

        # If no targets in range, move towards closest enemy  
        if not targets_in_range:
            # Find closest viking with a simple loop
            closest_viking = self.vikingArmy[0]
            shortest_distance = saxon.calculate_distance(closest_viking)
            
            for viking in self.vikingArmy:
                distance = saxon.calculate_distance(viking)
                if distance < shortest_distance:
                    shortest_distance = distance
                    closest_viking = viking
            
            saxon.move_to_enemy([closest_viking])
            return "A Saxon moved closer to the enemy!"
        
        # Attack a random target in range
        target = random.choice(targets_in_range)
        damage = saxon.attack(target)
        result = target.receiveDamage(damage)
        
        if target.health <= 0:
            self.vikingArmy.remove(target)
        
        return result
    

    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        
        elif len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
            
        elif len(self.vikingArmy) >= 1 and len(self.saxonArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."

