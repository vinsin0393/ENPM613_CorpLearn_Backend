from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from corpLearnApp.controllers.admin_decorator.admin_only import admin_only
from corpLearnApp.controllers.controller_excpetion_log_handler.exception_log_handler import exception_log_handler
from corpLearnApp.serializers import CourseSerializer, EmployeeCourseSerializer
from corpLearnApp.services.course import CourseService

@swagger_auto_schema(method='post', request_body=CourseSerializer, responses={201: CourseSerializer})
@api_view(['POST'])
@exception_log_handler
@admin_only
def create_course(request):
    """ Creates a new course in the system. Requires admin privileges. """
    data = CourseService.create_course(request.data)
    return Response(data)

@swagger_auto_schema(method='put', request_body=CourseSerializer, responses={200: CourseSerializer})
@api_view(['PUT'])
@exception_log_handler
@admin_only
def update_course(request, code):
    """ Updates an existing course identified by 'code'. Requires admin privileges. """
    data = CourseService.update_course(code, request.data)
    return Response(data)

@swagger_auto_schema(method='get', responses={200: CourseSerializer})
@api_view(['GET'])
@exception_log_handler
def get_course(request, code):
    """ Retrieves a specific course based on its 'code'. """
    data = CourseService.get_course(code)
    return Response(data)

@swagger_auto_schema(method='delete', responses={204: 'User deleted successfully', 404: 'User not found'})
@api_view(['DELETE'])
@exception_log_handler
@admin_only
def delete_course(request, code):
    """ Deletes a course identified by 'code'. Requires admin privileges. """
    data = CourseService.delete_course(code)
    return Response(data)

@swagger_auto_schema(method='post', request_body=EmployeeCourseSerializer, responses={201: EmployeeCourseSerializer})
@api_view(['POST'])
@exception_log_handler
@admin_only
def create_employee_course(request):
    """ Creates a course enrollment for an employee. Requires admin privileges. """
    data = CourseService.create_employee_course(request.data)
    return Response(data)

@swagger_auto_schema(method='put', request_body=EmployeeCourseSerializer, responses={200: EmployeeCourseSerializer})
@api_view(['PUT'])
@exception_log_handler
def update_employee_course(request, id):
    """ Updates an existing employee course enrollment identified by 'id'. Requires admin privileges. """
    data = CourseService.update_employee_course(id, request.data)
    return Response(data)

@swagger_auto_schema(method='get', responses={200: EmployeeCourseSerializer})
@api_view(['GET'])
@exception_log_handler
def get_employee_course(request, id):
    """ Retrieves a specific employee course enrollment based on its 'id'. """
    data = CourseService.get_employee_course(id)
    return Response(data)

@swagger_auto_schema(method='delete', responses={204: 'User deleted successfully', 404: 'User not found'})
@api_view(['DELETE'])
@exception_log_handler
@admin_only
def delete_employee_course(request, id):
    """ Deletes an employee course enrollment identified by 'id'. Requires admin privileges. """
    data = CourseService.delete_employee_course(id)
    return Response(data)

@swagger_auto_schema(method='get', responses={200: CourseSerializer(many=True)})
@api_view(['GET'])
@exception_log_handler
def get_all_courses(request):
    """ Retrieves all courses available in the system. Requires admin privileges. """
    courses = CourseService.get_all_courses()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='get', responses={200: EmployeeCourseSerializer(many=True)})
@api_view(['GET'])
@exception_log_handler
def get_employee_courses_by_user(request, employee_id):
    """ Retrieves all courses enrolled by a specific employee identified by 'employee_id'. """
    employee_courses = CourseService.get_courses_by_employee_id(employee_id)
    serializer = EmployeeCourseSerializer(employee_courses, many=True)
    return Response(serializer.data)