
class CourseRepository:
    def __init__(self, model, code=None):
        self.model = model
        self.code = code

    def create_course(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def update_course_data(self, **kwargs):
        course = self.model.objects.get(code=self.code)
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
