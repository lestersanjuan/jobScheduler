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
            - Cannot assign the same person to the same shift more than once
            - (Optional) Cannot assign the same person to both day and night on the same day
        """
        # --- Upfront Feasibility Check ---
        # Calculate total required slots for the week.
        total_slots = sum(day_req + night_req for (day_req, night_req) in self.shift_requirements.values())
        # Calculate the total capacity of all employees.
        total_capacity = sum(emp.maxShift for emp in employees)
        if total_capacity < total_slots:
            print("Overall, there are not enough shifts available among all employees!")
            return False

        # --- Create an Ordered List of Shift Slots ---
        days_in_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        all_slots = []
        for day in days_in_order:
            day_req, night_req = self.shift_requirements[day]
            all_slots.extend([(day, "day_shift")] * day_req)
            all_slots.extend([(day, "night_shift")] * night_req)

        # --- Track the Remaining Shifts for Each Employee ---
        employee_shifts_left = {emp: emp.maxShift for emp in employees}

        # --- Inline can_assign Function ---
        def can_assign(emp, day_name, shift_type) -> bool:
            # 1) Check that the employee has capacity left.
            if employee_shifts_left[emp] <= 0:
                return False
            # 2) Ensure the employee isn't already assigned to this shift.
            if emp in self.schedule[day_name][shift_type]:
                return False
            # 3) Check employee availability for the given shift.
            day_avail, night_avail = emp.availability[day_name]
            if shift_type == "day_shift" and not day_avail:
                return False
            if shift_type == "night_shift" and not night_avail:
                return False
            # 4) (Optional) Prevent assigning the same employee to both shifts on the same day.
            if shift_type == "night_shift" and emp in self.schedule[day_name]["day_shift"]:
                return False
            return True

        # --- Recursive Backtracking Function ---
        def backtrack(i: int) -> bool:
            # Prune if the total remaining capacity is less than the slots left.
            if sum(employee_shifts_left.values()) < (len(all_slots) - i):
                return False

            # Base case: all slots have been filled.
            if i == len(all_slots):
                return True

            day_name, shift_type = all_slots[i]

            # Try assigning each employee to the current slot.
            for emp in employees:
                if can_assign(emp, day_name, shift_type):
                    # Assign the employee.
                    self.schedule[day_name][shift_type].append(emp)
                    employee_shifts_left[emp] -= 1

                    # Recurse to fill the next slot.
                    if backtrack(i + 1):
                        return True

                    # Backtrack: undo the assignment.
                    self.schedule[day_name][shift_type].pop()
                    employee_shifts_left[emp] += 1

            # No valid assignment was found for this slot.
            return False

        # --- Start the Backtracking Process ---
        success = backtrack(0)
        if success:
            print("Successfully filled all required shifts using backtracking!")
        else:
            print("Could NOT fill all shifts with the given constraints.")
        return success
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
        


