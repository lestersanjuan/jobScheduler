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

    self.shift_requirements = {
            "Monday": self.mondayCount,
            "Tuesday": self.tuesdayCount,
            "Wednesday": self.wednesdayCount,
            "Thursday": self.thursdayCount,
            "Friday": self.fridayCount,
            "Saturday": self.saturdayCount,
            "Sunday": self.sundayCount,
        }

    def fillShifts(self, employees: list[Person]):
        """
        Greedy algorithm to fill shifts for the week.
        - Tries to assign employees to shifts while respecting availability and maxShift constraints.
        - Ensures shifts are filled up to the required number of employees.
        """
        for day, shifts in self.schedule.items():
            day_required, night_required = self.shift_requirements[day]

            # Fill day_shift
            for employee in employees:
                if len(shifts["day_shift"]) < day_required:  # Check if we need more for the day shift
                    if (
                        employee.availability[day][0]  # Check if available for day_shift
                        and employee.maxShift > 0     # Ensure they have shifts left
                    ):
                        shifts["day_shift"].append(employee)
                        employee.maxShift -= 1

            # Fill night_shift
            for employee in employees:
                if len(shifts["night_shift"]) < night_required:  # Check if we need more for the night shift
                    if (
                        employee.availability[day][1]  # Check if available for night_shift
                        and employee.maxShift > 0     # Ensure they have shifts left
                    ):
                        shifts["night_shift"].append(employee)
                        employee.maxShift -= 1
    

    def doesShiftHaveSoup(self, day): -> bool
        """Checks for if the shift has Soup"""
        for shift in self.schedule[day]: #check for day_shift, and night_shift
            for people in self.schedule[day][shift]: #check for each person in day/night shfit
                if self.schedule[day][shift][people].getIsSoup():
                    return True

        return False
    
    def getShift(self, shift: str):
        pass
        


