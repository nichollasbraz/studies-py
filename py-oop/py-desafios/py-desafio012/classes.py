from abc import ABC, abstractmethod
from random import randint
from random import choice

class Character(ABC):

    def __init__(self, name, health):

        self.name = name
        self.health = health
        self.attacks = []

    def attack_enemy(self, name_enemy, strength = 50):

        if self.health > 0:
            if name_enemy.health <= 0:
                return f"{name_enemy.name} já foi abatido!"
            else:
                enemy_damage_taken = name_enemy.take_damage(strength)
                name_enemy.health -= enemy_damage_taken

                if name_enemy.health <= 0:
                    return  f"{self.name} atacou {name_enemy.name} com {choice(self.attacks)}, recebendo {enemy_damage_taken} de dano. {name_enemy.name} foi abatido!"
                else:
                    return  f"{self.name} atacou {name_enemy.name} com {choice(self.attacks)}, recebendo {enemy_damage_taken} de dano."         
        else:
            return f"{self.name} foi abatido e não pode atacar."  


    def take_damage(self, strength):    

        damage = randint(1, strength)

        return damage
    

    @abstractmethod

    def cure(self):
        pass


class Warrior(Character):

    def __init__(self, name, health):

        super().__init__(name, health)
        self.attacks = ["Falcon Punch", "Fire Kick", "Mortal Headbutt"]

    def cure(self):

        hp = randint(1, 50)
        healings = ["utilizando o Segundo Fôlego", "bebendo uma Poção de Vida", "enrolando Ataduras"]

        if self.health <= 0:
            return f"{self.name} foi abatido e não pode se curar."
        else:
            self.health += hp

            return f"{self.name} curou-se {choice(healings)}, restaurando {hp} de vida."


class Mage(Character):

    def __init__(self, name, health):
        super().__init__(name, health)
        self.attacks = ["Infernal Blaze", "Mind Control", "Death Touch"]

    def cure(self):
        hp = randint(1, 50)
        healings = ["bebendo uma Poção de Vida"]
        
        if self.health <= 0:
            return f"{self.name} foi abatido e não pode se curar."
        else:
            self.health += hp
        
            return f"{self.name} curou-se {choice(healings)}, restaurando {hp} de vida."

