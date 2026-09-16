import os
import Tabuleiro
import Exibicao
import Persistencia

def cleanScreen():
    os.system("cls" if os.name == "nt" else "clear")

def ascii():
    print(r"""           ()
           ||q',,'                     
           ||d,~
(,---------------------,)
 ',       q888p       ,'
   \       986       /
    \  8p, d8b ,q8  /
     ) 888a888a888 (
    /  8b` q8p `d8  \              O
   /       689       \             |','
  /       d888b       \      (,---------,)
,'_____________________',     \   ,8,   /
(`__________L|_________`)      ) a888a (    _,_
[___________|___________]     /___`8`___\   }*{
  }:::|:::::}::|::::::{      (,=========,)  -=-
    |::::}::|:::::{:|'  .,.    \:::|:::/    ~`~=
     |}:::::|::{:::|'            ~".,."~`~
      '|:}::|::::|'~`~".,."
        ~`~".,."~`~".,            "~`~".,."~
                   ".,."~`~     
 ____        _        _ _         
| __ )  __ _| |_ __ _| | |__   __ _
|  _ \ / _` | __/ _` | | '_ \ / _` |
| |_) | (_| | || (_| | | | | | (_| |
|____/ \__,_|\__\__,_|_|_| |_|\__,_|
 _   _                  _ 
| \ | | __ ___   ____ _| |  *Projeto acadêmico
|  \| |/ _` \ \ / / _` | |  desenvolvido por 
| |\  | (_| |\ V / (_| | |  Nichollas Braz.
|_| \_|\__,_| \_/ \__,_|_|                                                              
        """)

def asciiVitoria(tab, jogadas, ultima_jogada, resultado):
    cleanScreen()
    Exibicao.asciiExibicao()
    Exibicao.mostrarHUD(tab, jogadas, ultima_jogada, resultado)
   
    print(f"""
  ┌────────────────────────────────────────┐
  │  *             VITÓRIA!             *  │
  ├────────────────────────────────────────┤
  │  A resistência inimiga foi aniquilada  │
  │         Permanecemos sozinhos.         │
  │                                        │
  │   O mar reconhece um único vencedor.   │
  └────────────────────────────────────────┘
        """)
         
def jogar():
    tab = Tabuleiro.Tabuleiro(6, 6, 5, 3)

    jogadas = 0
    ultima_jogada = None
    resultado = None

    while True:
        cleanScreen()
        Exibicao.asciiExibicao()
        Exibicao.mostrarHUD(
            tab,
            jogadas,
            ultima_jogada,
            resultado
        )

        entrada = input(
            "\nDigite uma posição (formato linha e coluna):\n[-1] desistir\n> "
        ).upper()
        
        # SAIR
        if entrada == "-1":
            print("Retornando ao menu...", end=" ")
            input("'ENTER' para continuar...")
            return

        # VALIDAÇÃO
        try:
            linha, coluna = entrada.split()
            linha = ord(linha) - 65
            coluna = int(coluna) - 1

        except:
            print("Entrada inválida.", end=" ")
            input("'ENTER' para continuar...")
            continue

        if not (0 <= linha <= 5 and 0 <= coluna <= 5):
            print("Entrada inválida.", end=" ")
            input("'ENTER' para continuar...")
            continue

        # ATAQUE
        resultado = tab.atirar(linha, coluna)

        if resultado == "OMT":
            print("Posição já atacada.", end=" ")
            input("'ENTER' para continuar...")
            continue

        jogadas += 1
        ultima_jogada = entrada

        # feedback simples
        if resultado == "ÁGUA":
            print("Água!", end=" ")
            input("'ENTER' para continuar...")
            pass
        elif resultado == "PARTE":
            print("*SUB ATINGIDO!*", end=" ")
            input("'ENTER' para continuar...")
            pass
        elif resultado == "NAVIO":
            print("*NAVIO AFUNDADO!*", end=" ")
            input("'ENTER' para continuar...")
        elif resultado == "SUB":
            print("*SUB AFUNDADO!*", end=" ")
            input("'ENTER' para continuar...")
        
        # VERIFICAR VITÓRIAS
        if tab.venceu():
            asciiVitoria(tab, jogadas, ultima_jogada, resultado)
            
            # SALVAR USUÁRIOS
            while True:
                nome = input("Digite seu nome (máx. 15 caracteres):\n> ").strip()

                if len(nome) == 0:
                    asciiVitoria(tab, jogadas, ultima_jogada, resultado)
                    print("Nome inválido.")
                    continue
                elif len(nome) > 15:
                    asciiVitoria(tab, jogadas, ultima_jogada, resultado)
                    print("Máximo de 15 caracteres.")
                    continue

                break
            
            asciiVitoria(tab, jogadas, ultima_jogada, resultado)
            Persistencia.salvarPontuacao(nome, jogadas)
            
            print("Digite seu nome (máx. 15 caracteres):")
            print(f"> {nome}")
            print("Salvo com sucesso!", end=" ")
            input("'ENTER' para continuar...")
            return
        
def menu():
    while True:
        cleanScreen()
        ascii()

        try:
            op = int(input(
                "[1] jogar\n"
                "[2] ranking\n"
                "[3] sair\n> "
            ))
        except:
            print("Entrada inválida.",end=" ")
            input("'ENTER' para continuar...")
            continue

        if op == 1:
            print("Iniciando jogo...", end=" ")
            input("'ENTER' para continuar...")
            jogar()

        elif op == 2:
            cleanScreen()
            ascii()
            Persistencia.mostrarRanking()
            input("'ENTER' para voltar ao menu...")

        elif op == 3:
            print("Encerrando jogo...")
            break

        else:
            print("Entrada inválida.", end=" ")
            input("'ENTER' para continuar...")
