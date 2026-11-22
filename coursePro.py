import sys

def calculate_grade(avg):
    if avg < 0 or avg > 100:
        return "Invalid Marks"
    elif avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3


def main():
    if len(sys.argv) != 7:
        print("Invalid arguments")
        sys.exit(1)

    name = sys.argv[1]
    department = sys.argv[2]
    semester = int(sys.argv[3])

    m1 = float(sys.argv[4])
    m2 = float(sys.argv[5])
    m3 = float(sys.argv[6])

    if any(mark < 0 or mark > 100 for mark in [m1, m2, m3]):
        print("Invalid marks")
        sys.exit(1)

    average = calculate_average(m1, m2, m3)
    grade = calculate_grade(average)

    print("\n----- STUDENT RESULT -----")
    print("Name:", name)
    print("Department:", department)
    print("Semester:", semester)
    print("Average:", round(average, 2))
    print("Grade:", grade)


if __name__ == "__main__":
    main()
