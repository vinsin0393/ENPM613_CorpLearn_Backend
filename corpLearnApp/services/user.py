from django.contrib.auth.hashers import make_password
from corpLearnApp.models import User, Role, Announcement, EmployeeConcern, DiscussionForum, DiscussionForumQuestion, DiscussionForumAnswer, Course
from corpLearnApp.repositories import UserRepository, RoleRepository, EmployeeConcernRepository, AnnounceRepository, DiscussionForumRepository, DiscussionForumQuestionRepository, DiscussionForumAnswerRepository
from corpLearnApp.serializers import UserSerializer, AnnouncementSerializer, EmployeeConcernSerializer, DiscussionForumSerializer, DiscussionForumQuestionSerializer, DiscussionForumAnswerSerializer
from corpLearnApp.services.service_exception_log_handler.exception_log_handler import exception_log_handler
from django.core.exceptions import ObjectDoesNotExist



class UserService:

    @staticmethod
    @exception_log_handler
    def add_user(data):
        """ Adds a new user to the system with default password settings. """
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
        """ Updates an existing user's details identified by 'user_id'. """
        user_repo = UserRepository(User)
        if data.get('password') is not None:
            hashed_password = make_password(data.get('password'))
            data['password'] = hashed_password
        user = user_repo.update_user(user_id, **data)
        return UserSerializer(user).data

    @staticmethod
    @exception_log_handler
    def get_user(user_id):
        """ Retrieves a specific user based on 'user_id'. """
        user_repo = UserRepository(User)
        user = user_repo.get_user(user_id)
        return UserSerializer(user).data

    @staticmethod
    @exception_log_handler
    def delete_user(user_id):
        """ Deletes a user identified by 'user_id'. """
        user_repo = UserRepository(User)
        user_repo.delete_user(user_id)
        return {'message': 'User deleted successfully'}

    @staticmethod
    @exception_log_handler
    def add_default_role():
        """ Adds a default role in the system. Useful for initial setup. """
        role_repo = RoleRepository(Role)
        return role_repo.get_or_create_default_roles()

    @staticmethod
    @exception_log_handler
    def create_announcement(data):
        """ Creates a new announcement in the system. """
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
        """ Updates an existing announcement identified by 'id'. """
        repository = AnnounceRepository(Announcement)
        announcement = repository.update_announcement(id, **data)
        return AnnouncementSerializer(announcement).data

    @staticmethod
    @exception_log_handler
    def get_announcement(id):
        """ Retrieves a specific announcement based on its 'id'. """
        repository = AnnounceRepository(Announcement)
        announcement = repository.get_announcement(id)
        return AnnouncementSerializer(announcement).data

    @staticmethod
    @exception_log_handler
    def delete_announcement(id):
        """ Deletes an announcement identified by 'id'. """
        repository = AnnounceRepository(Announcement)
        repository.delete_announcement(id)
        return {'message': 'Module deleted successfully'}


    @staticmethod
    @exception_log_handler
    def create_employee_concern(data):
        """ Creates a new employee concern. """
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
        """ Updates an existing employee concern identified by 'id'. """
        repository = EmployeeConcernRepository(EmployeeConcern)
        concern = repository.update_employee_corncern(id, **data)
        return EmployeeConcernSerializer(concern).data

    @staticmethod
    @exception_log_handler
    def get_employee_concern(id):
        """ Retrieves a specific employee concern based on its 'id'. """
        repository = EmployeeConcernRepository(EmployeeConcern)
        concern = repository.get_employee_corncern(id)
        return EmployeeConcernSerializer(concern).data

    @staticmethod
    @exception_log_handler
    def delete_employee_concern(id):
        """ Deletes an employee concern identified by 'id'. """
        repository = EmployeeConcernRepository(EmployeeConcern)
        repository.delete_employee_corncern(id)
        return {'message': 'Module deleted successfully'}

    @staticmethod
    @exception_log_handler
    def create_discussion_forum(data):
        """ Creates a new discussion forum. """
        repository = DiscussionForumRepository(DiscussionForum)
        data["course"] = Course.objects.get(code=data['course'])
        try:
            repository.get_discussion_forum(data["course"])
            forum = repository.get_discussion_forum(data["course"])
            return DiscussionForumSerializer(forum).data
        except Exception as e:
            forum = repository.create_discussion_forum(**data)
            return DiscussionForumSerializer(forum).data

    @staticmethod
    @exception_log_handler
    def update_discussion_forum(id, data):
        """ Updates an existing discussion forum identified by 'id'. """
        repository = DiscussionForumRepository(DiscussionForum)
        forum = repository.update_discussion_forum(id, **data)
        return DiscussionForumSerializer(forum).data

    @staticmethod
    @exception_log_handler
    def get_discussion_forum(id):
        """ Retrieves a specific discussion forum based on its 'id'. """
        repository = DiscussionForumRepository(DiscussionForum)
        forum = repository.get_discussion_forum(id)
        return DiscussionForumSerializer(forum).data

    @staticmethod
    @exception_log_handler
    def delete_discussion_forum(id):
        """ Deletes a discussion forum identified by 'id'. """
        repository = DiscussionForumRepository(DiscussionForum)
        repository.delete_discussion_forum(id)
        return {'message': 'Module deleted successfully'}

    @staticmethod
    @exception_log_handler
    def create_discussion_forum_question(data):
        """ Creates a new discussion forum question. """
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
        """ Updates an existing discussion forum question identified by 'id'. """
        repository = DiscussionForumQuestionRepository(DiscussionForumQuestion)
        question = repository.update_discussion_forum_question(id, **data)
        return DiscussionForumQuestionSerializer(question).data

    @staticmethod
    @exception_log_handler
    def get_discussion_forum_question(id):
        """ Get an existing discussion forum question identified by 'id'. """
        repository = DiscussionForumQuestionRepository(DiscussionForumQuestion)
        questions = repository.get_discussion_forum_question(id)
        return [DiscussionForumQuestionSerializer(question).data for question in questions]

    @staticmethod
    @exception_log_handler
    def delete_discussion_forum_question(id):
        """ Delete an existing discussion forum question identified by 'id'. """
        repository = DiscussionForumQuestionRepository(DiscussionForumQuestion)
        repository.delete_discussion_forum_question(id)
        return {'message': 'Module deleted successfully'}

    @staticmethod
    @exception_log_handler
    def create_discussion_forum_answer(data):
        """ Creates a discussion forum anwer"""
        question = data.pop('question', None)
        user = data.pop('user', None)
        try:
            question = DiscussionForumQuestionRepository(DiscussionForumQuestion).get_discussion_question(question)
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
        """ Updates an existing discussion forum answer identified by 'id'. """
        repository = DiscussionForumAnswerRepository(DiscussionForumAnswer)
        question = repository.update_discussion_forum_answer(id, **data)
        return DiscussionForumAnswerSerializer(question).data

    @staticmethod
    @exception_log_handler
    def get_discussion_forum_answer(id):
        """ Gets an existing discussion forum answer identified by 'id'. """
        repository = DiscussionForumAnswerRepository(DiscussionForumAnswer)
        question = repository.get_discussion_forum_answer(id)
        return DiscussionForumAnswerSerializer(question).data

    @staticmethod
    @exception_log_handler
    def delete_discussion_forum_answer(id):
        """ Deletes an existing discussion forum answer identified by 'id'. """
        repository = DiscussionForumAnswerRepository(DiscussionForumAnswer)
        repository.delete_discussion_forum_answer(id)
        return {'message': 'Module deleted successfully'}

    @staticmethod
    @exception_log_handler
    def get_all_announcements():
        """ Retrieves all announcements available in the system. """
        repo = AnnounceRepository(Announcement)
        return repo.get_all_announcements()

    @staticmethod
    @exception_log_handler
    def get_all_discussion_forums():
        """ Retrieves all discussion forums available. """
        repo = DiscussionForumRepository(DiscussionForum)
        return repo.get_all_discussion_forum()

    @staticmethod
    @exception_log_handler
    def get_answers_by_question_id(question_id):
        """ Retrieves answers for a specific discussion forum question identified by 'question_id'. """
        repo = DiscussionForumAnswerRepository(DiscussionForumAnswer)
        return repo.get_discussion_forum_answer_by_question_id(question_id)

    @staticmethod
    @exception_log_handler
    def get_all_employee_concerns():
        """ Retrieves all employee concerns logged in the system. """
        repo = EmployeeConcernRepository(EmployeeConcern)
        return repo.get_all_employee_concern()

    @staticmethod
    @exception_log_handler
    def get_employee_concerns_by_user_id(user_id):
        """ Retrieves employee concerns associated with a specific user identified by 'user_id'. """
        repo = EmployeeConcernRepository(EmployeeConcern)
        return repo.get_employee_concerns_by_user_id(user_id)

    @staticmethod
    @exception_log_handler
    def get_all_users():
        """ Retrieves all users registered in the system. """
        repo = UserRepository(User)
        return repo.get_all_user()

    @staticmethod
    @exception_log_handler
    def add_test_admin_user():
        """ Adds a test admin user to the system. Useful for testing purposes. """
        user_repo = UserRepository(User)
        default_password = 'test@1'
        hashed_password = make_password(default_password)
        user_repo.get_or_create_default_user(password=hashed_password)


