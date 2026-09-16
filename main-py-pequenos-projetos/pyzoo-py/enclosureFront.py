import os
import enclosures
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


def createEnclosureMenu():
    cleanTerminal()
    ascii()
    
    print("creating a new enclosure...\n")
    
    try:
        enclosure_id = input("enclosure id: ")
        
        if not enclosures.isEnclosureIdAvailable(enclosure_id):
            cleanTerminal()
            ascii()
            print(f"> {enclosure_id}\n")
            print(f"error: enclosure id {enclosure_id} already exists.\n")
            input("press ENTER to continue...")
            return
        
        cleanTerminal()
        ascii()
        print(f"> {enclosure_id}\n")
        enclosure_name = input("enclosure name: ")
        
        cleanTerminal()
        ascii()
        print(f"> {enclosure_id}\n")
        print(f"> {enclosure_name}\n")
        print("available types: Savanna, Forest, Aquatic\n")
        enclosure_type = input("enclosure type: ")
        
        cleanTerminal()
        ascii()
        print(f"> {enclosure_id}\n")
        print(f"> {enclosure_name}\n")
        print(f"> {enclosure_type}\n")
        
        try:
            capacity = int(input("capacity (max animals): "))
        except ValueError:
            print("error: capacity must be a number.\n")
            input("press ENTER to continue...")
            return
        
        if enclosure_type == "Savanna":
            enclosure = enclosures.SavannhaEnclosure(enclosure_id, enclosure_name, capacity)
        elif enclosure_type == "Forest":
            enclosure = enclosures.ForestEnclosure(enclosure_id, enclosure_name, capacity)
        elif enclosure_type == "Aquatic":
            enclosure = enclosures.AquaticEnclosure(enclosure_id, enclosure_name, capacity)
        else:
            cleanTerminal()
            ascii()
            print(f"> {enclosure_id}\n")
            print(f"> {enclosure_name}\n")
            print(f"> {enclosure_type}\n")
            print(f"> {capacity}\n")
            print(f"error: enclosure type {enclosure_type} not recognized.\n")
            input("press ENTER to continue...")
            return
        
        cleanTerminal()
        ascii()
        print(f"> {enclosure_id}\n")
        print(f"> {enclosure_name}\n")
        print(f"> {enclosure_type}\n")
        print(f"> {capacity}\n")
        
        if enclosures.registerEnclosure(enclosure):
            print(f"success! enclosure {enclosure_name} created successfully.")
        else:
            print(f"error: could not create enclosure.")
        
        input("\npress ENTER to continue...")
    
    except Exception as e:
        cleanTerminal()
        ascii()
        print(f"error: {e}\n")
        input("press ENTER to continue...")


def listEnclosuresMenu():
    cleanTerminal()
    ascii()
    
    print("showing registered enclosures...\n")
    
    enclosures_list = enclosures.listAllEnclosures()
    
    if not enclosures_list:
        print("no enclosures registered yet.")
    else:
        print("┌──────────┬────────────────────────┬──────────────┬───────────────────┐")
        print("│ id       │ name                   │ type         │ occupancy         │")
        print("├──────────┼────────────────────────┼──────────────┼───────────────────┤")
        
        for enc_id, enclosure in enclosures_list.items():
            eid = str(enc_id)[:8].ljust(8)
            name = enclosure.getEnclosureName()[:22].ljust(22)
            enc_type = enclosure.getEnclosureType()[:12].ljust(12)
            occupancy = f"{enclosure.getCurrentOccupancy()}/{enclosure.getCapacity()}"[:17].ljust(17)
            print(f"│ {eid} │ {name} │ {enc_type} │ {occupancy} │")
        
        print("└──────────┴────────────────────────┴──────────────┴───────────────────┘")
    
    input("\npress ENTER to continue...")


def addAnimalToEnclosureMenu():
    cleanTerminal()
    ascii()
    
    print("adding animal to enclosure...\n")
    
    enclosures_list = enclosures.listAllEnclosures()
    animals_list = animals.listAllAnimals()
    
    if not enclosures_list:
        print("no enclosures registered yet.\n")
        input("press ENTER to continue...")
        return
    
    if not animals_list:
        print("no animals registered yet.\n")
        input("press ENTER to continue...")
        return
    
    try:
        enclosure_id = input("enclosure id: ")
        
        cleanTerminal()
        ascii()
        print(f"> {enclosure_id}\n")
        animal_id = input("animal id: ")
        
        enclosure = enclosures.getEnclosure(enclosure_id)
        animal = animals.getAnimal(animal_id)
        
        cleanTerminal()
        ascii()
        print(f"> {enclosure_id}\n")
        print(f"> {animal_id}\n")
        
        if enclosure is None:
            print(f"error: enclosure with id {enclosure_id} not found.")
        elif animal is None:
            print(f"error: animal with id {animal_id} not found.")
        else:
            success, message = enclosure.addAnimal(animal)
            if success:
                print(f"success! {message}")
            else:
                print(f"error! {message}")
        
        input("\npress ENTER to continue...")
    
    except Exception as e:
        cleanTerminal()
        ascii()
        print(f"error: {e}\n")
        input("press ENTER to continue...")


def viewEnclosureDetailsMenu():
    cleanTerminal()
    ascii()
    
    print("viewing enclosure details...\n")
    
    enclosures_list = enclosures.listAllEnclosures()
    
    if not enclosures_list:
        print("no enclosures registered yet.\n")
        input("press ENTER to continue...")
        return
    
    try:
        enclosure_id = input("enclosure id: ")
        
        enclosure = enclosures.getEnclosure(enclosure_id)
        
        cleanTerminal()
        ascii()
        print(f"> {enclosure_id}\n")
        
        if enclosure is None:
            print(f"error: enclosure with id {enclosure_id} not found.")
        else:
            print(f"\ndetails of {enclosure.getEnclosureName()}:\n")
            print(f"id:         {enclosure.getEnclosureId()}")
            print(f"name:       {enclosure.getEnclosureName()}")
            print(f"type:       {enclosure.getEnclosureType()}")
            print(f"capacity:   {enclosure.getCapacity()}")
            print(f"occupancy:  {enclosure.getCurrentOccupancy()}")
            
            enc_animals = enclosure.getAnimals()
            print(f"\nanimals in this enclosure:")
            
            if not enc_animals:
                print("  no animals in this enclosure.")
            else:
                for animal in enc_animals:
                    print(f"  - {animal.getAnimalName()} ({animal.getAnimalSpecie()})")
        
        input("\npress ENTER to continue...")
    
    except Exception as e:
        cleanTerminal()
        ascii()
        print(f"error: {e}\n")
        input("press ENTER to continue...")


def main():
    msg = "choose an option:\n"

    while True:
        cleanTerminal()
        ascii()

        print(msg)
        print(r'''┌──────────────────────────────────────────────────────────────────────┐
│ 1. create enclosure  │ 2. list enclosures    │ 3. add animal         │
│ 4. view details      │ 5. return             │                       │
└──────────────────────────────────────────────────────────────────────┘''')
        try:
            key = int(input("> "))

            if key == 1:
                createEnclosureMenu()
                msg = "choose an option:\n"
            elif key == 2:
                listEnclosuresMenu()
                msg = "choose an option:\n"
            elif key == 3:
                addAnimalToEnclosureMenu()
                msg = "choose an option:\n"
            elif key == 4:
                viewEnclosureDetailsMenu()
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
