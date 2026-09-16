from abc import ABC, abstractmethod


class Enclosure(ABC):

    def __init__(self, enclosureId, enclosureName, enclosureType, capacity):
        self._enclosureId = enclosureId
        self._enclosureName = enclosureName
        self._enclosureType = enclosureType
        self._capacity = capacity
        self._animals = {}


    @abstractmethod
    def isAnimalCompatible(self, animal):
        pass


    def getEnclosureId(self):
        return self._enclosureId


    def getEnclosureName(self):
        return self._enclosureName


    def getEnclosureType(self):
        return self._enclosureType


    def getCapacity(self):
        return self._capacity


    def getCurrentOccupancy(self):
        return len(self._animals)


    def addAnimal(self, animal):
        if not self.isAnimalCompatible(animal):
            return False, f"{animal.getAnimalSpecie()} is not compatible with this enclosure."
        
        if self.getCurrentOccupancy() >= self._capacity:
            return False, "Enclosure is at full capacity."
        
        self._animals[animal.getAnimalId()] = animal
        return True, f"{animal.getAnimalName()} added to {self._enclosureName}."


    def removeAnimal(self, animalId):
        if animalId not in self._animals:
            return False, "Animal not found in this enclosure."
        
        del self._animals[animalId]
        return True, "Animal removed from enclosure."


    def getAnimals(self):
        return list(self._animals.values())


    def getAnimalsDict(self):
        return self._animals


class SavannhaEnclosure(Enclosure):

    def __init__(self, enclosureId, enclosureName, capacity):
        super().__init__(enclosureId, enclosureName, "Savanna", capacity)


    def isAnimalCompatible(self, animal):
        compatible_species = ['Lion', 'Giraffe']
        return animal.getAnimalSpecie() in compatible_species


class ForestEnclosure(Enclosure):

    def __init__(self, enclosureId, enclosureName, capacity):
        super().__init__(enclosureId, enclosureName, "Forest", capacity)


    def isAnimalCompatible(self, animal):
        compatible_species = ['Monkey', 'Elephant']
        return animal.getAnimalSpecie() in compatible_species


class AquaticEnclosure(Enclosure):

    def __init__(self, enclosureId, enclosureName, capacity):
        super().__init__(enclosureId, enclosureName, "Aquatic", capacity)


    def isAnimalCompatible(self, animal):
        compatible_species = ['Penguin']
        return animal.getAnimalSpecie() in compatible_species


enclosures_dict = {}


def registerEnclosure(enclosure):
    if enclosure.getEnclosureId() in enclosures_dict:
        return False
    enclosures_dict[enclosure.getEnclosureId()] = enclosure
    return True


def deleteEnclosure(enclosureId):
    if enclosureId not in enclosures_dict:
        return False
    
    enclosure = enclosures_dict[enclosureId]
    if enclosure.getCurrentOccupancy() > 0:
        return False  # Não pode deletar recinto com animais
    
    del enclosures_dict[enclosureId]
    return True


def getEnclosure(enclosureId):
    return enclosures_dict.get(enclosureId, None)


def listAllEnclosures():
    return enclosures_dict


def isEnclosureIdAvailable(enclosureId):
    return enclosureId not in enclosures_dict
