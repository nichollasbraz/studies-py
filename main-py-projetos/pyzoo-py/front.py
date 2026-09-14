import animalFront
import employeesFront
import enclosureFront
import animalCareFront
import activitiesFront
import os


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


def menu():

    msg = "welcome to PyZoo! choose an option:\n"

    while True:
        cleanTerminal()
        ascii()

        print(msg)
        print(r'''┌──────────────────────────────────────────────────────────────────────┐
│ 1. animals           │ 2. employees          │ 3. enclosures         │
│ 4. animal care       │ 5. activities         │ 6. exit               │
└──────────────────────────────────────────────────────────────────────┘''')
        try:
            key = int(input("> "))

            if key == 1:
                redirect()
                animalFront.main()
                msg = "welcome to PyZoo! choose an option:\n"
            elif key == 2:
                redirect()
                employeesFront.main()
                msg = "welcome to PyZoo! choose an option:\n"
            elif key == 3:
                redirect()
                enclosureFront.main()
                msg = "welcome to PyZoo! choose an option:\n"
            elif key == 4:
                redirect()
                animalCareFront.main()
                msg = "welcome to PyZoo! choose an option:\n"
            elif key == 5:
                redirect()
                activitiesFront.main()
                msg = "welcome to PyZoo! choose an option:\n"
            elif key == 6:
                cleanTerminal()
                print("thank you for your time! shutting down...")
                break
            else:
                msg = f"error: choose a number between 1 to 6.\n"
            
        except ValueError:
            msg = f"error: invalid value.\n"
            

if __name__ == "__main__":
    menu()
