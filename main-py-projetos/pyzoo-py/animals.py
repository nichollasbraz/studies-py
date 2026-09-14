from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, animalId, animalName, animalSpecie, animalAge):
        self._animalId = animalId
        self._animalName = animalName
        self._animalSpecie = animalSpecie
        self._animalAge = animalAge


    @abstractmethod
    def feed(self, food):
        pass


    @abstractmethod
    def treat(self):
        pass


    def getAnimalId(self):
        return self._animalId


    def getAnimalName(self):
        return self._animalName


    def getAnimalSpecie(self):
        return self._animalSpecie


    def getAnimalAge(self):
        return self._animalAge


    def setAnimalAge(self, newAge):
        self._animalAge = newAge


class Lion(Animal):

    def __init__(self, animalId, animalName, animalSpecie, animalAge):
        super().__init__(animalId, animalName, animalSpecie, animalAge)
        self._food = ['beef', 'horse meat', 'chicken']


    def feed(self, food):
        lwrFood = food.lower()  

        if lwrFood not in self._food:
            raise ValueError(f"{lwrFood} is not appropriate for a lion.")
        
        return True


    def treat(self):
        return "general treatment performed on the lion."


    def getAllowedFoods(self):
        return self._food


class Elephant(Animal):

    def __init__(self, animalId, animalName, animalSpecie, animalAge):
        super().__init__(animalId, animalName, animalSpecie, animalAge)
        self._food = ['grass', 'leaves', 'fruits', 'vegetables']


    def feed(self, food):
        lwrFood = food.lower()

        if lwrFood not in self._food:
            raise ValueError(f"{lwrFood} is not appropriate for an elephant.")
        
        return True


    def treat(self):
        return "trunk massage performed on the elephant."


    def getAllowedFoods(self):
        return self._food


class Monkey(Animal):

    def __init__(self, animalId, animalName, animalSpecie, animalAge):
        super().__init__(animalId, animalName, animalSpecie, animalAge)
        self._food = ['banana', 'fruits', 'nuts', 'insects']


    def feed(self, food):
        lwrFood = food.lower()

        if lwrFood not in self._food:
            raise ValueError(f"{lwrFood} is not appropriate for a monkey.")
        
        return True


    def treat(self):
        return "enrichment toys provided to the monkey."


    def getAllowedFoods(self):
        return self._food


class Giraffe(Animal):

    def __init__(self, animalId, animalName, animalSpecie, animalAge):
        super().__init__(animalId, animalName, animalSpecie, animalAge)
        self._food = ['leaves', 'tree branches', 'fruits']


    def feed(self, food):
        lwrFood = food.lower()

        if lwrFood not in self._food:
            raise ValueError(f"{lwrFood} is not appropriate for a giraffe.")
        
        return True


    def treat(self):
        return "neck care performed on the giraffe."


    def getAllowedFoods(self):
        return self._food


class Penguin(Animal):

    def __init__(self, animalId, animalName, animalSpecie, animalAge):
        super().__init__(animalId, animalName, animalSpecie, animalAge)
        self._food = ['fish', 'krill', 'squid']


    def feed(self, food):
        lwrFood = food.lower()

        if lwrFood not in self._food:
            raise ValueError(f"{lwrFood} is not appropriate for a penguin.")
        
        return True


    def treat(self):
        return "water bath performed on the penguin."


    def getAllowedFoods(self):
        return self._food


animals_dict = {}


def registerAnimal(animal):
    if animal.getAnimalId() in animals_dict:
        return False
    animals_dict[animal.getAnimalId()] = animal
    return True


def deleteAnimal(animalId):
    if animalId not in animals_dict:
        return False
    del animals_dict[animalId]
    return True


def getAnimal(animalId):
    return animals_dict.get(animalId, None)


def listAllAnimals():
    return animals_dict


def isAnimalIdAvailable(animalId):
    return animalId not in animals_dict
