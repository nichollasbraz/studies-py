from abc import ABC, abstractmethod
from datetime import datetime


class Employee(ABC):

    def __init__(self, employeeId, employeeName, employeeRole):
        self._employeeId = employeeId
        self._employeeName = employeeName
        self._employeeRole = employeeRole
        self._activities = []


    @abstractmethod
    def work(self):
        pass


    @abstractmethod
    def registerEmployee(self):
        pass


    @abstractmethod
    def deleteEmployee(self):
        pass


    def logActivity(self, activity):
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self._activities.append({
            'activity': activity,
            'timestamp': timestamp
        })


    def getActivities(self):
        return self._activities


    def getEmployeeId(self):
        return self._employeeId


    def getEmployeeName(self):
        return self._employeeName


    def getEmployeeRole(self):
        return self._employeeRole


class Zookeeper(Employee):

    def __init__(self, employeeId, employeeName):
        super().__init__(employeeId, employeeName, "Zookeeper")
        self._animalsCaredFor = []


    def registerEmployee(self):
        if self._employeeId in employees_dict:
            return False
        
        employees_dict[self._employeeId] = {
            'name': self._employeeName,
            'role': self._employeeRole,
            'object': self
        }
        self.logActivity("Registered as Zookeeper.")
        return True


    def deleteEmployee(self):
        if self._employeeId not in employees_dict:
            return False
        
        del employees_dict[self._employeeId]
        return True


    def feedAnimal(self, animal, food):
        try:
            animal.feed(food)
            activity = f"Fed {animal.getAnimalName()} ({animal.getAnimalSpecie()}) with {food}."
            self.logActivity(activity)
            self._animalsCaredFor.append(animal.getAnimalName())
            return True, f"{animal.getAnimalName()} was fed with {food}."
        except ValueError as e:
            self.logActivity(f"Failed to feed {animal.getAnimalName()} with {food}.")
            return False, str(e)


    def treatAnimal(self, animal):
        message = animal.treat()
        activity = f"Treated {animal.getAnimalName()} ({animal.getAnimalSpecie()})."
        self.logActivity(activity)
        self._animalsCaredFor.append(animal.getAnimalName())
        return True, message


    def cleanEnclosure(self, enclosureName):
        activity = f"Cleaned enclosure {enclosureName}."
        self.logActivity(activity)
        return True, f"Enclosure {enclosureName} was cleaned."


    def getAnimalsCaredFor(self):
        return list(set(self._animalsCaredFor))


    def work(self):
        return f"{self._employeeName} is working as a {self._employeeRole}."


class Veterinarian(Employee):

    def __init__(self, employeeId, employeeName):
        super().__init__(employeeId, employeeName, "Veterinarian")
        self._specialties = []


    def registerEmployee(self):
        if self._employeeId in employees_dict:
            return False
        
        employees_dict[self._employeeId] = {
            'name': self._employeeName,
            'role': self._employeeRole,
            'object': self
        }
        self.logActivity("Registered as Veterinarian.")
        return True


    def deleteEmployee(self):
        if self._employeeId not in employees_dict:
            return False
        
        del employees_dict[self._employeeId]
        return True


    def checkUpAnimal(self, animal):
        activity = f"Performed checkup on {animal.getAnimalName()} ({animal.getAnimalSpecie()})."
        self.logActivity(activity)
        return True, f"Checkup performed on {animal.getAnimalName()}."


    def prescribeMedicine(self, animal, medicine):
        activity = f"Prescribed {medicine} for {animal.getAnimalName()}."
        self.logActivity(activity)
        return True, f"{medicine} prescribed for {animal.getAnimalName()}."


    def addSpecialty(self, specialty):
        if specialty not in self._specialties:
            self._specialties.append(specialty)
            return True, f"Specialty {specialty} added."
        return False, f"Specialty {specialty} already exists."


    def getSpecialties(self):
        return self._specialties


    def work(self):
        return f"{self._employeeName} is working as a {self._employeeRole}."


employees_dict = {}


def listAllEmployees():
    return employees_dict


def getEmployeeById(employeeId):
    return employees_dict.get(employeeId, None)


def isEmployeeIdAvailable(employeeId):
    return employeeId not in employees_dict
