class AnnounceRepository:
    def __init__(self, model):
        self.model = model

    def create_announcement(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def update_announcement(self, id, **kwargs):
        announcement = self.model.objects.get(id=id)
        for key, value in kwargs.items():
            setattr(announcement, key, value)
        announcement.save()
        return announcement

    def get_announcement(self, id):
        return self.model.objects.get(id=id)

    def delete_announcement(self, id):
        return self.model.objects.get(id=id).delete()

    def get_all_announcements(self):
        return self.model.objects.all()
