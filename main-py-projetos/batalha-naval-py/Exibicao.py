def simbolo(tab, i, j):
    if (i, j) not in tab.posicoesAtacadas:
        return "█"
    if tab.getPosicao(i, j) == 0:
        return "_"

    nome = tab.posicaoParaEmbarcacao.get((i, j))

    if nome:
        if tab._afundou(nome):
            return "X"
        return "⌖"

    return "?"

def asciiExibicao():
    print("""                _._
                 :.
                 : :
                 :  .                 
                .:   :         _,_
               : :    .        }*{          
              :  :     :       -=-
             .   :.     .       ~`~=.
            :    ::      :        
           :     :::      .
          .      :::.      :
         :       ::::       .
        :        :::::       :
       .=w=w=w=w=::::::.      .
                  :=w=w=w=w=w=w=.   ....
<---._______:U~~~~~~~~\\_________.:---/
 \\::}::::}::}==================={:{:/
  '~`~".,."~`~=    ".,."~`~   ~`~.,."~`~".
          .`~          `."~`~".  ~`~=    ".,."~`~
                   ~`~=.             ~` 
""")
    
def mostrarHUD(tab, jogadas, ultima_jogada, resultado):
    linhas_tabuleiro = []

    for i in range(tab.numLinhas):
        letra = chr(ord("A") + i)
        linha = [simbolo(tab, i, j) for j in range(tab.numColunas)]
        linhas_tabuleiro.append(f"{letra} │ {'  '.join(linha)} │")

    hud = [
        f"JOGADA  :  {jogadas}",
        f"NAVIOS  :  {tab.navios_afundados}/5",
        f"SUBMAR  :  {tab.submarinos_afundados}/3",
        "",
        f"ÚLTIMO  :  {ultima_jogada if ultima_jogada else '-'}",
        f"RESULT  :  {resultado if resultado else '-'}"
    ]

    print("    1  2  3  4  5  6      S  T  A  T  U  S  ")
    print("  ┌──────────────────┐  ┌──────────────────┐")

    for i in range(tab.numLinhas):

        esquerda = linhas_tabuleiro[i]

        direita = hud[i] if i < len(hud) else ""

        print(f"{esquerda}  │ {direita:<16} │")

    print("  └──────────────────┘  └──────────────────┘")

def mostrarCaracteresUsados():
    print("O caractere _ é usado para água")
    print("O caractere X é usado para embarcação afundada")
    print("O caractere ⌖ é usado para embarcação parcialmente atingida")
    print("O caractere █ é usado para posições ainda não exploradas")