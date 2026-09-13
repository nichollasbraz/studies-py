class Thermo():
    def __init__(self, temperatura = 24):
        self.__temperatura = self._ajustar(temperatura)


    def _ajustar(self, valor):
        if valor < 16:
            return "16°C"
        elif valor > 30:
            return "30°C"
        return f"{valor}°C"


    @property
    def temperatura(self):
        return self.__temperatura 


    @temperatura.setter
    def temperatura(self, valor):
        self.__temperatura = self._ajustar(valor)


