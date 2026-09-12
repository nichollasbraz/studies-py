from classes import *

def main():
    g = Warrior("Thalys", 200)
    m = Mage("Nogueira", 10)
    print(g.attack_enemy(m, 100))
    print(g.attack_enemy(m, 100))
    print(g.attack_enemy(m, 100))
    print(g.cure())
    print(m.cure())

if __name__ == "__main__":
    main()