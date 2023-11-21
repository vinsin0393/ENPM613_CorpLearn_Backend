
class DiscussionForumAnswerRepository:
    def __init__(self, model):
        self.model = model

    def create_discussion_forum_answer(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def update_discussion_forum_answer(self, id, **kwargs):
        answer = self.model.objects.get(id=id)
        for key, value in kwargs.items():
            setattr(answer, key, value)
        answer.save()
        return answer

    def get_discussion_forum_answer(self, id):
        return self.model.objects.get(id=id)

    def delete_discussion_forum_answer(self, id):
        return self.model.objects.get(id=id).delete()


    def get_discussion_forum_answer_by_question_id(self, id):
        return self.model.objects.filter(question__id=id)
