import os
import activities
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


def registerActivityMenu():
    cleanTerminal()
    ascii()
    
    print("registering a new activity...\n")
    
    employees_list = employees.listAllEmployees()
    
    if not employees_list:
        print("no employees registered yet.")
        input("\npress ENTER to continue...")
        return
    
    try:
        emp_id = input("employee id: ")
        
        cleanTerminal()
        ascii()
        print(f"> {emp_id}\n")
        
        employee = employees.getEmployeeById(emp_id)
        
        if employee is None:
            print(f"error: employee with id {emp_id} not found.")
        else:
            print("activity types: feeding, treatment, checkup, cleaning, medicine\n")
            activity_type = input("activity type: ")
            
            cleanTerminal()
            ascii()
            print(f"> {emp_id}\n")
            print(f"> {activity_type}\n")
            description = input("description: ")
            
            success, activity_id = activities.registerActivity(emp_id, activity_type, description)
            
            cleanTerminal()
            ascii()
            print(f"> {emp_id}\n")
            print(f"> {activity_type}\n")
            print(f"> {description}\n")
            
            if success:
                print(f"success! activity {activity_id} registered.")
            else:
                print(f"error: could not register activity.")
        
        input("\npress ENTER to continue...")
    
    except Exception as e:
        cleanTerminal()
        ascii()
        print(f"error: {e}\n")
        input("press ENTER to continue...")


def listAllActivitiesMenu():
    cleanTerminal()
    ascii()
    
    print("showing all activities...\n")
    
    activities_list = activities.listAllActivities()
    
    if not activities_list:
        print("no activities registered yet.")
    else:
        print("┌───────────┬──────────┬────────────────┬──────────────────────────────┐")
        print("│ id        │ emp id   │ type           │ timestamp                    │")
        print("├───────────┼──────────┼────────────────┼──────────────────────────────┤")
        
        for activity_id, activity in activities_list.items():
            info = activity.getActivityInfo()
            aid = str(activity_id)[:9].ljust(9)
            emp = str(info['employee_id'])[:8].ljust(8)
            act_type = info['type'][:14].ljust(14)
            timestamp = info['timestamp'][:28].ljust(28)
            print(f"│ {aid} │ {emp} │ {act_type} │ {timestamp} │")
        
        print("└───────────┴──────────┴────────────────┴──────────────────────────────┘")
    
    input("\npress ENTER to continue...")


def listEmployeeActivitiesMenu():
    cleanTerminal()
    ascii()
    
    print("showing employee activities...\n")
    
    employees_list = employees.listAllEmployees()
    
    if not employees_list:
        print("no employees registered yet.")
        input("\npress ENTER to continue...")
        return
    
    try:
        emp_id = input("employee id: ")
        
        employee = employees.getEmployeeById(emp_id)
        
        cleanTerminal()
        ascii()
        print(f"> {emp_id}\n")
        
        if employee is None:
            print(f"error: employee with id {emp_id} not found.")
        else:
            emp_activities = activities.listActivitiesByEmployee(emp_id)
            
            if not emp_activities:
                print(f"no activities for employee {employee['name']} yet.")
            else:
                print(f"activities of {employee['name']}:\n")
                for activity_id, activity in emp_activities.items():
                    info = activity.getActivityInfo()
                    print(f"[{info['id']}] {info['timestamp']}")
                    print(f"  type: {info['type']}")
                    print(f"  description: {info['description']}\n")
        
        input("\npress ENTER to continue...")
    
    except Exception as e:
        cleanTerminal()
        ascii()
        print(f"error: {e}\n")
        input("press ENTER to continue...")


def listActivitiesByTypeMenu():
    cleanTerminal()
    ascii()
    
    print("showing activities by type...\n")
    
    print("activity types: feeding, treatment, checkup, cleaning, medicine\n")
    activity_type = input("activity type: ")
    
    try:
        cleanTerminal()
        ascii()
        print(f"> {activity_type}\n")
        
        type_activities = activities.listActivitiesByType(activity_type)
        
        if not type_activities:
            print(f"no activities of type '{activity_type}' found.")
        else:
            print(f"activities of type '{activity_type}':\n")
            for activity_id, activity in type_activities.items():
                info = activity.getActivityInfo()
                print(f"[{info['id']}] {info['timestamp']} | employee: {info['employee_id']}")
                print(f"  description: {info['description']}\n")
        
        input("\npress ENTER to continue...")
    
    except Exception as e:
        cleanTerminal()
        ascii()
        print(f"error: {e}\n")
        input("press ENTER to continue...")


def viewStatisticsMenu():
    cleanTerminal()
    ascii()
    
    print("viewing activity statistics...\n")
    
    total_activities = activities.getActivityCount()
    print(f"total activities: {total_activities}\n")
    
    activity_types = ['feeding', 'treatment', 'checkup', 'cleaning', 'medicine']
    
    print("breakdown by type:")
    for act_type in activity_types:
        count = activities.getActivityCountByType(act_type)
        print(f"  {act_type:15} : {count}")
    
    input("\npress ENTER to continue...")


def main():
    msg = "choose an option:\n"

    while True:
        cleanTerminal()
        ascii()

        print(msg)
        print(r'''┌──────────────────────────────────────────────────────────────────────┐
│ 1. register activity │ 2. all activities     │ 3. emp. activities    │
│ 4. actv. by type     │ 5. statistics         │ 6. return             │
└──────────────────────────────────────────────────────────────────────┘''')
        try:
            key = int(input("> "))

            if key == 1:
                registerActivityMenu()
                msg = "choose an option:\n"
            elif key == 2:
                listAllActivitiesMenu()
                msg = "choose an option:\n"
            elif key == 3:
                listEmployeeActivitiesMenu()
                msg = "choose an option:\n"
            elif key == 4:
                listActivitiesByTypeMenu()
                msg = "choose an option:\n"
            elif key == 5:
                viewStatisticsMenu()
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
