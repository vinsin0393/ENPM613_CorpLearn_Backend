from corpLearnApp.models import Course, EmployeeCourse, User
from corpLearnApp.repositories import CourseRepository, EmployeeCourseRepository, UserRepository
from corpLearnApp.serializers import CourseSerializer, EmployeeCourseSerializer
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
import json

from corpLearnApp.services.service_exception_log_handler.exception_log_handler import exception_log_handler


class CourseService:
    @staticmethod
    @exception_log_handler
    def create_course(data):
        """ Creates a new course with the provided data. """
        admin_id = data.pop('admin', None)
        UserRepository(User)
        try:
            admin = UserRepository(User).get_user(admin_id)
        except User.DoesNotExist:
            raise ObjectDoesNotExist(f"No User with id {admin_id} exists.")
        data['admin'] = admin
        repository = CourseRepository(Course)
        course = repository.create_course(**data)
        return CourseSerializer(course).data

    @staticmethod
    @exception_log_handler
    def update_course(code, data):
        """ Updates an existing course identified by 'code'. """
        repository = CourseRepository(Course, code)
        course = repository.update_course_data(**data)
        return CourseSerializer(course).data

    @staticmethod
    @exception_log_handler
    def get_course(code):
        """ Retrieves a specific course based on its 'code'. """
        repository = CourseRepository(Course)
        course = repository.get_course(code)
        return CourseSerializer(course).data

    @staticmethod
    @exception_log_handler
    def delete_course(code):
        """ Deletes a course identified by 'code'. """
        repository = CourseRepository(Course)
        repository.delete_course(code)
        return {'message': 'Course deleted successfully'}

    @staticmethod
    @exception_log_handler
    def create_employee_course(data):
        """ Creates a course enrollment for an employee. """
        employee_id = data.pop('employee', None)
        course_id = data.pop('course', None)
        try:
            employee = UserRepository(User).get_user(employee_id)
            course = CourseRepository(Course).get_course(course_id)
            if EmployeeCourse.objects.filter(employee=employee, course=course).exists():
                raise ValidationError(f"EmployeeCourse with user {employee_id} and course {course_id} already exists.")
        except User.DoesNotExist:
            raise ObjectDoesNotExist(f"No User with id {employee} exists.")
        data['employee'] = employee
        data['course'] = course
        data["status"] = "Start"
        data["start_date"] = datetime.now().date()
        data["end_date"] = datetime.now().date()
        data['deadline'] = datetime.now().date() + timedelta(days=course.time_to_complete)
        data["data"] = json.dumps(data["data"])
        repository = EmployeeCourseRepository(EmployeeCourse)
        employee_course = repository.create_employee_course(**data)
        return EmployeeCourseSerializer(employee_course).data

    @staticmethod
    @exception_log_handler
    def update_employee_course(id, data):
        """ Updates an existing employee course enrollment identified by 'id'. """
        repository = EmployeeCourseRepository(EmployeeCourse)
        if "status" in data and data["status"] == "InProgress":
            data["start_date"] = datetime.now().date()
        if "status" in data and data["status"] == "Completed":
            data["end_date"] = datetime.now().date()
        employee_course = repository.update_employee_course(id, **data)
        return EmployeeCourseSerializer(employee_course).data

    @staticmethod
    @exception_log_handler
    def get_employee_course(id):
        """ Retrieves a specific employee course enrollment based on its 'id'. """
        repository = EmployeeCourseRepository(EmployeeCourse)
        employee_course = repository.get_employee_course(id)
        return EmployeeCourseSerializer(employee_course).data

    @staticmethod
    @exception_log_handler
    def delete_employee_course(id):
        """ Deletes an employee course enrollment identified by 'id'. """
        repository = EmployeeCourseRepository(EmployeeCourse)
        repository.delete_employee_course(id)
        return {'message': 'EmployeeCourse deleted successfully'}

    @staticmethod
    @exception_log_handler
    def get_all_courses():
        """ Retrieves all courses available in the system. """
        repo = CourseRepository(Course)
        return repo.get_all_course()

    @staticmethod
    @exception_log_handler
    def get_courses_by_employee_id(employee_id):
        """ Retrieves all courses enrolled by a specific employee identified by 'employee_id'. """
        repo = EmployeeCourseRepository(EmployeeCourse)
        return repo.get_employee_course_by_user_id(employee_id)