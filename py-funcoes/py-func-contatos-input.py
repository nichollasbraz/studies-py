def contatos():
    contatos = []

    somaIdades = 0
    femIdades = 0
    homemMaiorIdade = 0

    for i in range(0,4):
        nome = input("Digite o nome:\n> ")
        
        idade = int(input("Digite a idade:\n> "))
        somaIdades += idade

        sexo = input("Essa pessoa é de qual sexo? (M/F):\n> ").upper()
        
        if sexo == 'M' and idade > homemMaiorIdade:
            homemMaiorIdade = idade
            nomeHomemMaiorIdade = nome

        pessoa = {
        "nome": nome,
        "idade": idade,
        "sexo": sexo
        }
        contatos.append(pessoa)

        if sexo == 'F' and idade < 20:
                femIdades += 1
        
    mediaIdades = somaIdades / 4

    print(
         f"Média da idade do grupo: {mediaIdades}.\n"
         f"Homem com maior idade do grupo: {nomeHomemMaiorIdade} com {homemMaiorIdade} anos.\n"
         f"Mulheres abaixo de 20 anos no grupo: {femIdades}."
          )

contatos()
