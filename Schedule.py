from Person import Person
import random
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

        self.schedule = {
                            "Monday": {"day_shift": [], "night_shift": []},
                            "Tuesday": {"day_shift": [], "night_shift": []},
                            "Wednesday": {"day_shift": [], "night_shift": []},
                            "Thursday": {"day_shift": [], "night_shift": []},
                            "Friday": {"day_shift": [], "night_shift": []},
                            "Saturday": {"day_shift": [], "night_shift": []},
                            "Sunday": {"day_shift": [], "night_shift": []},
                        }


        self.shift_requirements = {
                "Monday": self.mondayCount,
                "Tuesday": self.tuesdayCount,
                "Wednesday": self.wednesdayCount,
                "Thursday": self.thursdayCount,
                "Friday": self.fridayCount,
                "Saturday": self.saturdayCount,
                "Sunday": self.sundayCount,
            }
    def fillShiftsRandomized(self, employees: list[Person]):
        """
        Randomized algorithm to fill shifts for the week.
        - Randomly selects employees to fill shifts while respecting:
            - Employee availability
            - Employee maxShift constraint
        - Ensures shifts are filled up to the required number of employees.
        """
        for day, shifts in self.schedule.items():
            day_required, night_required = self.shift_requirements[day]

            # Shuffle the employee list to randomize order
            random.shuffle(employees)

            # Fill day_shift
            for employee in employees:
                if len(shifts["day_shift"]) < day_required:  # Check if we need more for the day shift
                    if (
                        employee.availability[day][0]  # Check if available for day_shift
                        and employee.maxShift > 0     # Ensure they have shifts left
                    ):
                        shifts["day_shift"].append(employee)
                        employee.maxShift -= 1

            # Shuffle again for night shift to ensure fairness
            random.shuffle(employees)

            # Fill night_shift
            for employee in employees:
                if len(shifts["night_shift"]) < night_required:  # Check if we need more for the night shift
                    if (
                        employee.availability[day][1]  # Check if available for night_shift
                        and employee.maxShift > 0     # Ensure they have shifts left
                        and employee not in shifts["day_shift"]
                    ):
                        shifts["night_shift"].append(employee)
                        employee.maxShift -= 1

        
        
            # If not enough employees are assigned to the shifts, print a warning
            if len(shifts["day_shift"]) < day_required:
                print(f"WARNING: Not enough employees for {day} day shift.")
            if len(shifts["night_shift"]) < night_required:
                print(f"WARNING: Not enough employees for {day} night shift.")

    def fillShiftsGreedy(self, employees: list[Person]):
        """
        Greedy algorithm to fill shifts for the week.
        - Fills all shifts in the schedule while respecting:
            - Employee availability
            - Employee maxShift constraint
        - Ensures shifts are filled up to the required number of employees.
        """

        
        for day, shifts in self.schedule.items():
            day_required, night_required = self.shift_requirements[day]

            # Sort employees by maxShift (prioritize employees with higher maxShift)
            employees_sorted = sorted(employees, key=lambda e: e.maxShift, reverse=True)
            
            # Fill day_shift
            for employee in employees_sorted:
                if len(shifts["day_shift"]) < day_required:  # Check if we need more for the day shift
                    if (
                        employee.availability[day][0]  # Check if available for day_shift
                        and employee.maxShift > 0     # Ensure they have shifts left
                    ):
                        shifts["day_shift"].append(employee)
                        employee.maxShift -= 1

            # Fill night_shift
            for employee in employees_sorted:
                if len(shifts["night_shift"]) < night_required:  # Check if we need more for the night shift
                    if (
                        employee.availability[day][1]  # Check if available for night_shift
                        and employee.maxShift > 0     # Ensure they have shifts left
                        and employee not in shifts["day_shift"]
                    ):
                        shifts["night_shift"].append(employee)
                        employee.maxShift -= 1

            # If not enough employees are assigned to the shifts, print a warning
            if len(shifts["day_shift"]) < day_required:
                print(f"WARNING: Not enough employees for {day} day shift.")
            if len(shifts["night_shift"]) < night_required:
                print(f"WARNING: Not enough employees for {day} night shift.")
    

    def doesShiftHaveSoup(self, day): 
        """Checks for if the shift has Soup"""
        for shift in self.schedule[day]: #check for day_shift, and night_shift
            for people in self.schedule[day][shift]: #check for each person in day/night shfit
                if self.schedule[day][shift][people].getIsSoup():
                    return True

        return False
    def __repr__(self):
        """
        Represent the schedule as a table-like structure.
        """
        # Create header
        header = f"{'Day':<10} | {'Day Shift':<40} | {'Night Shift':<40}\n"
        header += "-" * 95 + "\n"

        # Add each day's shifts
        rows = []
        for day, shifts in self.schedule.items():
            day_shift = ", ".join(emp.name for emp in shifts["day_shift"])
            night_shift = ", ".join(emp.name for emp in shifts["night_shift"])
            rows.append(f"{day:<10} | {day_shift:<40} | {night_shift:<40}")

        # Combine header and rows
        return header + "\n".join(rows)


    def getShift(self, shift: str):
        pass
        


