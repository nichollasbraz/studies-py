class Retangulo():

    def __init__(self, base = 1, altura = 1):
        self._base = None
        self._altura = None
        self._area = None
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base


    @property
    def altura(self):
        return self._altura


    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area


    @property
    def medidas(self):
        return f"altura : {self._altura}\nbase : {self._base}\nárea : {self.area}"


    @base.setter
    def base(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise ValueError("valor deve ser um número.")
        if valor <= 0:
            raise ValueError("valor não pode ser igual ou menor que zero.")
        else:
            self._base = valor

            print(f"valor alterado com êxito. ({valor})")


    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise ValueError("valor deve ser um número.")
        if valor <= 0:  
            raise ValueError("valor não pode ser igual ou menor que zero.")
        else:
            self._altura = valor
                        
            print(f"valor alterado com êxito. ({valor})")


    @area.setter
    def area(self, valor):
        raise PermissionError("área não pode ser configurada dessa forma.")


    @medidas.setter
    def medidas(self, valores: tuple):
        if not isinstance(valores, tuple):
            raise TypeError("medidas devem ser informadas dentro de uma tupla.")
        if len(valores) != 2:
            raise SyntaxError("medidas devem ser informadas dentro de uma tupla.")
        if isinstance(valores[0], float) or isinstance(valores[0], int):
            self._base = valores[0]

            print(f"valor alterado com êxito. ({valores[0]})")
        else:
            raise ValueError("valor deve ser um número.")
        if isinstance(valores[1], float) or isinstance(valores[1], int):
            self._altura = valores[1]

            print(f"valor alterado com êxito. ({valores[1]})")
        else:
            raise ValueError("valor deve ser um número.")

        self._area = self._base * self._altura
        return self._area