from abc import ABC
from datetime import date

class Pessoa(ABC):

    def __init__(self, nome: str, nascimento: int):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nascimento


    @property
    def idade(self):
        return date.today().year - self._nascimento


    @property
    def nascimento(self):
        return self._nascimento


    @idade.setter
    def idade(self, ano):
        raise PermissionError("não é possível alterar a idade. altere o nascimento.")


    @nascimento.setter
    def nascimento(self, ano: int):
        if isinstance(ano, int):
            if 1900 <= ano <= date.today().year:
                self._nascimento = ano
                return self._nascimento
            else:
                raise ValueError("deve ser um número válido.")
        else:
            raise ValueError("deve ser um número inteiro.")


class Aluno(Pessoa):

    def __init__(self, nome: str, nascimento: int, curso: str):
        super().__init__(nome, nascimento)
        self.cursos = ["ADS", "ADM", "ECON", "RI", "CONT"]
        self.curso = curso        

    @property
    def curso(self):
        return self._curso


    @curso.setter
    def curso(self, curso: str):
        cursoUpper = curso.upper().strip()
        if cursoUpper not in self.cursos:
            raise NameError("curso não encontrado na lista.")
        else:
            self._curso = cursoUpper


    def add_curso(self, curso: str) -> bool:
        cursoUpper = curso.upper().strip()
        if cursoUpper not in self.cursos:
            self.cursos.append(cursoUpper)
            return True
        else:
            raise ValueError("curso já está na lista.")
    