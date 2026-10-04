def calculateGrossSalary(basicSalary, allowances=0.0, bonus=0.0):
    return basicSalary + allowances + bonus

def calculateNetSalary(grossSalary, deductions=0.0):
    return grossSalary - deductions

def getPositiveNumber(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Amount cannot be negative. Please enter 0 or more.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

def displaySalarySummary(employeeName, grossSalary, deductions, netSalary):
    print("\n--- Monthly Salary Summary ---")
    print(f"Employee Name : {employeeName}")
    print(f"Gross Salary  : {grossSalary:.2f}")
    print(f"Deductions    : {deductions:.2f}")
    print(f"Net Salary    : {netSalary:.2f}")


def main():
    print("---- Employee Salary Calculator ----")

    employeeName = input("Enter employee name: ").strip()
    while not employeeName:
        print("Employee name cannot be empty.")
        employeeName = input("Enter employee name: ").strip()

    basicSalary = getPositiveNumber("Enter basic salary: ")
    allowances = getPositiveNumber("Enter allowances (0 if none): ")
    bonus = getPositiveNumber("Enter bonus (0 if none): ")

    grossSalary = calculateGrossSalary(basicSalary, allowances, bonus)

    while True:
        deductions = getPositiveNumber("Enter deductions (0 if none): ")
        if deductions <= grossSalary:
            break
        print(f"Deductions cannot exceed gross salary ({grossSalary:.2f}). Try again.")

    netSalary = calculateNetSalary(grossSalary, deductions)

    displaySalarySummary(employeeName, grossSalary, deductions, netSalary)


if __name__ == "__main__":
    main()