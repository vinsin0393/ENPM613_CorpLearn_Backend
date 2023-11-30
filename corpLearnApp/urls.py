from django.urls import path

from corpLearnApp.controllers import (create_user, get_user, update_user, login, delete_user, add_role, create_course,
                                      update_course, get_course, delete_course, get_all_courses, create_employee_course,
                                      update_employee_course,
                                      get_employee_course, get_employee_courses_by_user, delete_employee_course,
                                      create_announcement, update_announcement,
                                      get_announcement, delete_announcement, create_discussion_forum,
                                      update_discussion_forum, get_discussion_forum,
                                      delete_discussion_forum, create_employee_concern, update_employee_concern,
                                      get_employee_concern,
                                      delete_employee_concern, create_discussion_forum_question,
                                      update_discussion_forum_question,
                                      get_discussion_forum_question, delete_discussion_forum_question,
                                      create_discussion_forum_answer,
                                      update_discussion_forum_answer, get_discussion_forum_answer,
                                      delete_discussion_forum_answer, get_all_announcements,
                                      get_all_discussion_forums, get_discussion_forum_answers,
                                      get_all_employee_concerns, get_employee_concerns_by_user,
                                      get_all_users, create_training_document, update_training_document,
                                      get_training_document, delete_training_document, get_modules_by_course,
                                      get_modules_by_document, create_module, update_module, get_module, delete_module,
                                      upload_document, download_training_document)

urlpatterns = [
# URL patterns for Users
    path('login', login, name='login'),
    path('users/create', create_user, name='create_user'),
    path('users/<int:user_id>', get_user, name='get_user'),
    path('users/update/<int:user_id>', update_user, name='update_user'),
    path('users/delete/<int:user_id>', delete_user, name='delete_user'),
    path('users/roles/add', add_role, name='add_role'),
    path('users/all', get_all_users, name='get_all_users'),

# URL patterns for Announcements
    path('users/announcements/create', create_announcement, name='create_announcement'),
    path('users/announcements/update/<int:id>', update_announcement, name='update_announcement'),
    path('users/announcements/<int:id>', get_announcement, name='get_announcement'),
    path('users/announcements/delete/<int:id>', delete_announcement, name='delete_announcement'),
    path('users/announcements/all', get_all_announcements, name='get_all_announcements'),



# URL patterns for Employee Concerns
    path('users/employee-concerns/create', create_employee_concern, name='create_employee_concern'),
    path('users/employee-concerns/update/<int:id>', update_employee_concern, name='update_employee_concern'),
    path('users/employee-concerns/<int:id>', get_employee_concern, name='get_employee_concern'),
    path('users/employee-concerns/delete/<int:id>', delete_employee_concern, name='delete_employee_concern'),
    path('users/employee-concerns/all', get_all_employee_concerns, name='get_all_employee_concerns'),
    path('users/employee-concerns/user/<int:user_id>', get_employee_concerns_by_user, name='get_employee_concerns_by_user'),

# URL patterns for Discussion forums
    path('users/discussion-forums/create', create_discussion_forum, name='create_discussion_forum'),
    path('users/discussion-forums/update/<int:id>', update_discussion_forum, name='update_discussion_forum'),
    path('users/discussion-forums/<str:course_id>', get_discussion_forum, name='get_discussion_forum'),
    path('users/discussion-forums/delete/<int:id>', delete_discussion_forum, name='delete_discussion_forum'),
    path('users/discussion-forums/all', get_all_discussion_forums, name='get_all_discussion_forums'),

# URL patterns for Discussion forums Questions
    path('users/discussion-forum-questions/create', create_discussion_forum_question, name='create_discussion_forum_question'),
    path('users/discussion-forum-questions/update/<int:id>', update_discussion_forum_question, name='update_discussion_forum_question'),
    path('users/discussion-forum-questions/<int:id>', get_discussion_forum_question, name='get_discussion_forum_question'),
    path('users/discussion-forum-questions/delete/<int:id>', delete_discussion_forum_question, name='delete_discussion_forum_question'),

# URL patterns for Discussion forums Answers
    path('users/discussion-forum-answers/create', create_discussion_forum_answer, name='create_discussion_forum_answer'),
    path('users/discussion-forum-answers/update/<int:id>', update_discussion_forum_answer, name='update_discussion_forum_answer'),
    path('users/discussion-forum-answers/<int:id>', get_discussion_forum_answer, name='get_discussion_forum_answer'),
    path('users/discussion-forum-answers/delete/<int:id>', delete_discussion_forum_answer, name='delete_discussion_forum_answer'),
    path('users/discussion-forum-answers/question/<int:question_id>', get_discussion_forum_answers, name='get_discussion_forum_answers'),

# URL patterns for Course
    path('courses/create', create_course, name='create_course'),
    path('courses/update/<str:code>', update_course, name='update_course'),
    path('courses/<str:code>', get_course, name='get_course'),
    path('courses/delete/<str:code>', delete_course, name='delete_course'),
    path('courses', get_all_courses, name='get_all_courses'),

# URL patterns for EmployeeCourse
    path('courses/employee-courses/create', create_employee_course, name='create_employee_course'),
    path('courses/employee-courses/update/<int:id>', update_employee_course, name='update_employee_course'),
    path('courses/employee-courses/<int:id>', get_employee_course, name='get_employee_course'),
    path('courses/employee-courses/delete/<int:id>', delete_employee_course, name='delete_employee_course'),
    path('courses/employee-courses/user/<int:employee_id>', get_employee_courses_by_user, name='get_employee_courses_by_user'),

# URL patterns for training documents
    path('documents/training-documents/create', create_training_document, name='create_training_document'),
    path('documents/training-documents/update/<int:id>', update_training_document, name='update_training_document'),
    path('documents/training-documents/<int:id>', get_training_document, name='get_training_document'),
    path('documents/training-documents/delete/<int:id>', delete_training_document, name='delete_training_document'),

# URL patterns for training modules
    path('documents/modules/<str:course_id>/modules', get_modules_by_course, name='get_modules_by_course'),
    path('documents/modules/<int:document_id>/modules', get_modules_by_document, name='get_modules_by_document'),
    path('documents/modules/create', create_module, name='create_module'),
    path('documents/modules/update/<int:id>', update_module, name='update_module'),
    path('documents/modules/<int:id>', get_module, name='get_module'),
    path('documents/modules/delete/<int:id>', delete_module, name='delete_module'),

# URL patterns for upload documents
    path('documents/upload', upload_document, name='upload_document'),
    path('documents/download/<int:module_id>', download_training_document, name='download_training_document'),
]
