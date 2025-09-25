import random
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from dataclasses import dataclass, field
from typing import List, Optional, Tuple
# Soldier


class Soldier:

    ## Define the properties on the constructor
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    ## Return the strenght of the soldier
    
    def attack(self):
        return self.strength
        
    ## We don't need to return anything, we just susbtract the damage from the health
    
    def receiveDamage(self, damage):
        self.health -= damage

    

# Viking

class Viking(Soldier):
    
    ## We define viking's properties as the constructor
    
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    ## Define battlecry, don't take any arguments and just return a string
    
    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
            

# Saxon

class Saxon(Soldier):
    
    ## We define saxon's constructor, saxons has no names
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    ## We define saxon's properties
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
        
# Davicente

class War():
    
    ## The war constructor sholdn't recieve any arguments, we create the army of both sides
    
    def __init__(self):
       self.vikingArmy = []
       self.saxonArmy = []

    ## We append the new viking to the Viking Army 

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    ## We append the new saxon to the Saxon Army
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    ## We return the saxon's missing health from the vikings attack
    
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        
        result = saxon.receiveDamage(viking.strength)
        
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        
        return result
        
    ## We return viking's missing health fromn the saxon's attack
    
    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        
        result = viking.receiveDamage(saxon.strength)
        
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        
        return result
    

    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        
        elif len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
            
        elif len(self.vikingArmy) >= 1 and len(self.saxonArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."

# ---------- Parâmetros gerais ----------
WORLD_SIZE = 500           # 500 x 500
N_VIKINGS = 15
N_SAXONS  = 15
MAX_TURNS = 500
ATTACK_RANGE = 1           # adjacente (8 vizinhos)
MOVE_SPEED = 1             # 1 célula por turno
RANDOM_SEED = None         # resultados reproduzíveis, ex: 42

if RANDOM_SEED is not None:
    random.seed(RANDOM_SEED)

# ---------- Modelo ----------
@dataclass
class Soldier:
    x: int
    y: int
    hp: int
    atk: int
    name: str
    team: str  # "VIKING" ou "SAXON"
    alive: bool = field(default=True)

    def pos(self) -> Tuple[int, int]:
        return (self.x, self.y)

    def distance_to(self, other: "Soldier") -> float:
        # Distância Euclidiana para decisão de alvo
        return math.hypot(self.x - other.x, self.y - other.y)

    def chebyshev_to(self, other: "Soldier") -> int:
        # Distância Chebyshev para alcance de ataque (adjacente)
        return max(abs(self.x - other.x), abs(self.y - other.y))

    def move_towards(self, target: "Soldier"):
        if not self.alive:
            return
        dx = 0
        dy = 0
        if target.x > self.x: dx = 1
        elif target.x < self.x: dx = -1
        if target.y > self.y: dy = 1
        elif target.y < self.y: dy = -1
        # aplica velocidade
        self.x = max(0, min(WORLD_SIZE - 1, self.x + dx * MOVE_SPEED))
        self.y = max(0, min(WORLD_SIZE - 1, self.y + dy * MOVE_SPEED))

    def attack(self, target: "Soldier"):
        if not (self.alive and target.alive):
            return
        target.hp -= self.atk
        if target.hp <= 0:
            target.alive = False

# ---------- Helpers ----------
def random_free_cell(occupied: set) -> Tuple[int, int]:
    # Tenta encontrar célula livre (simples; evita sobreposição no spawn)
    while True:
        x = random.randint(0, WORLD_SIZE - 1)
        y = random.randint(0, WORLD_SIZE - 1)
        if (x, y) not in occupied:
            occupied.add((x, y))
            return x, y

def create_army(n: int, team: str, name_prefix: str,
                hp_range=(40, 70), atk_range=(8, 14),
                occupied: Optional[set] = None) -> List[Soldier]:
    if occupied is None:
        occupied = set()
    army = []
    for i in range(n):
        x, y = random_free_cell(occupied)
        hp  = random.randint(*hp_range)
        atk = random.randint(*atk_range)
        army.append(Soldier(x, y, hp, atk, f"{name_prefix}{i}", team))
    return army

def nearest_enemy(me: Soldier, enemies: List[Soldier]) -> Optional[Soldier]:
    alive_enemies = [e for e in enemies if e.alive]
    if not alive_enemies:
        return None
    return min(alive_enemies, key=lambda e: me.distance_to(e))

def simulate_turn(vikings: List[Soldier], saxons: List[Soldier]):
    # 1) Movimento
    for unit, foes in ((u, saxons) for u in vikings if u.alive):
        tgt = nearest_enemy(unit, foes)
        if tgt:
            if unit.chebyshev_to(tgt) > ATTACK_RANGE:
                unit.move_towards(tgt)

    for unit, foes in ((u, vikings) for u in saxons if u.alive):
        tgt = nearest_enemy(unit, foes)
        if tgt:
            if unit.chebyshev_to(tgt) > ATTACK_RANGE:
                unit.move_towards(tgt)

    engagements: List[Tuple[Soldier, Soldier]] = []

    for attacker, foes in ((u, saxons) for u in vikings if u.alive):
        tgt = nearest_enemy(attacker, foes)
        if tgt and attacker.chebyshev_to(tgt) <= ATTACK_RANGE:
            engagements.append((attacker, tgt))

    for attacker, foes in ((u, vikings) for u in saxons if u.alive):
        tgt = nearest_enemy(attacker, foes)
        if tgt and attacker.chebyshev_to(tgt) <= ATTACK_RANGE:
            engagements.append((attacker, tgt))

    # Resolve todos os ataques do turno
    for a, t in engagements:
        if a.alive and t.alive:
            a.attack(t)

def alive_list(units: List[Soldier]) -> List[Soldier]:
    return [u for u in units if u.alive]

def outcome(vikings: List[Soldier], saxons: List[Soldier]) -> Optional[str]:
    v_alive = any(u.alive for u in vikings)
    s_alive = any(u.alive for u in saxons)
    if v_alive and s_alive:
        return None
    if v_alive and not s_alive:
        return "VIKINGS"
    if s_alive and not v_alive:
        return "SAXONS"
    return "DRAW"

# ---------- Visualização ----------
def plot_battle(vikings: List[Soldier], saxons: List[Soldier], title: str):
    fig = plt.figure(figsize=(6, 6))
    ax = plt.gca()
    ax.set_xlim(0, WORLD_SIZE)
    ax.set_ylim(0, WORLD_SIZE)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xticks(range(0, WORLD_SIZE + 1, 10))
    ax.set_yticks(range(0, WORLD_SIZE + 1, 10))
    ax.grid(True, which='major')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(title)

    # Vikings: azul | Saxões: vermelho
    for s in vikings:
        if not s.alive:  # desenha mortos mais “apagados”
            rect = patches.Rectangle((s.x, s.y), 1, 1, linewidth=1,
                                     edgecolor='black', facecolor='#6b8fbf', alpha=0.3)
        else:
            rect = patches.Rectangle((s.x, s.y), 1, 1, linewidth=1,
                                     edgecolor='black', facecolor='blue')
        ax.add_patch(rect)

    for s in saxons:
        if not s.alive:
            rect = patches.Rectangle((s.x, s.y), 1, 1, linewidth=1,
                                     edgecolor='black', facecolor='#bf6b6b', alpha=0.3)
        else:
            rect = patches.Rectangle((s.x, s.y), 1, 1, linewidth=1,
                                     edgecolor='black', facecolor='red')
        ax.add_patch(rect)

    # Legenda simples
    plt.text(2, WORLD_SIZE - 4, f"Vikings alive: {len(alive_list(vikings))}", fontsize=9)
    plt.text(2, WORLD_SIZE - 8, f"Saxons alive: {len(alive_list(saxons))}", fontsize=9)
    plt.show()

# ---------- Execução ----------
# Evita spawns sobrepostos entre exércitos usando o mesmo conjunto "occupied"
occupied_cells = set()
vikings = create_army(N_VIKINGS, "VIKING", "V", occupied=occupied_cells)
saxons  = create_army(N_SAXONS,  "SAXON",  "S", occupied=occupied_cells)

# Estado inicial
plot_battle(vikings, saxons, " Vikings (blue) vs Saxons (red)")

# Loop de turnos
winner = None
for turn in range(1, MAX_TURNS + 1):
    simulate_turn(vikings, saxons)
    who = outcome(vikings, saxons)
    if who is not None:
        winner = who
        break

# Estado final
title = f"Winner: {winner}" if winner else f"No winner after {MAX_TURNS} turns"
plot_battle(vikings, saxons, title)

# Imprime resumo
v_alive = len(alive_list(vikings))
s_alive = len(alive_list(saxons))
print(f"Turns executed: {turn if winner else MAX_TURNS}")
print(f"Vikings alive: {v_alive}  |  Saxons alive: {s_alive}")
print("Winner:", winner if winner else "None (Final turn)")
