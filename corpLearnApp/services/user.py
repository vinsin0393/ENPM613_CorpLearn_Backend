from django.contrib.auth.hashers import make_password
from corpLearnApp.models import User, Role, Announcement, EmployeeConcern, DiscussionForum, DiscussionForumQuestion, DiscussionForumAnswer
from corpLearnApp.repositories import UserRepository, RoleRepository, EmployeeConcernRepository, AnnounceRepository, DiscussionForumRepository, DiscussionForumQuestionRepository, DiscussionForumAnswerRepository
from corpLearnApp.serializers import UserSerializer, AnnouncementSerializer, EmployeeConcernSerializer, DiscussionForumSerializer, DiscussionForumQuestionSerializer, DiscussionForumAnswerSerializer
from corpLearnApp.services.service_exception_log_handler.exception_log_handler import exception_log_handler
from django.core.exceptions import ObjectDoesNotExist



class UserService:

    @staticmethod
    @exception_log_handler
    def add_user(data):
        default_password = 'test@1'
        hashed_password = make_password(default_password)
        data['password'] = hashed_password
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user_repo = UserRepository(User)
            user = user_repo.create_user(**serializer.validated_data)
            return UserSerializer(user).data

    @staticmethod
    @exception_log_handler
    def update_user(user_id, data):
        user_repo = UserRepository(User)
        if data.get('password') is not None:
            hashed_password = make_password(data.get('password'))
            data['password'] = hashed_password
        user = user_repo.update_user(user_id, **data)
        return UserSerializer(user).data

    @staticmethod
    @exception_log_handler
    def get_user(user_id):
        user_repo = UserRepository(User)
        user = user_repo.get_user(user_id)
        return UserSerializer(user).data

    @staticmethod
    @exception_log_handler
    def delete_user(user_id):
        user_repo = UserRepository(User)
        user_repo.delete_user(user_id)
        return {'message': 'User deleted successfully'}

    @staticmethod
    @exception_log_handler
    def add_default_role():
        role_repo = RoleRepository(Role)
        return role_repo.get_or_create_default_roles()

    @staticmethod
    @exception_log_handler
    def create_announcement(data):
        admin = data.pop('admin', None)

        try:
            admin = UserRepository(User).get_user(admin)
        except User.DoesNotExist:
            raise ObjectDoesNotExist(f"No User with id {admin} exists.")
        data['admin'] = admin
        repository = AnnounceRepository(Announcement)
        announcement = repository.create_announcement(**data)
        return AnnouncementSerializer(announcement).data

    @staticmethod
    @exception_log_handler
    def update_announcement(id, data):
        repository = AnnounceRepository(Announcement)
        announcement = repository.update_announcement(id, **data)
        return AnnouncementSerializer(announcement).data

    @staticmethod
    @exception_log_handler
    def get_announcement(id):
        repository = AnnounceRepository(Announcement)
        announcement = repository.get_announcement(id)
        return AnnouncementSerializer(announcement).data

    @staticmethod
    @exception_log_handler
    def delete_announcement(id):
        repository = AnnounceRepository(Announcement)
        repository.delete_announcement(id)
        return {'message': 'Module deleted successfully'}


    @staticmethod
    @exception_log_handler
    def create_employee_concern(data):
        employee = data.pop('employee', None)
        try:
            employee = UserRepository(User).get_user(employee)
        except User.DoesNotExist:
            raise ObjectDoesNotExist(f"No User with id {employee} exists.")
        data['employee'] = employee
        repository = EmployeeConcernRepository(EmployeeConcern)
        concern = repository.create_employee_corncern(**data)
        return EmployeeConcernSerializer(concern).data

    @staticmethod
    @exception_log_handler
    def update_employee_concern(id, data):
        repository = EmployeeConcernRepository(EmployeeConcern)
        concern = repository.update_employee_corncern(id, **data)
        return EmployeeConcernSerializer(concern).data

    @staticmethod
    @exception_log_handler
    def get_employee_concern(id):
        repository = EmployeeConcernRepository(EmployeeConcern)
        concern = repository.get_employee_corncern(id)
        return EmployeeConcernSerializer(concern).data

    @staticmethod
    @exception_log_handler
    def delete_employee_concern(id):
        repository = EmployeeConcernRepository(EmployeeConcern)
        repository.delete_employee_corncern(id)
        return {'message': 'Module deleted successfully'}

    @staticmethod
    @exception_log_handler
    def create_discussion_forum(data):
        repository = DiscussionForumRepository(DiscussionForum)
        forum = repository.create_discussion_forum(**data)
        return DiscussionForumSerializer(forum).data

    @staticmethod
    @exception_log_handler
    def update_discussion_forum(id, data):
        repository = DiscussionForumRepository(DiscussionForum)
        forum = repository.update_discussion_forum(id, **data)
        return DiscussionForumSerializer(forum).data

    @staticmethod
    @exception_log_handler
    def get_discussion_forum(id):
        repository = DiscussionForumRepository(DiscussionForum)
        forum = repository.get_discussion_forum(id)
        return DiscussionForumSerializer(forum).data

    @staticmethod
    @exception_log_handler
    def delete_discussion_forum(id):
        repository = DiscussionForumRepository(DiscussionForum)
        repository.delete_discussion_forum(id)
        return {'message': 'Module deleted successfully'}

    @staticmethod
    @exception_log_handler
    def create_discussion_forum_question(data):
        discussion_forum = data.pop('discussion_forum', None)
        user = data.pop('user', None)
        try:
            discussion_forum = DiscussionForumRepository(DiscussionForum).get_discussion_forum(discussion_forum)
            user = UserRepository(User).get_user(user)
        except DiscussionForum.DoesNotExist:
            raise ObjectDoesNotExist(f"No Discussion Question with id {discussion_forum} exists.")
        data['discussion_forum'] = discussion_forum
        data['user'] = user
        repository = DiscussionForumQuestionRepository(DiscussionForumQuestion)
        question = repository.create_discussion_forum_question(**data)
        return DiscussionForumQuestionSerializer(question).data

    @staticmethod
    @exception_log_handler
    def update_discussion_forum_question(id, data):
        repository = DiscussionForumQuestionRepository(DiscussionForumQuestion)
        question = repository.update_discussion_forum_question(id, **data)
        return DiscussionForumQuestionSerializer(question).data

    @staticmethod
    @exception_log_handler
    def get_discussion_forum_question(id):
        repository = DiscussionForumQuestionRepository(DiscussionForumQuestion)
        question = repository.get_discussion_forum_question(id)
        return DiscussionForumQuestionSerializer(question).data

    @staticmethod
    @exception_log_handler
    def delete_discussion_forum_question(id):
        repository = DiscussionForumQuestionRepository(DiscussionForumQuestion)
        repository.delete_discussion_forum_question(id)
        return {'message': 'Module deleted successfully'}

    @staticmethod
    @exception_log_handler
    def create_discussion_forum_answer(data):
        question = data.pop('question', None)
        user = data.pop('user', None)
        try:
            question = DiscussionForumQuestionRepository(DiscussionForumQuestion).get_discussion_forum_question(question)
            user = UserRepository(User).get_user(user)
        except DiscussionForumQuestion.DoesNotExist:
            raise ObjectDoesNotExist(f"No Discussion with id {question} exists.")
        data['question'] = question
        data['user'] = user
        repository = DiscussionForumAnswerRepository(DiscussionForumAnswer)
        question = repository.create_discussion_forum_answer(**data)
        return DiscussionForumAnswerSerializer(question).data

    @staticmethod
    @exception_log_handler
    def update_discussion_forum_answer(id, data):
        repository = DiscussionForumAnswerRepository(DiscussionForumAnswer)
        question = repository.update_discussion_forum_answer(id, **data)
        return DiscussionForumAnswerSerializer(question).data

    @staticmethod
    @exception_log_handler
    def get_discussion_forum_answer(id):
        repository = DiscussionForumAnswerRepository(DiscussionForumAnswer)
        question = repository.get_discussion_forum_answer(id)
        return DiscussionForumAnswerSerializer(question).data

    @staticmethod
    @exception_log_handler
    def delete_discussion_forum_answer(id):
        repository = DiscussionForumAnswerRepository(DiscussionForumAnswer)
        repository.delete_discussion_forum_answer(id)
        return {'message': 'Module deleted successfully'}

    @staticmethod
    @exception_log_handler
    def get_all_announcements():
        repo = AnnounceRepository(Announcement)
        return repo.get_all_announcements()

    @staticmethod
    @exception_log_handler
    def get_all_discussion_forums():
        repo = DiscussionForumRepository(DiscussionForum)
        return repo.get_all_discussion_forum()

    @staticmethod
    @exception_log_handler
    def get_answers_by_question_id(question_id):
        repo = DiscussionForumAnswerRepository(DiscussionForumAnswer)
        return repo.get_discussion_forum_answer_by_question_id(question_id)

    @staticmethod
    @exception_log_handler
    def get_all_employee_concerns():
        repo = EmployeeConcernRepository(EmployeeConcern)
        return repo.get_all_employee_concern()

    @staticmethod
    @exception_log_handler
    def get_employee_concerns_by_user_id(user_id):
        repo = EmployeeConcernRepository(EmployeeConcern)
        return repo.get_employee_concerns_by_user_id(user_id)

    @staticmethod
    @exception_log_handler
    def get_all_users():
        repo = UserRepository(User)
        return repo.get_all_user()
    @staticmethod
    @exception_log_handler
    def add_test_admin_user():
        user_repo = UserRepository(User)
        default_password = 'test@1'
        hashed_password = make_password(default_password)
        user_repo.get_or_create_default_user(password=hashed_password)


