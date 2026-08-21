from time import sleep

class Livro():
    def __init__(self, titulo = "desconhecido", paginas = 0):
        self.titulo = titulo
        self.paginas_total = paginas
        self.pagina_atual = 1

        sleep(1)
        print(f"você abriu o livro: {self.titulo}")
        sleep(1)
        print(f"página atual: {self.pagina_atual}")
        sleep(1)

    def avancar_paginas(self, num):
        self.cont = 0

        if self.pagina_atual == self.paginas_total:
            print(f"você já está na última pagina do livro!")
            sleep(1)
            pass
        else:
            print(f"avançando...")
            sleep(1)

            for contador in range(0, num, 1):
                if self.fim_do_livro():
                    print(f"\nvocê chegou ao fim do livro.")
                    sleep(1)
                    break
                
                self.pagina_atual += 1
                self.cont += 1
                    
                if (
                    self.pagina_atual == self.paginas_total
                    or contador == num - 1
                ):
                    print(f"pág {self.pagina_atual}", end="", flush=True)
                else:
                    print(f"pág {self.pagina_atual}", end=" → ", flush=True)

                sleep(0.5)

            print(f"você avançou {self.cont} páginas")
            sleep(1)
            print(f"página atual: {self.pagina_atual}")
            sleep(1)
            
    def fim_do_livro(self) -> bool:
        return True if self.pagina_atual == self.paginas_total else False
    
livro1 = Livro("Thalys Nogueira", 30)
livro1.avancar_paginas(32)
livro1.avancar_paginas(5)
