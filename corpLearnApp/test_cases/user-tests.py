import datetime

from django.test import TestCase
from django.contrib.auth.hashers import check_password
from corpLearnApp.models import User, Role, Announcement, EmployeeConcern, DiscussionForum, DiscussionForumQuestion, \
    DiscussionForumAnswer
from corpLearnApp.repositories import DiscussionForumQuestionRepository, UserRepository, DiscussionForumRepository, \
    DiscussionForumAnswerRepository
from corpLearnApp.services.user import UserService
from django.utils import timezone

class UserServiceTestCase(TestCase):

    def setUp(self):
        Role.objects.create(name='Test Role')
        self.user_data = {
            'email': 'test@example.com',
            'name': 'Test User',
            'role_id': Role.objects.first().id,
        }
        self.admin_user = User.objects.create_user(id= 1, email='admin@example.com', name='Admin User', password='admin@123')
        self.announcement_data = {
            'content': 'This is a test announcement',
            'admin': self.admin_user.id
        }
        self.announcement = Announcement.objects.create(
            content='Initial Announcement',
            admin=self.admin_user
        )

        self.employee = UserRepository(User).create_user(id=1, email='employee@example.com', name='Employee', password='employee@123')
        self.concern_data = {
            'content': 'This is a test concern',
            'employee': self.employee.id
        }
        self.concern = EmployeeConcern.objects.create(
            content='Initial Concern',
            employee=self.employee)

        self.specific_time = timezone.make_aware(datetime.datetime(2023, 11, 20, 16, 1, 10, 991518))
        self.forum_data ={'created_date': self.specific_time}
        self.forum = DiscussionForumRepository(DiscussionForum).create_discussion_forum(created_date=self.specific_time)

        self.user = UserRepository(User).create_user(id= 1,email='user@example.com', name='Test User', password='test@123')
        self.discussion_forum = DiscussionForumRepository(DiscussionForum).create_discussion_forum(created_date=self.specific_time)
        self.question_data = {
            'content': 'This is a test question',
            'discussion_forum': self.discussion_forum.id,
            'user': self.user.id
        }
        self.question = DiscussionForumQuestion.objects.create(
            id= 1,
            content='Initial Question',
            discussion_forum=self.discussion_forum,
            user=self.user
        )
        self.answer_data = {
            'question': self.question.id,
            'user': self.user.id,
            'content': 'This is a test answer'
        }
        self.answer = DiscussionForumAnswerRepository(DiscussionForumAnswer).create_discussion_forum_answer(
            question=self.question,
            user=self.user,
            content='Initial Answer'
        )
        self.employee_concern = EmployeeConcern.objects.create(
            content='This is a test concern',
            employee=self.employee
        )


    def test_add_user(self):
        user_data = UserService.add_user(self.user_data)
        user = User.objects.get(email=self.user_data['email'])
        self.assertIsNotNone(user_data)
        self.assertEqual(user_data['email'], user.email)
        self.assertEqual(user_data['name'], user.name)
        self.assertIsNotNone(user)
        self.assertTrue(check_password('test@1', user.password))


    def test_update_user(self):
        updated_name = 'Updated Test User'
        UserService.update_user(self.user.id, {'name': updated_name})
        updated_user = User.objects.get(id=self.user.id)
        self.assertEqual(updated_user.name, updated_name)

    def test_get_user(self):
        user_data = UserService.get_user(self.user.id)

        self.assertEqual(user_data['email'], self.user.email)
        self.assertEqual(user_data['name'], self.user.name)

    def test_delete_user(self):
        UserService.delete_user(self.user.id)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=self.user.id)


    def test_create_announcement(self):
        announcement_data = UserService.create_announcement(self.announcement_data)
        announcement = Announcement.objects.get(id=announcement_data['id'])
        self.assertEqual(announcement_data['content'], announcement.content)
        self.assertEqual(announcement.admin, self.admin_user)

    def test_update_announcement(self):
        new_content = 'Updated content'
        UserService.update_announcement(self.announcement.id, {'content': new_content})
        updated_announcement = Announcement.objects.get(id=self.announcement.id)
        self.assertEqual(updated_announcement.content, new_content)

    def test_get_announcement(self):
        announcement_data = UserService.get_announcement(self.announcement.id)
        self.assertEqual(announcement_data['content'], self.announcement.content)

    def test_delete_announcement(self):
        UserService.delete_announcement(self.announcement.id)
        with self.assertRaises(Announcement.DoesNotExist):
            Announcement.objects.get(id=self.announcement.id)

    def test_create_employee_concern(self):
        concern_data = UserService.create_employee_concern(self.concern_data)
        concern = EmployeeConcern.objects.get(id=concern_data['id'])
        self.assertEqual(concern_data['content'], concern.content)
        self.assertEqual(concern.employee, self.employee)

    def test_update_employee_concern(self):
        new_content = 'Updated concern'
        UserService.update_employee_concern(self.concern.id, {'content': new_content})
        updated_concern = EmployeeConcern.objects.get(id=self.concern.id)
        self.assertEqual(updated_concern.content, new_content)

    def test_get_employee_concern(self):
        concern_data = UserService.get_employee_concern(self.concern.id)
        self.assertEqual(concern_data['content'], self.concern.content)

    def test_delete_employee_concern(self):
        UserService.delete_employee_concern(self.concern.id)
        with self.assertRaises(EmployeeConcern.DoesNotExist):
            EmployeeConcern.objects.get(id=self.concern.id)

    def test_create_discussion_forum(self):
        forum_data = UserService.create_discussion_forum(self.forum_data)
        forum = UserService.get_discussion_forum(id=forum_data['id'])
        self.assertEqual(forum['created_date'], '2023-11-20T16:01:10.991518Z')

    def test_update_discussion_forum(self):
        forum_data = UserService.create_discussion_forum(self.forum_data)
        forum = UserService.get_discussion_forum(forum_data['id'])
        id  =forum.pop('id', None)
        forum['created_date'] = '2023-11-21T16:01:10.991518Z'
        UserService.update_discussion_forum(id, forum)
        forum = UserService.get_discussion_forum(id)
        self.assertEqual(forum['created_date'], '2023-11-21T16:01:10.991518Z')

    def test_get_discussion_forum(self):
        forum_data = UserService.create_discussion_forum(self.forum_data)
        forum = UserService.get_discussion_forum(id= forum_data['id'])
        self.assertEqual(forum['id'], forum_data['id'])

    def test_delete_discussion_forum(self):
        UserService.delete_discussion_forum(self.forum.id)
        with self.assertRaises(DiscussionForum.DoesNotExist):
            DiscussionForum.objects.get(id=self.forum.id)

    def test_create_discussion_forum_question(self):
        question_data = UserService.create_discussion_forum_question(self.question_data)
        question = DiscussionForumQuestionRepository(DiscussionForumQuestion).get_discussion_forum_question(id=question_data['id'])
        self.assertEqual(question_data['content'], question.content)
        self.assertEqual(question.discussion_forum, self.discussion_forum)
        self.assertEqual(question.user, self.user)

    def test_update_discussion_forum_question(self):
        new_content = 'Updated question'
        UserService.update_discussion_forum_question(self.question.id, {'content': new_content})
        updated_question = DiscussionForumQuestion.objects.get(id=self.question.id)
        self.assertEqual(updated_question.content, new_content)

    def test_get_discussion_forum_question(self):
        question_data = UserService.get_discussion_forum_question(self.question.id)
        self.assertEqual(question_data['content'], self.question.content)

    def test_delete_discussion_forum_question(self):
        UserService.delete_discussion_forum_question(self.question.id)
        with self.assertRaises(DiscussionForumQuestion.DoesNotExist):
            DiscussionForumQuestion.objects.get(id=self.question.id)

    def test_create_discussion_forum_answer(self):
        answer_data = UserService.create_discussion_forum_answer(self.answer_data)
        answer = DiscussionForumAnswer.objects.get(id=answer_data['id'])
        self.assertEqual(answer_data['content'], answer.content)
        self.assertEqual(answer.question, self.question)
        self.assertEqual(answer.user, self.user)

    def test_update_discussion_forum_answer(self):
        new_content = 'Updated answer'
        UserService.update_discussion_forum_answer(self.answer.id, {'content': new_content})
        updated_answer = DiscussionForumAnswer.objects.get(id=self.answer.id)
        self.assertEqual(updated_answer.content, new_content)

    def test_get_discussion_forum_answer(self):
        answer_data = UserService.get_discussion_forum_answer(self.answer.id)
        self.assertEqual(answer_data['content'], self.answer.content)

    def test_delete_discussion_forum_answer(self):
        UserService.delete_discussion_forum_answer(self.answer.id)
        with self.assertRaises(DiscussionForumAnswer.DoesNotExist):
            DiscussionForumAnswer.objects.get(id=self.answer.id)

    def test_get_all_announcements(self):
        announcements = UserService.get_all_announcements()
        self.assertIn(self.announcement, announcements)

    def test_get_all_discussion_forums(self):
        forums = UserService.get_all_discussion_forums()
        self.assertIn(self.discussion_forum, forums)

    def test_get_answers_by_question_id(self):
        answers = UserService.get_answers_by_question_id(self.question.id)
        self.assertIn(self.answer, answers)

    def test_get_all_employee_concerns(self):
        concerns = UserService.get_all_employee_concerns()
        self.assertIn(self.employee_concern, concerns)

    def test_get_employee_concerns_by_user_id(self):
        concerns = UserService.get_employee_concerns_by_user_id(self.user.id)
        self.assertIn(self.employee_concern, concerns)

    def test_get_all_users(self):
        users = UserService.get_all_users()
        self.assertIn(self.user, users)