import os
import employees
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


def feedAnimalMenu():
    cleanTerminal()
    ascii()
    
    print("feeding an animal...\n")
    
    employees_list = employees.listAllEmployees()
    animals_list = animals.listAllAnimals()
    
    if not employees_list:
        print("no employees registered yet.\n")
        input("press ENTER to continue...")
        return
    
    if not animals_list:
        print("no animals registered yet.\n")
        input("press ENTER to continue...")
        return
    
    try:
        zookeeper_id = input("zookeeper id: ")
        
        cleanTerminal()
        ascii()
        print(f"> {zookeeper_id}\n")
        animal_id = input("animal id: ")
        
        employee = employees.getEmployeeById(zookeeper_id)
        animal = animals.getAnimal(animal_id)
        
        cleanTerminal()
        ascii()
        print(f"> {zookeeper_id}\n")
        print(f"> {animal_id}\n")
        
        if employee is None:
            print(f"error: employee with id {zookeeper_id} not found.")
        elif animal is None:
            print(f"error: animal with id {animal_id} not found.")
        elif employee['role'] != 'Zookeeper':
            print(f"error: employee {employee['name']} is not a zookeeper.")
        else:
            emp_obj = employee['object']
            print(f"allowed foods for {animal.getAnimalName()}: {', '.join(animal.getAllowedFoods())}\n")
            
            food = input("food to give: ")
            
            cleanTerminal()
            ascii()
            print(f"> {zookeeper_id}\n")
            print(f"> {animal_id}\n")
            print(f"> {food}\n")
            
            success, message = emp_obj.feedAnimal(animal, food)
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


def treatAnimalMenu():
    """menu para tratar um animal."""
    cleanTerminal()
    ascii()
    
    print("treating an animal...\n")
    
    employees_list = employees.listAllEmployees()
    animals_list = animals.listAllAnimals()
    
    if not employees_list:
        print("no employees registered yet.\n")
        input("press ENTER to continue...")
        return
    
    if not animals_list:
        print("no animals registered yet.\n")
        input("press ENTER to continue...")
        return
    
    try:
        zookeeper_id = input("zookeeper id: ")
        
        cleanTerminal()
        ascii()
        print(f"> {zookeeper_id}\n")
        animal_id = input("animal id: ")
        
        employee = employees.getEmployeeById(zookeeper_id)
        animal = animals.getAnimal(animal_id)
        
        cleanTerminal()
        ascii()
        print(f"> {zookeeper_id}\n")
        print(f"> {animal_id}\n")
        
        if employee is None:
            print(f"error: employee with id {zookeeper_id} not found.")
        elif animal is None:
            print(f"error: animal with id {animal_id} not found.")
        elif employee['role'] != 'Zookeeper':
            print(f"error: employee {employee['name']} is not a zookeeper.")
        else:
            emp_obj = employee['object']
            success, message = emp_obj.treatAnimal(animal)
            
            print(f"success! {message}")
        
        input("\npress ENTER to continue...")
    
    except Exception as e:
        cleanTerminal()
        ascii()
        print(f"error: {e}\n")
        input("press ENTER to continue...")


def checkUpAnimalMenu():
    cleanTerminal()
    ascii()
    
    print("performing checkup on animal...\n")
    
    employees_list = employees.listAllEmployees()
    animals_list = animals.listAllAnimals()
    
    if not employees_list:
        print("no employees registered yet.\n")
        input("press ENTER to continue...")
        return
    
    if not animals_list:
        print("no animals registered yet.\n")
        input("press ENTER to continue...")
        return
    
    try:
        veterinarian_id = input("veterinarian id: ")
        
        cleanTerminal()
        ascii()
        print(f"> {veterinarian_id}\n")
        animal_id = input("animal id: ")
        
        employee = employees.getEmployeeById(veterinarian_id)
        animal = animals.getAnimal(animal_id)
        
        cleanTerminal()
        ascii()
        print(f"> {veterinarian_id}\n")
        print(f"> {animal_id}\n")
        
        if employee is None:
            print(f"error: employee with id {veterinarian_id} not found.")
        elif animal is None:
            print(f"error: animal with id {animal_id} not found.")
        elif employee['role'] != 'Veterinarian':
            print(f"error: employee {employee['name']} is not a veterinarian.")
        else:
            emp_obj = employee['object']
            success, message = emp_obj.checkUpAnimal(animal)
            
            print(f"success! {message}")
        
        input("\npress ENTER to continue...")
    
    except Exception as e:
        cleanTerminal()
        ascii()
        print(f"error: {e}\n")
        input("press ENTER to continue...")


def prescribeMedicineMenu():
    cleanTerminal()
    ascii()
    
    print("prescribing medicine...\n")
    
    employees_list = employees.listAllEmployees()
    animals_list = animals.listAllAnimals()
    
    if not employees_list:
        print("no employees registered yet.\n")
        input("press ENTER to continue...")
        return
    
    if not animals_list:
        print("no animals registered yet.\n")
        input("press ENTER to continue...")
        return
    
    try:
        veterinarian_id = input("veterinarian id: ")
        
        cleanTerminal()
        ascii()
        print(f"> {veterinarian_id}\n")
        animal_id = input("animal id: ")
        
        cleanTerminal()
        ascii()
        print(f"> {veterinarian_id}\n")
        print(f"> {animal_id}\n")
        medicine = input("medicine: ")
        
        employee = employees.getEmployeeById(veterinarian_id)
        animal = animals.getAnimal(animal_id)
        
        cleanTerminal()
        ascii()
        print(f"> {veterinarian_id}\n")
        print(f"> {animal_id}\n")
        print(f"> {medicine}\n")
        
        if employee is None:
            print(f"error: employee with id {veterinarian_id} not found.")
        elif animal is None:
            print(f"error: animal with id {animal_id} not found.")
        elif employee['role'] != 'Veterinarian':
            print(f"error: employee {employee['name']} is not a veterinarian.")
        else:
            emp_obj = employee['object']
            success, message = emp_obj.prescribeMedicine(animal, medicine)
            
            print(f"success! {message}")
        
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
│ 1. feed animal       │ 2. treat animal       │ 3. checkup animal     │ 
│ 4. presc. medicine   │ 5. return             │                       │                                              
└──────────────────────────────────────────────────────────────────────┘''')
        try:
            key = int(input("> "))

            if key == 1:
                feedAnimalMenu()
                msg = "choose an option:\n"
            elif key == 2:
                treatAnimalMenu()
                msg = "choose an option:\n"
            elif key == 3:
                checkUpAnimalMenu()
                msg = "choose an option:\n"
            elif key == 4:
                prescribeMedicineMenu()
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
