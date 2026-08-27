from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

a1 = Aluno("José", 17, "Informática", "T601")
print(a1.__dict__)
print(a1.matricula())
print(a1.aniversario())

p1 = Professor("Samuel", 33, "Mestrado", "Biologia")
print(p1.__dict__)
print(p1.aula())
print(p1.aniversario())

f1 = Funcionario("Samara", 21, "Recepcionista", "Administrativo")
print(f1.__dict__)
print(f1.ponto())
print(f1.aniversario())
