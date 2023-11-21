
class EmployeeConcernRepository:
    def __init__(self, model):
        self.model = model

    def create_employee_corncern(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def update_employee_corncern(self, id, **kwargs):
        employeecorncern = self.model.objects.get(id=id)
        for key, value in kwargs.items():
            setattr(employeecorncern, key, value)
        employeecorncern.save()
        return employeecorncern

    def get_employee_corncern(self, id):
        return self.model.objects.get(id=id)

    def delete_employee_corncern(self, id):
        return self.model.objects.get(id=id).delete()

    def get_all_employee_concern(self):
        return self.model.objects.all()

    def get_employee_concerns_by_user_id(self, user_id):
        return self.model.objects.filter(employee__id=user_id)