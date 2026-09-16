import os
import employees


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


def registerZookeeperMenu():
    cleanTerminal()
    ascii()
    
    print("registering a new zookeeper...\n")
    
    try:
        emp_id = input("employee id: ")
        
        if not employees.isEmployeeIdAvailable(emp_id):
            cleanTerminal()
            ascii()
            print(f"> {emp_id}\n")
            print(f"error: employee id {emp_id} already exists.\n")
            input("press ENTER to continue...")
            return
        
        cleanTerminal()
        ascii()
        print(f"> {emp_id}\n")
        emp_name = input("employee name: ")
        
        zookeeper = employees.Zookeeper(emp_id, emp_name)
        
        cleanTerminal()
        ascii()
        print(f"> {emp_id}\n")
        print(f"> {emp_name}\n")
        
        if zookeeper.registerEmployee():
            print(f"success! zookeeper {emp_name} registered successfully.")
        else:
            print(f"error: could not register zookeeper.")
        
        input("\npress ENTER to continue...")
    
    except Exception as e:
        cleanTerminal()
        ascii()
        print(f"error: {e}\n")
        input("press ENTER to continue...")


def registerVeterinarianMenu():
    cleanTerminal()
    ascii()
    
    print("registering a new veterinarian...\n")
    
    try:
        emp_id = input("employee id: ")
        
        if not employees.isEmployeeIdAvailable(emp_id):
            cleanTerminal()
            ascii()
            print(f"> {emp_id}\n")
            print(f"error: employee id {emp_id} already exists.\n")
            input("press ENTER to continue...")
            return
        
        cleanTerminal()
        ascii()
        print(f"> {emp_id}\n")
        emp_name = input("employee name: ")
        
        veterinarian = employees.Veterinarian(emp_id, emp_name)
        
        cleanTerminal()
        ascii()
        print(f"> {emp_id}\n")
        print(f"> {emp_name}\n")
        
        if veterinarian.registerEmployee():
            print(f"success! veterinarian {emp_name} registered successfully.")
        else:
            print(f"error: could not register veterinarian.")
        
        input("\npress ENTER to continue...")
    
    except Exception as e:
        cleanTerminal()
        ascii()
        print(f"error: {e}\n")
        input("press ENTER to continue...")


def listEmployeesMenu():
    cleanTerminal()
    ascii()
    
    print("showing registered employees...\n")
    
    employees_list = employees.listAllEmployees()
    
    if not employees_list:
        print("no employees registered yet.")
    else:
        print("┌──────────┬────────────────────────────────┬──────────────────────────┐")
        print("│ id       │ name                           │ role                     │")
        print("├──────────┼────────────────────────────────┼──────────────────────────┤")
        
        for emp_id, emp_info in employees_list.items():
            eid = str(emp_id)[:8].ljust(8)
            name = emp_info['name'][:30].ljust(30)
            role = emp_info['role'][:24].ljust(24)
            print(f"│ {eid} │ {name} │ {role} │")
        
        print("└──────────┴────────────────────────────────┴──────────────────────────┘")
    
    input("\npress ENTER to continue...")


def deleteEmployeeMenu():
    cleanTerminal()
    ascii()
    
    print("deleting an employee...\n")
    
    employees_list = employees.listAllEmployees()
    
    if not employees_list:
        print("no employees registered yet.\n")
        input("press ENTER to continue...")
        return
    
    try:
        emp_id = input("employee id to delete: ")
        
        employee = employees.getEmployeeById(emp_id)
        
        if employee is None:
            cleanTerminal()
            ascii()
            print(f"> {emp_id}\n")
            print(f"error: employee with id {emp_id} not found.")
        else:
            emp_name = employee['name']
            emp_obj = employee['object']
            
            cleanTerminal()
            ascii()
            print(f"> {emp_id}\n")
            
            if emp_obj.deleteEmployee():
                print(f"success! employee {emp_name} deleted successfully.")
            else:
                print(f"error: could not delete employee.")
        
        input("\npress ENTER to continue...")
    
    except Exception as e:
        cleanTerminal()
        ascii()
        print(f"error: {e}\n")
        input("press ENTER to continue...")


def viewEmployeeActivitiesMenu():
    cleanTerminal()
    ascii()
    
    print("viewing employee activities...\n")
    
    employees_list = employees.listAllEmployees()
    
    if not employees_list:
        print("no employees registered yet.\n")
        input("press ENTER to continue...")
        return
    
    try:
        emp_id = input("employee id: ")
        
        employee = employees.getEmployeeById(emp_id)
        
        if employee is None:
            cleanTerminal()
            ascii()
            print(f"> {emp_id}\n")
            print(f"error: employee with id {emp_id} not found.")
        else:
            emp_obj = employee['object']
            activities = emp_obj.getActivities()
            
            cleanTerminal()
            ascii()
            print(f"> {emp_id}\n")
            
            if not activities:
                print(f"no activities recorded for {employee['name']} yet.")
            else:
                print(f"activities of {employee['name']}:\n")
                for i, activity in enumerate(activities, 1):
                    print(f"{i}. [{activity['timestamp']}]")
                    print(f"   {activity['activity']}\n")
        
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
│ 1. reg. zookeeper    │ 2. reg. veterinarian  │ 3. list employees     │
│ 4. delete employee   │ 5. view activities    │ 6. return             │
└──────────────────────────────────────────────────────────────────────┘''')
        try:
            key = int(input("> "))

            if key == 1:
                registerZookeeperMenu()
                msg = "choose an option:\n"
            elif key == 2:
                registerVeterinarianMenu()
                msg = "choose an option:\n"
            elif key == 3:
                listEmployeesMenu()
                msg = "choose an option:\n"
            elif key == 4:
                deleteEmployeeMenu()
                msg = "choose an option:\n"
            elif key == 5:
                viewEmployeeActivitiesMenu()
                msg = "choose an option:\n"
            elif key == 6:
                redirect()
                break
            else:
                msg = "error: choose a number between 1 to 6.\n"
            
        except ValueError:
            msg = "error: invalid value.\n"


if __name__ == "__main__":
    main()
