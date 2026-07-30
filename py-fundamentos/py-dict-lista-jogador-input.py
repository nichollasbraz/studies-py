jogadorDict = {}
partidasList = []

jogadorDict["jogador"] = str(input("nome do jogador:\n> "))

qtyJogos = int(input("quantidade de partidas:\n> "))

for g in range(1, qtyJogos + 1):
    partidasList.append(int(input(f"quantidade de gols na {g}ª partida:\n> ")))

jogadorDict["gols"] = partidasList[:]
jogadorDict["total"] = sum(partidasList)

print(f"{jogadorDict['jogador']} jogou {len(jogadorDict['gols'])} partidas.")

if jogadorDict["total"] > 1:
    for c, v in enumerate(jogadorDict['gols']):
        if v == 0:
            print(f"não foram feitos gols na {c + 1}ª partida.")
        else:
            print(f"foram feitos {v} gols na {c + 1}ª partida.")
else:
    print(f"o jogador não fez gols em nenhuma partida.")
