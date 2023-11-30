
class DiscussionForumQuestionRepository:
    def __init__(self, model):
        self.model = model

    def create_discussion_forum_question(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def update_discussion_forum_question(self, id, **kwargs):
        question = self.model.objects.get(id=id)
        for key, value in kwargs.items():
            setattr(question, key, value)
        question.save()
        return question

    def get_discussion_forum_question(self, id):
        return self.model.objects.filter(discussion_forum_id=id)
    
    def get_discussion_question(self, pk):
        return self.model.objects.get(id=pk)

    def delete_discussion_forum_question(self, id):
        return self.model.objects.get(id=id).delete()

    def get_all_discussion_forum_question(self):
        return self.model.objects.all()

    def get_discussion_forum_question_by_discussion_id(self, id):
        return self.model.objects.filter(discussion_forum__id=id)