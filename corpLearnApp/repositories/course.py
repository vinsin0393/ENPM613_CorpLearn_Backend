
class CourseRepository:
    def __init__(self, model):
        self.model = model

    def create_course(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def update_course(self, code, **kwargs):
        course = self.model.objects.get(code=code)
        for key, value in kwargs.items():
            setattr(course, key, value)
        course.save()
        return course

    def get_course(self, code):
        return self.model.objects.get(code=code)

    def delete_course(self, code):
        return self.model.objects.get(code=code).delete()

    def get_all_course(self):
        return self.model.objects.all()
