
class ModuleRepository:
    def __init__(self, model):
        self.model = model

    def create_module(self, **kwargs):
        kwargs['course_id'] = kwargs['course']
        del kwargs['course']
        return self.model.objects.create(**kwargs)

    def update_module(self, id, **kwargs):
        module = self.model.objects.get(id=id)
        for key, value in kwargs.items():
            setattr(module, key, value)
        module.save()
        return module

    def get_module(self, id):
        return self.model.objects.get(id=id)

    def delete_module(self, id):
        return self.model.objects.get(id=id).delete()

    def get_all_module(self):
        return self.model.objects.all()

    def get_module_by_course_id(self, id):
        return self.model.objects.filter(course__code=id)

    def get_module_by_document_id(self, id):
        return self.model.objects.filter(training_document__id=id)
