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

        self.schedule = {Monday: {day_shift:[], night_shift: []}, Tuesday: {day_shift:[], night_shift: []}, 
        Wednesday: {day_shift:[], night_shift: []}, Thursday: {day_shift:[], night_shift: []}, 
        Friday: {day_shift:[], night_shift: []},
        Saturday: {day_shift:[], night_shift: []}, Sunday: {day_shift:[], night_shift: []}}

    def setShift(self, shift: str, employee: Person): -> None #Leave for future implementation
        pass


    def fillShifts(self):
        pass
        
    def doesShiftHaveSoup(self, day): -> bool
        """Checks for if the shift has Soup"""
        for shift in self.schedule[day]: #check for day_shift, and night_shift
            for people in self.schedule[day][shift]: #check for each person in day/night shfit
                if self.schedule[day][shift][people].getIsSoup():
                    return True

        return False
    
    def getShift(self, shift: str):
        pass
        


