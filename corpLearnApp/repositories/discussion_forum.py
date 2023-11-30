
class DiscussionForumRepository:
    def __init__(self, model):
        self.model = model

    def create_discussion_forum(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def update_discussion_forum(self, id, **kwargs):
        discussionForum = self.model.objects.get(id=id)
        for key, value in kwargs.items():
            setattr(discussionForum, key, value)
        discussionForum.save()
        return discussionForum

    def get_discussion_forum(self, id):
        return self.model.objects.get(course_id=id)

    def delete_discussion_forum(self, id):
        return self.model.objects.get(id=id).delete()

    def get_all_discussion_forum(self):
        return self.model.objects.all()
