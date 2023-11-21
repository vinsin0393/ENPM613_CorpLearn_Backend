from django.test import TestCase
from corpLearnApp.models import Course, EmployeeCourse, User
from corpLearnApp.services.course import CourseService


class CourseServiceTestCase(TestCase):

    def setUp(self):
        self.admin_user = User.objects.create_user(id =1, email='admin@example.com', name='Admin User', password='admin@123')
        self.course = Course.objects.create(code='ENPM613', admin=self.admin_user, time_to_complete=30)
        self.employee = User.objects.create_user(email='employee@example.com', name='Employee User', password='employee@123')
        self.employee_course_data = {
            'employee': self.employee.id,
            'course': self.course.code
        }
        self.employee_course = EmployeeCourse.objects.create(employee=self.employee, course=self.course, status='InProgress')

    def test_create_course(self):
        course_data = {
            'code': 'ENPM614',
            'admin': self.admin_user.id,
            'time_to_complete': 15
        }
        result = CourseService.create_course(course_data)
        new_course = Course.objects.get(code=course_data['code'])
        self.assertEqual(result['code'], new_course.code)

    def test_update_course(self):
        updated_data = {'time_to_complete': 20}
        CourseService.update_course(self.course.code, updated_data)
        updated_course = Course.objects.get(code=self.course.code)
        self.assertEqual(updated_course.time_to_complete, updated_data['time_to_complete'])

    def test_get_course(self):
        result = CourseService.get_course(self.course.code)
        self.assertEqual(result['time_to_complete'], self.course.time_to_complete)

    def test_delete_course(self):
        CourseService.delete_course(self.course.code)
        with self.assertRaises(Course.DoesNotExist):
            Course.objects.get(code=self.course.code)

    def test_create_employee_course(self):
        course_data = {
            'code': 'ENPM614',
            'admin': self.admin_user.id,
            'time_to_complete': 15
        }
        new_course = Course.objects.create(code='ENPM617', admin=self.admin_user, time_to_complete=15)
        new_employee_course_data = {
            'employee': self.employee.id,
            'course': new_course.code
        }
        result = CourseService.create_employee_course(new_employee_course_data)
        new_employee_course = EmployeeCourse.objects.get(id=result['id'])
        self.assertEqual(result['status'], new_employee_course.status)

    def test_update_employee_course(self):
        updated_data = {'status': 'Completed'}
        CourseService.update_employee_course(self.employee_course.id, updated_data)
        updated_employee_course = EmployeeCourse.objects.get(id=self.employee_course.id)
        self.assertEqual(updated_employee_course.status, updated_data['status'])

    def test_get_employee_course(self):
        result = CourseService.get_employee_course(self.employee_course.id)
        self.assertEqual(result['status'], self.employee_course.status)

    def test_delete_employee_course(self):
        CourseService.delete_employee_course(self.employee_course.id)
        with self.assertRaises(EmployeeCourse.DoesNotExist):
            EmployeeCourse.objects.get(id=self.employee_course.id)

    def test_get_all_courses(self):
        courses = CourseService.get_all_courses()
        self.assertIn(self.course, courses)

    def test_get_courses_by_employee_id(self):
        courses = CourseService.get_courses_by_employee_id(self.employee.id)
        self.assertIn(self.course, [ec.course for ec in courses])

    def tearDown(self):
        Course.objects.all().delete()
        User.objects.all().delete()
        EmployeeCourse.objects.all().delete()