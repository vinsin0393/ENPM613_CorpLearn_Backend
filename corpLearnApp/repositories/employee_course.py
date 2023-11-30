
import json
class EmployeeCourseRepository:
    def __init__(self, model):
        self.model = model

    def create_employee_course(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def update_employee_course(self, id, **kwargs):
        employeeCourse = self.model.objects.get(id=id)
        if not "data" in kwargs:
            data = {}
            if employeeCourse.data != '': 
                data = json.loads(employeeCourse.data)
            if "status" in kwargs and kwargs["status"] == "InProgress": data["current_module"] = 0
        if "data" in kwargs:
            data = kwargs["data"]

        kwargs["data"] = json.dumps(data)
        for key, value in kwargs.items():
            setattr(employeeCourse, key, value)
        employeeCourse.save()
        return employeeCourse

    def get_employee_course(self, id):
        return self.model.objects.get(id=id)

    def delete_employee_course(self, id):
        return self.model.objects.get(id=id).delete()

    def get_employee_course_by_user_id(self, user_id):
        return self.model.objects.filter(employee__id=user_id)
