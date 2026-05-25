def hurricane(tam):
    if (tam >= 135):
        print("\nAcesso liberado! Aproveite!")
        return True
    else:
        print("\nO participante não está apto para andar no Hurricane.")
        return False
    
hurricane(125)
