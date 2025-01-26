from Person import Person


class Schedule:
    def __init__(self):
        """
        DayOfWeek = (morning shift shift count, night shfit count)
        """
        self.mondayCount = (2,4)
        self.tuesdayCount = (2,4)
        self.wednesdayCount = (2,4)
        self.thursdayCount = (2,4)
        self.fridayCount = (4,5)
        self.saturdayCount = (4,5)
        self.sundayCount = (4, 4)

        self.schedule = {Monday: {day_shift:"", nighy_shift: ""}, Tuesday: {day_shift:"", nighy_shift: ""}, 
        Wednesday: {day_shift:"", nighy_shift: ""}, Thursday: {day_shift:"", nighy_shift: ""}, 
        Friday: {day_shift:"", nighy_shift: ""},
        Saturday: {day_shift:"", nighy_shift: ""}, Sunday: {day_shift:"", nighy_shift: ""}}

    def setShift(self, shift: str, employee: Person):

        pass

    def doesShiftHaveSoup(self, day):

    def getShift(self, shift: str):
        pass
        


