def chamar_notas(nota_1, nota_2):
    if nota_1 <= 0 or nota_1 > 10:
        print("\nInserção inválida.")
        return None

    elif nota_2 <= 0 or nota_2 > 10:
        print("\nInserção inválida.")
        return None

    else:
        media = (nota_1 + nota_2) / 2
        return media

def media_final(media, nota_1, nota_2):
        
    if media >= 7:
        print("\nPrimeira nota: {:.1f}\nSegunda nota: {:.1f}".format(nota_1, nota_2))
        print("Nota final: {:.1f}".format(media))
        print("Candidato aprovado! Parabéns")
    
    else:
        print("\nPrimeira nota: {:.1f}\nSegunda nota: {:.1f}".format(nota_1, nota_2))
        print("Nota final: {:.1f}".format(media))
        print("Candidato reprovado")


nome = (input("Nome do aluno: "))
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
media = chamar_notas(nota_1, nota_2)

if media is not None:
    media_final(media, nota_1, nota_2)
