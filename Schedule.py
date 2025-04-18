from Person import Person
import random


counter = 0


class Schedule:
    def __init__(self):
        """
        DayOfWeek = (morning shift shift count, night shfit count)
        """
        self.mondayCount = (2, 4)
        self.tuesdayCount = (2, 4)
        self.wednesdayCount = (2, 4)
        self.thursdayCount = (2, 5)
        self.fridayCount = (4, 5)
        self.saturdayCount = (4, 6)
        self.sundayCount = (4, 5)

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
        Fills the schedule using an optimized backtracking algorithm that:
        - Randomizes employee order to yield a new schedule on each run.
        - Enforces that an employee cannot be assigned to more than one shift per day.
        - Ensures each completed shift has at least one employee with soup.
        Returns True if a complete valid schedule is found, otherwise False.
        """

        # --- Upfront Feasibility Check ---
        total_slots = sum(day_req + night_req for (day_req, night_req)
                          in self.shift_requirements.values())
        total_capacity = sum(emp.maxShift for emp in employees)
        if total_capacity < total_slots:
            print("Overall, there are not enough shifts available among all employees!")
            return False

        # --- Create a List of All Shift Slots ---
        days_in_order = ["Monday", "Tuesday", "Wednesday",
                         "Thursday", "Friday", "Saturday", "Sunday"]
        all_slots = []
        for day in days_in_order:
            day_req, night_req = self.shift_requirements[day]
            all_slots.extend([(day, "day_shift")] * day_req)
            all_slots.extend([(day, "night_shift")] * night_req)

        # --- Track Remaining Shifts for Each Employee ---
        employee_shifts_left = {emp: emp.maxShift for emp in employees}

        # Used to cache states we've seen: maps state -> bool (True=success, False=failure)
        memo = {}

        def can_assign(emp, day_name, shift_type) -> bool:
            # Check that the employee has remaining capacity.
            if employee_shifts_left[emp] <= 0:
                return False
            # Prevent assigning an employee to more than one shift in the same day.
            if emp in self.schedule[day_name]["day_shift"] or emp in self.schedule[day_name]["night_shift"]:
                return False
            # Check employee availability.
            day_avail, night_avail = emp.availability[day_name]
            if shift_type == "day_shift" and not day_avail:
                return False
            if shift_type == "night_shift" and not night_avail:
                return False
            return True

        # Randomize employees list for variability.
        local_employees = employees[:]
        random.shuffle(local_employees)

        def backtrack(i: int) -> bool:
            # If we've assigned everyone successfully, return True.
            if i == len(all_slots):
                return True

            # Create a key representing the current state for memoization.
            # (We sort by id(emp) to avoid "random" dictionary order issues.)
            state_key = (
                i,
                tuple(
                    sorted((id(emp), employee_shifts_left[emp]) for emp in employee_shifts_left))
            )

            # If we've already explored this state, return its result.
            if state_key in memo:
                return memo[state_key]

            # Prune if remaining capacity is insufficient.
            if sum(employee_shifts_left.values()) < (len(all_slots) - i):
                memo[state_key] = False
                return False

            # --- MRV Heuristic: Select the slot with the fewest candidate employees ---
            min_options = None
            min_index = i
            for j in range(i, len(all_slots)):
                day_name_j, shift_type_j = all_slots[j]
                options = [emp for emp in local_employees if can_assign(
                    emp, day_name_j, shift_type_j)]
                # Update our best slot if we find a slot with fewer valid employees
                if min_options is None or len(options) < len(min_options):
                    min_options = options
                    min_index = j
                # If zero candidates for this slot, we can fail immediately
                if len(options) == 0:
                    memo[state_key] = False
                    return False

            # Swap the most constrained slot into the current position i
            all_slots[i], all_slots[min_index] = all_slots[min_index], all_slots[i]
            day_name, shift_type = all_slots[i]

            # Randomize candidate order for further variability.
            random.shuffle(min_options)
            for emp in min_options:
                # Assign this employee to the current slot
                self.schedule[day_name][shift_type].append(emp)
                employee_shifts_left[emp] -= 1

                # If this slot (day/night) is now fully assigned, check for at least one soup
                req_needed = self.shift_requirements[day_name][
                    0] if shift_type == "day_shift" else self.shift_requirements[day_name][1]
                if len(self.schedule[day_name][shift_type]) == req_needed:
                    # If no soup in this group, revert and continue
                    if not any(e.getIsSoup() for e in self.schedule[day_name][shift_type]):
                        self.schedule[day_name][shift_type].pop()
                        employee_shifts_left[emp] += 1
                        continue

                # Recur for the next slot
                if backtrack(i + 1):
                    memo[state_key] = True
                    return True

                # Backtrack / Undo the assignment
                self.schedule[day_name][shift_type].pop()
                employee_shifts_left[emp] += 1

            # If no candidate led to a solution, record failure for this state
            memo[state_key] = False
            return False

        # Run backtracking
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
        employee_shift_counts = {
            employee: employee.maxShift for employee in employees}

        for day, shifts in self.schedule.items():
            day_required, night_required = self.shift_requirements[day]

            # Shuffle employees to randomize order for fairness
            available_employees = employees[:]

            # Fill day_shift
            random.shuffle(available_employees)
            for employee in available_employees:
                if len(shifts["day_shift"]) < day_required:
                    if (
                        # available for day shift
                        employee.availability[day][0]
                        and employee_shift_counts[employee] > 0
                    ):
                        shifts["day_shift"].append(employee)
                        employee_shift_counts[employee] -= 1

            # Shuffle again for night shift
            random.shuffle(available_employees)
            for employee in available_employees:
                if len(shifts["night_shift"]) < night_required:
                    if (
                        # available for night shift
                        employee.availability[day][1]
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
        employee_shift_counts = {
            employee: employee.maxShift for employee in employees}

        for day, shifts in self.schedule.items():
            day_required, night_required = self.shift_requirements[day]

            # Shuffle employees to randomize order for fairness
            available_employees = employees[:]

            # Fill day_shift
            random.shuffle(available_employees)
            for employee in available_employees:
                # Check if we need more for the day shift
                if len(shifts["day_shift"]) < day_required:
                    if (
                        # Check if available for day_shift
                        employee.availability[day][0]
                        # Ensure they have shifts left
                        and employee_shift_counts[employee] > 0
                    ):
                        shifts["day_shift"].append(employee)
                        employee_shift_counts[employee] -= 1

            # Shuffle again for night shift
            random.shuffle(available_employees)
            for employee in available_employees:
                # Check if we need more for the night shift
                if len(shifts["night_shift"]) < night_required:
                    if (
                        # Check if available for night_shift
                        employee.availability[day][1]
                        # Ensure they have shifts left
                        and employee_shift_counts[employee] > 0
                        # Ensure they are not already in day_shift
                        and employee not in shifts["day_shift"]
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
            employees_sorted = sorted(
                employees, key=lambda e: e.maxShift, reverse=True)

            # Fill day_shift
            for employee in employees_sorted:
                # Check if we need more for the day shift
                if len(shifts["day_shift"]) < day_required:
                    if (
                        # Check if available for day_shift
                        employee.availability[day][0]
                        and employee.maxShift > 0     # Ensure they have shifts left
                    ):
                        shifts["day_shift"].append(employee)
                        employee.maxShift -= 1

            # Fill night_shift
            for employee in employees_sorted:
                # Check if we need more for the night shift
                if len(shifts["night_shift"]) < night_required:
                    if (
                        # Check if available for night_shift
                        employee.availability[day][1]
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
