import random

AGUA = 0
NAVIO = 1
SUBMARINO = 2

class Tabuleiro:
    def __init__(self, numLinhas, numColunas, numNavios, numSubmarinos):
        self.numLinhas = numLinhas
        self.numColunas = numColunas

        self.tabuleiro = [0] * (numLinhas * numColunas)

        self.posicoesAtacadas = set()
        self.acertos = set()

        self.numNavios = numNavios
        self.numSubmarinos = numSubmarinos

        self.embarcacoes = {}
        self.posicaoParaEmbarcacao = {}

        self.navios_afundados = 0
        self.submarinos_afundados = 0

        self._posicionarBarcos()

    # MATRIZ BASE
    def getPosicao(self, i, j):
        return self.tabuleiro[i * self.numColunas + j]

    def setPosicao(self, i, j, valor):
        self.tabuleiro[i * self.numColunas + j] = valor

    # ATAQUE
    def atirar(self, linha, coluna):
        if (linha, coluna) in self.posicoesAtacadas:
            return "OMT"

        self.posicoesAtacadas.add((linha, coluna))

        valor = self.getPosicao(linha, coluna)

        if valor == AGUA:
            return "ÁGUA"

        self.acertos.add((linha, coluna))

        nome = self.posicaoParaEmbarcacao.get((linha, coluna))

        if nome:
            if self._afundou(nome):
                if valor == NAVIO:
                    self.navios_afundados += 1
                    return "NAVIO"
                else:
                    self.submarinos_afundados += 1
                    return "SUB"

            return "PARTE" # parcial

        return "ACERTO"

    # AFUNDAMENTO
    def _afundou(self, nome):
        for pos in self.embarcacoes[nome]:
            if pos not in self.acertos:
                return False
        
        return True

    # POSICIONAMENTO
    def _posicionarBarcos(self):
        # NAVIOS (1 célula)
        count = 0
        while count < self.numNavios:
            i = random.randint(0, self.numLinhas - 1)
            j = random.randint(0, self.numColunas - 1)

            if self.getPosicao(i, j) == 0:
                self.setPosicao(i, j, NAVIO)

                nome = f"N{count}"
                self.embarcacoes[nome] = {(i, j)}
                self.posicaoParaEmbarcacao[(i, j)] = nome

                count += 1
        # SUBMARINOS (2 células)
        count = 0
        while count < self.numSubmarinos:
            i = random.randint(0, self.numLinhas - 2)
            j = random.randint(0, self.numColunas - 2)

            orient = random.choice(["H", "V"])

            if orient == "H":
                if self.getPosicao(i, j) == 0 and self.getPosicao(i, j + 1) == 0:

                    self.setPosicao(i, j, SUBMARINO)
                    self.setPosicao(i, j + 1, SUBMARINO)

                    nome = f"S{count}"

                    self.embarcacoes[nome] = {(i, j), (i, j + 1)}
                    self.posicaoParaEmbarcacao[(i, j)] = nome
                    self.posicaoParaEmbarcacao[(i, j + 1)] = nome

                    count += 1

            else:
                if self.getPosicao(i, j) == 0 and self.getPosicao(i + 1, j) == 0:
                    self.setPosicao(i, j, SUBMARINO)
                    self.setPosicao(i + 1, j, SUBMARINO)

                    nome = f"S{count}"

                    self.embarcacoes[nome] = {(i, j), (i + 1, j)}
                    self.posicaoParaEmbarcacao[(i, j)] = nome
                    self.posicaoParaEmbarcacao[(i + 1, j)] = nome

                    count += 1
    # VITÓRIA
    def venceu(self):
      total_navios = self.numNavios
      total_submarinos = self.numSubmarinos

      return (
        self.navios_afundados == total_navios and
        self.submarinos_afundados == total_submarinos
      )
