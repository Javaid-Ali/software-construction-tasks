class Employee:
    def __init__(self, active, months_employed, rating,
                 disciplinary_action, attendance):
        self.active = active
        self.months_employed = months_employed
        self.rating = rating
        self.disciplinary_action = disciplinary_action
        self.attendance = attendance

def eligibility(employee):
    is_active = employee.active
    has_required_service = employee.months_employed >= 12
    has_required_rating = employee.rating >= 4
    has_no_disciplinary_action = not employee.disciplinary_action
    has_required_attendance = employee.attendance >= 90

    return (
        is_active
        and has_required_service
        and has_required_rating
        and has_no_disciplinary_action
        and has_required_attendance
    )

normal_employee = Employee(True, 24, 4.5, False, 95)
boundary_employee = Employee(True, 12, 4, False, 90)
failed_employee = Employee(True, 11, 3, True, 85)

print(eligibility(normal_employee))
print(eligibility(boundary_employee))
print(eligibility(failed_employee))