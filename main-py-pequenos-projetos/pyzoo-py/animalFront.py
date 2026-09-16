import os
import animals


def redirect():
    cleanTerminal()
    ascii()
    input("redirecting... press ENTER to continue...")


def cleanTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def ascii():
    print(r'''                           ___   __   __
                          [_  | /  \ /  \
                        PY / /_| () | () |
                         _|____]\__/ \__/_
                     _.-"|   |   |   |   |"-._
                 _.-"|   |   |   |   |   |   |"-._
             _.-"|   |   |   |   |   |   |   |   |"-._
        _.-"`|   |   |   |   |   |   |   |   |   |   |`"-._
    _.-" |   |   |   |.-~|~-.|__ |_..|.__|___|   |   |   | "-._
   "     |   |   |   |'  | ` |  \|~"~|   |   |`-.|   |   |   |  "
         |   |   |  /| _ |   |)  |\  |   |   |   |\  |   |   |  
         |   |   | /`| a)|   |   | | |   |   |   | `\|   |   |  
         |   |   |:` |   |  /|   | | |   |   |   |   |   |   |  
         |   |`-.||` |.-.| ( |   |/  |.  |   |   | `;|\  |   |  
         |   |`-.|`--|_.'|.;\|__/|   |   |  .|   |  ||\\ |   |  
         | _ |   |:--|   | | |   |  /|   |/  |   | .'| \\|   |  
         |("\|  /|/  |   | | |   | ' |   |   |   | / |  :|;  |   
         |`\'|_/`|   |   | .\|   |/`~|=-.|   |   |/  |  `|   |   
         |  `|_.'|   |   | /`|   ||  |   |\  |   |(  |   |   |   
         |   |   |   |   |/  |\  ||  |   | `Y|  /| \ |   |   |   
         |   |   |   |   |  /| Y ||  |   |  || /`|  \|   |   |   
         |   |   |   |  /| | | | ||  |   |  || | ||  |   |   |   
         |   |   |   | "-|-" |/__||  |   | /_|_| |/__|   |   |   
         |   |   |   |   |   |'""|   |   | '"|"  |"""|   |   |   
       __|___|___|___|___|___|___|___|___|___|___|___|___|___|__
                    ᵃᶜᵃᵈᵉᵐⁱᶜ ᵖʳᵒʲᵉᶜᵗ ᵈᵉᵛᵉˡᵒᵖᵉᵈ ᵇʸ ⁿⁱᶜʰᵒˡˡᵃˢ ᵇʳᵃᶻˑ
''')


def registerAnimalMenu():
    """menu para registrar um novo animal."""
    cleanTerminal()
    ascii()

    print("registering a new animal...\n")

    try:
        animal_id = input("animal id: ")
        
        if not animals.isAnimalIdAvailable(animal_id):
            cleanTerminal()
            ascii()
            print(f"> {animal_id}\n")
            print(f"error: animal id {animal_id} already exists.\n")
            input("press ENTER to continue...")
            return

        cleanTerminal()
        ascii()
        print(f"> {animal_id}\n")
        animal_name = input("animal name: ")

        cleanTerminal()
        ascii()
        print(f"> {animal_id}\n")
        print(f"> {animal_name}\n")
        print("available species: Lion, Elephant, Monkey, Giraffe, Penguin\n")
        animal_specie = input("animal species: ")

        cleanTerminal()
        ascii()        
        print(f"> {animal_id}\n")
        print(f"> {animal_name}\n")
        print(f"> {animal_specie}\n")
        animal_age = input("animal age: ")
        
        # criar animal baseado na espécie
        if animal_specie == "Lion":
            animal = animals.Lion(animal_id, animal_name, animal_specie, animal_age)
        elif animal_specie == "Elephant":
            animal = animals.Elephant(animal_id, animal_name, animal_specie, animal_age)
        elif animal_specie == "Monkey":
            animal = animals.Monkey(animal_id, animal_name, animal_specie, animal_age)
        elif animal_specie == "Giraffe":
            animal = animals.Giraffe(animal_id, animal_name, animal_specie, animal_age)
        elif animal_specie == "Penguin":
            animal = animals.Penguin(animal_id, animal_name, animal_specie, animal_age)
        else:
            cleanTerminal()
            ascii()
            print(f"> {animal_id}\n")
            print(f"> {animal_name}\n")
            print(f"> {animal_specie}\n")
            print(f"error: species {animal_specie} not recognized.\n")
            input("press ENTER to continue...")
            return
        
        if animals.registerAnimal(animal):
            cleanTerminal()
            ascii()
            print(f"> {animal_id}\n")
            print(f"> {animal_name}\n")
            print(f"> {animal_specie}\n")
            print(f"> {animal_age}\n")
            print(f"success! {animal_name} ({animal_specie}) registered successfully.")
        else:
            cleanTerminal()
            ascii()
            print(f"> {animal_id}\n")
            print(f"> {animal_name}\n")
            print(f"> {animal_specie}\n")
            print(f"> {animal_age}\n")
            print(f"error: could not register animal.")
        
        input("\npress ENTER to continue...")
    
    except Exception as e:
        cleanTerminal()
        ascii()
        print(f"error: {e}")
        input("\npress ENTER to continue...")


def listAnimalsMenu():
    cleanTerminal()
    ascii()
    
    print("showing registered animals...\n")
    
    animals_list = animals.listAllAnimals()
    
    if not animals_list:
        print("no animals registered yet.")
    else:
        print("┌──────────┬──────────────────────────┬─────────────────┬──────────────┐")
        print("│ id       │ name                     │ species         │ age          │")
        print("├──────────┼──────────────────────────┼─────────────────┼──────────────┤")
        
        for animal_id, animal in animals_list.items():
            aid = str(animal_id)[:8].ljust(8)
            name = animal.getAnimalName()[:24].ljust(24)
            specie = animal.getAnimalSpecie()[:15].ljust(15)
            age = str(animal.getAnimalAge())[:12].ljust(12)
            print(f"│ {aid} │ {name} │ {specie} │ {age} │")
        
        print("└──────────┴──────────────────────────┴─────────────────┴──────────────┘")
    
    input("\npress ENTER to continue...")


def deleteAnimalMenu():
    """menu para deletar um animal."""
    cleanTerminal()
    ascii()
    
    print("deleting an animal...\n")
    
    animals_list = animals.listAllAnimals()
    
    if not animals_list:
        print("no animals registered yet.")
        input("\npress ENTER to continue...")
        return
    
    try:
        animal_id = input("animal id to delete: ")
        
        animal = animals.getAnimal(animal_id)
        
        if animal is None:
            cleanTerminal()
            ascii()
            print(f"> {animal_id}")
            print(f"error: animal with id {animal_id} not found.")
        else:
            animal_name = animal.getAnimalName()
            cleanTerminal()
            ascii()
            print(f"> {animal_id}")
            
            if animals.deleteAnimal(animal_id):
                print(f"success! animal {animal_name} deleted successfully.")
            else:
                print(f"error: could not delete animal.")
        
        input("\npress ENTER to continue...")
    
    except Exception as e:
        cleanTerminal()
        ascii()
        print(f"error: {e}")
        input("\npress ENTER to continue...")


def viewAnimalDetailsMenu():
    """menu para visualizar detalhes de um animal."""
    cleanTerminal()
    ascii()
    
    print("viewing animal details...\n")
    
    animals_list = animals.listAllAnimals()
    
    if not animals_list:
        print("no animals registered yet.")
        input("\npress ENTER to continue...")
        return
    
    try:
        animal_id = input("animal id: ")
        
        animal = animals.getAnimal(animal_id)
        
        if animal is None:
            cleanTerminal()
            ascii()
            print(f"> {animal_id}")
            print(f"error: animal with id {animal_id} not found.")
        else:
            cleanTerminal()
            ascii()
            print(f"> {animal_id}")
            print(f"\ndetails of {animal.getAnimalName()}:\n")
            print(f"id:             {animal.getAnimalId()}")
            print(f"name:           {animal.getAnimalName()}")
            print(f"species:        {animal.getAnimalSpecie()}")
            print(f"age:            {animal.getAnimalAge()}")
            print(f"allowed foods:  {', '.join(animal.getAllowedFoods())}")
        
        input("\npress ENTER to continue...")
    
    except Exception as e:
        cleanTerminal()
        ascii()
        print(f"error: {e}")
        input("\npress ENTER to continue...")


def main():

    msg = "choose an option:\n"

    while True:
        cleanTerminal()
        ascii()

        print(msg)
        print(r'''┌──────────────────────────────────────────────────────────────────────┐
│ 1. register animal   │ 2. list animals       │ 3. view details       │
│ 4. delete animal     │ 5. return             │                       │
└──────────────────────────────────────────────────────────────────────┘''')
        try:
            key = int(input("> "))

            if key == 1:
                registerAnimalMenu()
                msg = "choose an option:\n"
            elif key == 2:
                listAnimalsMenu()
                msg = "choose an option:\n"
            elif key == 3:
                viewAnimalDetailsMenu()
                msg = "choose an option:\n"
            elif key == 4:
                deleteAnimalMenu()
                msg = "choose an option:\n"
            elif key == 5:
                redirect()
                break
            else:
                msg = f"error: choose a number between 1 to 5.\n"
            
        except ValueError:
            msg = f"error: invalid value.\n"
            

if __name__ == "__main__":
    main()
