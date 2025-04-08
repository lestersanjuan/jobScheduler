from Schedule import Schedule
from Person import Person

if __name__ == "__main__":
    # Create test employees
    employees = [
        Person(
            name="Andrea",
            availability={
                "Monday": [False, False],  # X
                "Tuesday": [True, False],
                "Wednesday": [False, True],
                "Thursday": [False, False],
                "Friday": [False, True],
                "Saturday": [False, False],
                "Sunday": [True, True],
            },
            isSoup=True,
            maxShift=4,
            minShift=1,
        ),
        Person(
            name="Andrew",
            availability={
                "Monday": [True, True],
                "Tuesday": [False, True],
                "Wednesday": [True, True],
                "Thursday": [False, True],
                "Friday": [True, True],
                "Saturday": [True, True],
                "Sunday": [False, False],  # UNAVAILABLE
            },
            isSoup=True,
            maxShift=3,
            minShift=1,
        ),
        Person(
            name="Athena",
            availability={
                "Monday": [False, False],
                "Tuesday": [True, True],
                "Wednesday": [False, False],
                "Thursday": [False, True],
                "Friday": [False, True],
                "Saturday": [True, True],
                "Sunday": [True, False],
            },
            isSoup=True,
            maxShift=3,
            minShift=1,
        ),
        Person(
            name="Chester",
            availability={
                "Monday": [True, False],
                "Tuesday": [True, False],
                "Wednesday": [True, False],
                "Thursday": [True, False],
                "Friday": [True, False],
                "Saturday": [False, False],
                "Sunday": [False, False],
            },
            isSoup=True,
            maxShift=3,
            minShift=3,
        ),
        Person(
            name="Dan",
            availability={
                "Monday": [False, False],  # UNAVAILABLE
                "Tuesday": [False, False],
                "Wednesday": [False, False],  # UNAVAILABLE
                "Thursday": [False, True],
                "Friday": [False, False],
                "Saturday": [False, False],  # UNAVAILABLE
                "Sunday": [False, False],
            },
            isSoup=True,
            maxShift=1,
            minShift=1,
        ),
        Person(
            name="Destiny",
            availability={
                "Monday": [False, False],
                "Tuesday": [True, False],
                "Wednesday": [False, False],
                "Thursday": [True, False],
                "Friday": [True, False],
                "Saturday": [False, False],
                "Sunday": [False, False],
            },
            isSoup=False,
            maxShift=2,
            minShift=1,
        ),
        Person(
            name="Donny",
            availability={
                "Monday": [False, True],
                "Tuesday": [False, True],
                "Wednesday": [False, False],
                "Thursday": [False, False],
                "Friday": [False, False],
                "Saturday": [False, False],
                "Sunday": [False, False],
            },
            isSoup=False,
            maxShift=2,
            minShift=0,
        ),
        Person(
            name="Imogene",
            availability={
                "Monday": [False, True],
                "Tuesday": [True, True],
                "Wednesday": [False, True],
                "Thursday": [True, False],  # UNAVAILABLE ON NIGHT
                "Friday": [True, False],
                "Saturday": [True, True],
                "Sunday": [False, True],
            },
            isSoup=False,
            maxShift=5,
            minShift=2,
        ),
        Person(
            name="Jacob",
            availability={
                "Monday": [True, False],
                "Tuesday": [False, True],
                "Wednesday": [False, False],
                "Thursday": [False, False],
                "Friday": [False, False],
                "Saturday": [False, False],
                "Sunday": [True, False],
            },
            isSoup=True,
            maxShift=3,
            minShift=1,
        ),
        Person(
            name="Jason",
            availability={
                "Monday": [False, False],
                "Tuesday": [False, True],
                "Wednesday": [False, True],
                "Thursday": [False, True],
                "Friday": [False, True],
                "Saturday": [False, False],
                "Sunday": [False, True],
            },
            isSoup=False,
            maxShift=3,
            minShift=1,
        ),
        Person(
            name="Janice",
            availability={
                "Monday": [False, False],
                "Tuesday": [False, False],
                "Wednesday": [False, False],
                "Thursday": [False, True],
                "Friday": [True, True],
                "Saturday": [True, True],
                "Sunday": [False, False],
            },
            isSoup=False,
            maxShift=3,
            minShift=1,
        ),
        Person(
            name="Jojo",
            availability={
                "Monday": [False, False],
                "Tuesday": [False, True],
                "Wednesday": [False, False],
                "Thursday": [False, True],
                "Friday": [False, False],  # UNAVAILABLE
                "Saturday": [False, False],
                "Sunday": [False, False],
            },
            isSoup=False,
            maxShift=2,
            minShift=0,
        ),
        Person(
            name="John",
            availability={
                "Monday": [False, False],
                "Tuesday": [False, False],
                "Wednesday": [False, False],
                "Thursday": [False, False],
                "Friday": [False, False],
                "Saturday": [False, False],
                "Sunday": [False, True],
            },
            isSoup=True,
            maxShift=1,
            minShift=1,
        ),
        Person(
            name="Josh",
            availability={
                "Monday": [True, True],
                "Tuesday": [True, True],
                "Wednesday": [True, True],
                "Thursday": [True, True],
                "Friday": [False, False],  # UNAVAILABLE
                "Saturday": [False, False],  # UNAVAILABLE
                "Sunday": [False, True],  # UNAVAILABLE
            },
            isSoup=False,
            maxShift=4,
            minShift=0,
        ),
        Person(
            name="Karen",
            availability={
                "Monday": [False, True],
                "Tuesday": [False, True],
                "Wednesday": [False, False],  # UNAVAILABLE
                "Thursday": [False, True],
                "Friday": [False, True],
                "Saturday": [True, False],
                "Sunday": [True, False],
            },
            isSoup=True,
            maxShift=4,
            minShift=0,
        ),
        Person(
            name="Kayla",
            availability={
                "Monday": [False, False],
                "Tuesday": [False, False],
                "Wednesday": [False, False],
                "Thursday": [True, True],
                "Friday": [False, False],
                "Saturday": [False, False],  # UNAVAILABLE
                "Sunday": [False, False],  # UNAVAILABLE
            },
            isSoup=True,
            maxShift=4,
            minShift=2,
        ),
        Person(
            name="Lester",
            availability={
                "Monday": [False, False],
                "Tuesday": [False, True],
                "Wednesday": [True, True],
                "Thursday": [False, True],
                "Friday": [True, True],
                "Saturday": [True, True],
                "Sunday": [True, True],
            },
            isSoup=True,
            maxShift=3,
            minShift=2,
        ),
        Person(
            name="Luan",
            availability={
                "Monday": [True, False],
                "Tuesday": [True, False],
                "Wednesday": [True, False],
                "Thursday": [True, False],
                "Friday": [False, True],
                "Saturday": [False, False],
                "Sunday": [True, True],
            },
            isSoup=False,
            maxShift=3,
            minShift=3,
        ),
        Person(
            name="Maddie",
            availability={
                "Monday": [False, False],
                "Tuesday": [False, False],
                "Wednesday": [False, False],
                "Thursday": [False, False],
                "Friday": [False, False],
                "Saturday": [True, True],
                "Sunday": [True, False],
            },
            isSoup=False,
            maxShift=2,
            minShift=0,
        ),
        Person(
            name="Raj",
            availability={
                "Monday": [True, False],
                "Tuesday": [False, False],
                "Wednesday": [False, False],
                "Thursday": [False, False],
                "Friday": [True, False],
                "Saturday": [False, False],  # UNAVAILABLE
                "Sunday": [False, False],  # UNAVAILABLE
            },
            isSoup=True,
            maxShift=4,
            minShift=1,
        ),
        Person(
            name="Richard",
            availability={
                "Monday": [False, False],
                "Tuesday": [False, False],
                "Wednesday": [False, False],
                "Thursday": [False, False],
                "Friday": [False, False],
                "Saturday": [False, False],
                "Sunday": [False, False],
            },
            isSoup=False,
            maxShift=1,
            minShift=0,
        ),
        Person(
            name="Shawn",
            availability={
                "Monday": [False, True],
                "Tuesday": [False, True],
                "Wednesday": [False, True],
                "Thursday": [False, False],  # UNAVAILABLE
                "Friday": [False, False],  # UNAVAILABLE
                "Saturday": [False, False],  # UNAVAILABLE
                "Sunday": [False, False],
            },
            isSoup=False,
            maxShift=4,
            minShift=1,
        ),
        Person(
            name="Tammy",
            availability={
                "Monday": [False, False],
                "Tuesday": [False, False],
                "Wednesday": [False, False],
                "Thursday": [False, False],
                "Friday": [False, False],
                "Saturday": [False, False],
                "Sunday": [True, False],
            },
            isSoup=True,
            maxShift=2,
            minShift=0,
        ),
        Person(
            name="Tayvia",
            availability={
                "Monday": [False, False],
                "Tuesday": [False, True],
                "Wednesday": [False, False],
                "Thursday": [False, False],
                "Friday": [False, True],
                "Saturday": [True, True],
                "Sunday": [False, False],
            },
            isSoup=False,
            maxShift=2,
            minShift=1,
        ),

    ]

    # Create a schedule and populate it
    schedule = Schedule()
    schedule.fillShiftsBacktracking(employees)
    # Print the filled schedule
    print(schedule)
