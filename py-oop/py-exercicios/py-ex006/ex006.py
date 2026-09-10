class Avaliacao:

    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota # PROTEGIDO


    # MÉTODOS ACESSORES

    def get_nota(self): # GETTER
        return self._nota


    def set_nota(self, nota): # SETTER
        if 0 <= nota <= 10:
            self._nota = nota
            return self._nota
        else:
            return f"valor inválido."

    
    