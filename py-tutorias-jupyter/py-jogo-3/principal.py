# principal.py
import exibicao
import frontend 

def main():
    exibicao.boas_vindas()
    frontend.jogar()
    exibicao.despedida()

if __name__ == '__main__': #aqui, testa se está sendo executado diretamente ou se está sendo importado
    main()