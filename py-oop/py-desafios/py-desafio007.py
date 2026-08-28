import os

def cleanTerminal():
    os.system('cls' if os.name == 'nt' else 'clear') 

def ascii2():
    cleanTerminal()
    print(r'''   o                   o
    \               __/
     \___          /
         \__    __/
            \  /
 ____________\/____________
/   ____________________   \
|  /__/  \__   \__/  \__\  |
| |    __   \__    __   \| |
| |\__/  \__   \__/  \__ | |
| |    __   \__    __   \| |
| |\__/  \__   \__/  \__ | |
| |    __   \__    __   \| |
| |\__/  \__   \__/  \__ | |
| |    __   \__    __   \| |
| |\__/  \__   \__/  \__ | |
|  \________\___________/  |
|                 _   _    |
|  prs           (|) (/)   |
\_________________________/
    "--"           "--"
''')

def ascii():
    cleanTerminal()
    print(r'''   o                   o
    \               __/
     \___          /
         \__    __/
            \  /
 ____________\/____________
/   ____________________   \
|  /                    \  |
| |                      | |
| |                      | |
| |                      | |
| |                      | |
| |                      | |
| |                      | |
| |                      | |
| |                      | |
|  \____________________/  |
|                 _   _    |
|  prs           (|) (|)   |
\_________________________/
    "--"           "--"
''')

class Controle:
    def __init__(self):
        self.tvStats = False
        self.controleVol = 0
        self.controleCh = 1
        
    def tvLigar(self):
        if self.tvStats == False:
            ascii2()
            self.tvStats = True
        else:
            ascii()
            self.tvStats = False

    def mudarCanal(self, entrada):
        if not self.tvStats:
            return
        else:
            if entrada == '>':
                if self.controleCh == 5:
                    self.controleCh = 1
                else:
                    self.controleCh += 1          

            elif entrada == '<':
                if self.controleCh == 1:
                    self.controleCh = 5
                else:
                    self.controleCh -= 1

        return self.controleCh

    def mudarVol(self, entrada):
        if not self.tvStats:
            return
        else:
            if entrada == '+':
                if self.controleVol == 5:
                    return
                else:
                    self.controleVol += 1

            elif entrada == '-':
                if self.controleVol == 0:
                    return
                else:
                    self.controleVol -= 1

            return self.controleVol

    def tvPainel(self):
        if not self.tvStats:
            ascii()
            print(
                f"a TV está desligada\n"
                f"\n[@] ON/OFF\n"
                f"[0] EXIT\n"
                )
        else:
            ascii2()

            print(
                f"a TV está ligada\n"
                f"\nCANAL  :", end= " ")
            
            for canal in range (1,6):
                if canal == self.controleCh:
                    print(f"[{canal}]", end=" ")
                else:
                    print(f"{canal}", end=" ")
            print()

            print(f"VOLUME :", end=" ")
            for volume in range(1, 6):
                if volume <= self.controleVol:
                    print(f"█", end="")
                else:
                    print(f"░", end="")
            print()
            print()


controle = Controle()

while True:
    controle.tvPainel()
    entrada = input(">> ")

    if entrada == '@':
        controle.tvLigar()
        while True:
            controle.tvPainel()

            print(
                f"[-][+] VOL         [<][>] CH\n"
                f"[@] ON/OFF\n")
            entrada = input(">> ")

            if entrada == '>' or entrada == '<':
                controle.mudarCanal(entrada)
            if entrada == '+' or entrada == '-':
                controle.mudarVol(entrada)
            if entrada == '@':
                controle.tvLigar()
                break
            
    elif entrada == '0':
        break
