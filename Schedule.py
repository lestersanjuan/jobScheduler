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
    def fillShiftsBacktracking(self, employees: list[Person]) -> bool:
        """
        Attempt to fill all day_shift and night_shift slots for each day using backtracking.
        Returns True if successful, or False if it is impossible given constraints:
            - Employee availability
            - Employee maxShift
            - Cannot assign same person to the same shift more than once
            - (Optional) Cannot assign same person to day+night on the same day (if desired)
        """

        # 1) Create an ordered list of all "shift slots" we must fill.
        #    For example, if Monday requires 2 day and 4 night => 6 slots for Monday.
        days_in_order = [
            "Monday", "Tuesday", "Wednesday", "Thursday", 
            "Friday", "Saturday", "Sunday"
        ]
        all_slots = []
        for day_name in days_in_order:
            day_req, night_req = self.shift_requirements[day_name]
            for _ in range(day_req):
                all_slots.append((day_name, "day_shift"))
            for _ in range(night_req):
                all_slots.append((day_name, "night_shift"))

        # 2) Track how many shifts each employee can still work (their maxShift).
        employee_shifts_left = {emp: emp.maxShift for emp in employees}

        # 3) The recursive backtracking function.
        def backtrack(i: int) -> bool:
            # If we have assigned employees for all slots, we're done.
            if i == len(all_slots):
                return True

            day_name, shift_type = all_slots[i]

            # Try each employee for slot i.
            for emp in employees:
                if self.can_assign(emp, day_name, shift_type, employee_shifts_left):
                    # Assign employee to this slot
                    self.schedule[day_name][shift_type].append(emp)
                    employee_shifts_left[emp] -= 1

                    # Move on to the next slot
                    if backtrack(i + 1):
                        return True

                    # Backtrack: undo the assignment if it didn't lead to a solution
                    self.schedule[day_name][shift_type].pop()
                    employee_shifts_left[emp] += 1

            # No valid assignment for slot i => fail
            return False

        # 4) Start backtracking from the first slot
        success = backtrack(0)
        if success:
            print("Successfully filled all required shifts using backtracking!")
        else:
            print("Could NOT fill all shifts with the given constraints.")
        return success

    def can_assign(
        self, 
        emp: Person, 
        day_name: str, 
        shift_type: str, 
        shifts_left: dict
    ) -> bool:
        """
        Checks whether 'emp' can be assigned to (day_name, shift_type) given:
          - Enough shifts left (maxShift not exceeded).
          - The person is not already in that shift on that day.
          - Availability for day/night.
          - (Optional) If you want to forbid day+night on same day for one person.
        """
        # 1) Check the employee still has capacity to work.
        if shifts_left[emp] <= 0:
            return False

        # 2) Check that employee is not already assigned to this exact shift.
        if emp in self.schedule[day_name][shift_type]:
            return False

        # 3) Check their availability for this day/shift.
        day_avail, night_avail = emp.availability[day_name]
        if shift_type == "day_shift" and not day_avail:
            return False
        if shift_type == "night_shift" and not night_avail:
            return False

        # 4) (Optional) Check if you do NOT allow day+night for the same day:
        if shift_type == "night_shift":
            if emp in self.schedule[day_name]["day_shift"]:
                return False

        return True

    def fillShiftsRandomized(self, employees: list[Person]):
        """
        Randomized algorithm to fill shifts for the week.
        - Randomly selects employees to fill shifts while respecting:
            - Employee availability
            - Employee maxShift constraint
        - Ensures shifts are filled up to the required number of employees (but might not fill all).
        """
        # Track remaining shifts for each employee
        employee_shift_counts = {employee: employee.maxShift for employee in employees}

        for day, shifts in self.schedule.items():
            day_required, night_required = self.shift_requirements[day]

            # Shuffle employees to randomize order for fairness
            available_employees = employees[:]

            # Fill day_shift
            random.shuffle(available_employees)
            for employee in available_employees:
                if len(shifts["day_shift"]) < day_required:
                    if (
                        employee.availability[day][0]  # available for day shift
                        and employee_shift_counts[employee] > 0
                    ):
                        shifts["day_shift"].append(employee)
                        employee_shift_counts[employee] -= 1

            # Shuffle again for night shift
            random.shuffle(available_employees)
            for employee in available_employees:
                if len(shifts["night_shift"]) < night_required:
                    if (
                        employee.availability[day][1]  # available for night shift
                        and employee_shift_counts[employee] > 0
                        and employee not in shifts["day_shift"]
                    ):
                        shifts["night_shift"].append(employee)
                        employee_shift_counts[employee] -= 1

            # Check for unfilled shifts
            if len(shifts["day_shift"]) < day_required:
                print(f"WARNING: Not enough employees for {day} day shift.")
            if len(shifts["night_shift"]) < night_required:
                print(f"WARNING: Not enough employees for {day} night shift.")
    def fillShiftsRandomized(self, employees: list[Person]):
        """
        Randomized algorithm to fill shifts for the week.
        - Randomly selects employees to fill shifts while respecting:
            - Employee availability
            - Employee maxShift constraint
        - Ensures shifts are filled up to the required number of employees.
        """
        # Track remaining shifts for each employee
        employee_shift_counts = {employee: employee.maxShift for employee in employees}

        for day, shifts in self.schedule.items():
            day_required, night_required = self.shift_requirements[day]

            # Shuffle employees to randomize order for fairness
            available_employees = employees[:]

            # Fill day_shift
            random.shuffle(available_employees)
            for employee in available_employees:
                if len(shifts["day_shift"]) < day_required:  # Check if we need more for the day shift
                    if (
                        employee.availability[day][0]  # Check if available for day_shift
                        and employee_shift_counts[employee] > 0  # Ensure they have shifts left
                    ):
                        shifts["day_shift"].append(employee)
                        employee_shift_counts[employee] -= 1

            # Shuffle again for night shift
            random.shuffle(available_employees)
            for employee in available_employees:
                if len(shifts["night_shift"]) < night_required:  # Check if we need more for the night shift
                    if (
                        employee.availability[day][1]  # Check if available for night_shift
                        and employee_shift_counts[employee] > 0  # Ensure they have shifts left
                        and employee not in shifts["day_shift"]  # Ensure they are not already in day_shift
                    ):
                        shifts["night_shift"].append(employee)
                        employee_shift_counts[employee] -= 1

            # Check for unfilled shifts and print warnings
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
        """Checks if any employee scheduled on the given day has soup."""
        for shift in self.schedule[day]:  # shift is either "day_shift" or "night_shift"
            for emp in self.schedule[day][shift]:
                if emp.getIsSoup():
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
        


