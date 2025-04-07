class Person:
    def __init__(self, name: str, availability: dict(), isSoup: bool, maxShift: int, minShift: int):  # type: ignore
        """
        Important attribute: Availability
        Availability will be made as where {DayOfTheWeek: [day_shift, night_shift]} where day_shift/night_shift = bool
        For example: 
            Person("Lester", {Monday: [True, False], Tuesday: [False, False]..., Sunday:[True, True]}, True, 1, 2)
        """
        self.name = name
        self.availability = availability
        self.setAvailability()
        self.isSoup = isSoup
        self.maxShift = maxShift
        self.minShift = minShift

    def setShiftCount(self, amount: int):
        pass

    def setName(self, name: str):
        pass

    def setAvailability(self):
        for x in self.availability:
            if self.availability[x] == "O":
                self.availability[x] = [True, False]
            elif self.availability[x] == "C":
                self.availability[x] = [False, True]
            elif self.availability[x] == "X":
                self.availability[x] = [False, False]

    def setIsSoup(self, isSoup: bool):
        self.isSoup = isSoup

    def getName(self):
        pass

    def getAvailability(self):
        pass

    def getIsSoup(self):
        return self.isSoup
