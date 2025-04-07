from Schedule import Schedule
from Person import Person

if __name__ == "__main__":
    # Create test employees
    employees = [
        Person(Name="Andrea", availability={"Monday": "X", "Tuesday": "C", "Wednesday": "C", "Thursday": "X",
               "Friday": "C", "Saturday": "X", "Sunday": "X"}, isSoup=True, maxShift=4, minShift=1),

        Person(Name="Andrew", availability={"Monday": "X", "Tuesday": "C", "Wednesday": "X", "Thursday": "C",
               "Friday": "O", "Saturday": "O", "Sunday": "O"}, isSoup=True, maxShift=3, minShift=1),

        Person(Name="Athena", availability={"Monday": "X", "Tuesday": "X", "Wednesday": "X", "Thursday": "C",
               "Friday": "O", "Saturday": "O", "Sunday": "X"}, isSoup=True, maxShift=3, minShift=2),

        Person(Name="Chester", availability={"Monday": "O", "Tuesday": "O", "Wednesday": "O", "Thursday": "O",
               "Friday": "O", "Saturday": "X", "Sunday": "X"}, isSoup=True, maxShift=3, minShift=3),

        Person(Name="Dan", availability={"Monday": "O", "Tuesday": "C", "Wednesday": "C", "Thursday": "X",
               "Friday": "O", "Saturday": "O", "Sunday": "X"}, isSoup=True, maxShift=3, minShift=1),

        Person(Name="Destiny", availability={"Monday": "X", "Tuesday": "O", "Wednesday": "X", "Thursday": "O",
               "Friday": "O", "Saturday": "O", "Sunday": "X"}, isSoup=False, maxShift=2, minShift=1),

        Person(Name="Donny", availability={"Monday": "C", "Tuesday": "C", "Wednesday": "X", "Thursday": "X",
               "Friday": "X", "Saturday": "X", "Sunday": "X"}, isSoup=False, maxShift=2, minShift=0),

        Person(Name="Imogene", availability={"Monday": "C", "Tuesday": "O", "Wednesday": "C", "Thursday": "O",
               "Friday": "O", "Saturday": "O", "Sunday": "C"}, isSoup=False, maxShift=5, minShift=2),

        Person(Name="Jacob", availability={"Monday": "O", "Tuesday": "C", "Wednesday": "X", "Thursday": "X",
               "Friday": "X", "Saturday": "X", "Sunday": "O"}, isSoup=True, maxShift=3, minShift=1),

        Person(Name="Ivan", availability={"Monday": "X", "Tuesday": "X", "Wednesday": "X", "Thursday": "O",
               "Friday": "O", "Saturday": "X", "Sunday": "C"}, isSoup=True, maxShift=2, minShift=0),

        Person(Name="Jojo", availability={"Monday": "X", "Tuesday": "C", "Wednesday": "X", "Thursday": "C",
               "Friday": "X", "Saturday": "X", "Sunday": "X"}, isSoup=False, maxShift=2, minShift=0),

        Person(Name="Josh", availability={"Monday": "O", "Tuesday": "O", "Wednesday": "O", "Thursday": "O",
               "Friday": "O", "Saturday": "O", "Sunday": "O"}, isSoup=False, maxShift=4, minShift=0),

        Person(Name="Karen", availability={"Monday": "C", "Tuesday": "C", "Wednesday": "C", "Thursday": "C",
               "Friday": "C", "Saturday": "O", "Sunday": "O"}, isSoup=True, maxShift=4, minShift=0),

        Person(Name="Kayla", availability={"Monday": "X", "Tuesday": "C", "Wednesday": "X", "Thursday": "O",
               "Friday": "X", "Saturday": "X", "Sunday": "X"}, isSoup=True, maxShift=3, minShift=1),

        Person(Name="Lester", availability={"Monday": "X", "Tuesday": "O", "Wednesday": "C", "Thursday": "O",
               "Friday": "O", "Saturday": "O", "Sunday": "O"}, isSoup=True, maxShift=3, minShift=2),

        Person(Name="Luan", availability={"Monday": "O", "Tuesday": "O", "Wednesday": "O", "Thursday": "O",
               "Friday": "C", "Saturday": "O", "Sunday": "C"}, isSoup=False, maxShift=3, minShift=3),

        Person(Name="Maddie", availability={"Monday": "X", "Tuesday": "X", "Wednesday": "X", "Thursday": "X",
               "Friday": "X", "Saturday": "O", "Sunday": "O"}, isSoup=False, maxShift=2, minShift=0),

        Person(Name="Raj", availability={"Monday": "O", "Tuesday": "X", "Wednesday": "X", "Thursday": "X",
               "Friday": "X", "Saturday": "X", "Sunday": "X"}, isSoup=False, maxShift=4, minShift=1),

        Person(Name="Richard", availability={"Monday": "X", "Tuesday": "X", "Wednesday": "X", "Thursday": "X",
               "Friday": "O", "Saturday": "X", "Sunday": "X"}, isSoup=False, maxShift=1, minShift=0),

        Person(Name="Shawn", availability={"Monday": "C", "Tuesday": "C", "Wednesday": "C", "Thursday": "C",
               "Friday": "O", "Saturday": "O", "Sunday": "X"}, isSoup=False, maxShift=4, minShift=2),

        Person(Name="Tammy", availability={"Monday": "X", "Tuesday": "X", "Wednesday": "X", "Thursday": "X",
               "Friday": "X", "Saturday": "X", "Sunday": "O"}, isSoup=True, maxShift=2, minShift=0),

        Person(Name="Tayvia", availability={"Monday": "X", "Tuesday": "C", "Wednesday": "X", "Thursday": "X",
               "Friday": "C", "Saturday": "O", "Sunday": "O"}, isSoup=False, maxShift=2, minShift=1),

        Person(Name="Tiffany", availability={"Monday": "C", "Tuesday": "C", "Wednesday": "X", "Thursday": "X",
               "Friday": "X", "Saturday": "X", "Sunday": "O"}, isSoup=False, maxShift=2, minShift=0),
    ]

    # Create a schedule and populate it
    schedule = Schedule()
    schedule.fillShiftsBacktracking(employees)
    # Print the filled schedule
    print(schedule)
