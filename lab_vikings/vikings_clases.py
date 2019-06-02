# Project lab-data-vikings
import random


# Soldier (constructor, ataque y daño)
class Soldier:

# se hace el constructor de Soldier, que tiene que tener 2 atributos: health y strenght:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

# Se define la instancia ataque:
    def attack(self):
        return self.strength

#se define la instancia daño recibido: (no devuelve nada)
    def receive_damage(self, damage):
        self.health = self.health - damage



# Viking

class Viking(Soldier):

# se hace el constructor de Viking, que al añadir un atributo distinto del padre, que es Soldier,
# se tiene que inicializar de nuevo, incoroporando el atributo distinto (name):

    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength) # super() es para llamar al inicializador padre (soldier)

# la instancia attack al no modificarse, utiliza la de soldier

# la isntancia daño recibido, si se modifica:

    def receive_damage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# se añade otra instancia:
    def battle_cry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):

# para Saxon, no hay modificacion del constructor, ni de ataque tampoco

# si hay modificacion de daño recibido, ya que no hay que definir los nombres:

    def receive_damage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"


# War
class War:
    pass
