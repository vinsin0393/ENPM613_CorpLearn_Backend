class TrainingDocumentRepository:
    def __init__(self, model):
        self.model = model

    def create_training_document(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def update_training_document(self, id, **kwargs):
        announcement = self.model.objects.get(id=id)
        for key, value in kwargs.items():
            setattr(announcement, key, value)
        announcement.save()
        return announcement

    def get_training_document(self, id):
        return self.model.objects.get(id=id)

    def delete_training_document(self, id):
        return self.model.objects.get(id=id).delete()
