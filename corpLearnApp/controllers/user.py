from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError

from corpLearnApp.controllers.admin_decorator.admin_only import admin_only
from corpLearnApp.controllers.controller_excpetion_log_handler.exception_log_handler import exception_log_handler

import logging

logger = logging.getLogger(__name__)

from corpLearnApp.serializers import (
    AnnouncementSerializer,
    DiscussionForumSerializer,
    DiscussionForumQuestionSerializer,
    DiscussionForumAnswerSerializer,
    EmployeeConcernSerializer,
    RoleSerializer,
    UserSerializer
)
from corpLearnApp.services import UserService


@swagger_auto_schema(method='post', request_body=UserSerializer, responses={201: UserSerializer})
@api_view(['POST'])
@exception_log_handler
def login(request):
    """ Authenticates a user and provides JWT tokens upon successful login. """
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(email=email, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        update_last_login(None, user)
        response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'expires_in': refresh.access_token.payload['exp'],
            'refresh_expires_in': refresh.payload['exp'],
            'user': {
                'id': user.id,
                'email': user.email,
                'name': user.name,
                'role': user.role.id,
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@swagger_auto_schema(method='post', request_body=UserSerializer, responses={201: UserSerializer})
@api_view(["POST"])
@exception_log_handler
def create_user(request):
    """ Handles the creation of a new user in the system. """
    user_data = UserService.add_user(request.data)
    return Response(user_data, status=status.HTTP_201_CREATED)


@swagger_auto_schema(method='get', responses={200: UserSerializer})
@api_view(["GET"])
@exception_log_handler
def get_user(request, user_id):
    """ Retrieves specific user details based on the provided user ID. """
    try:
        # if not request.user.role.allow_edit() and not request.user.id == int(user_id):
        #     logger.error(f'User {request.user.id} does not have permission to access user {user_id}')
        #     return Response({'error': 'You do not have permission for this action'}, status=status.HTTP_403_FORBIDDEN)

        user_data = UserService.get_user(user_id)
        return Response(user_data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        logger.error(f'User not found: {e}')
        raise

@swagger_auto_schema(method='put', request_body=UserSerializer, responses={200: UserSerializer})
@api_view(["PUT"])
@exception_log_handler
def update_user(request, user_id):
    """ Updates user information for the specified user ID. """
    try:
        user_data = UserService.update_user(user_id, request.data)
        return Response(user_data, status=status.HTTP_200_OK)
    except ValidationError as e:
        logger.error(f'Validation error while updating user {user_id}: {e}')
        raise

@swagger_auto_schema(method='delete', responses={204: 'User deleted successfully', 404: 'User not found'})
@api_view(["DELETE"])
@exception_log_handler
def delete_user(request, user_id):
    """ Removes a user from the system based on the provided user ID. """
    UserService.delete_user(user_id)
    return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='post', request_body=RoleSerializer, responses={201: RoleSerializer})
@api_view(['POST'])
@exception_log_handler
def add_role(request):
    """ Adds a new role to the system. """
    role_data = UserService.add_default_role()
    serializer = RoleSerializer(role_data)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@swagger_auto_schema(method='post', request_body=AnnouncementSerializer, responses={201: AnnouncementSerializer})
@api_view(['POST'])
@exception_log_handler
def create_announcement(request):
    """ Manages the creation of a new announcement. """
    data = UserService.create_announcement(request.data)
    return Response(data)

@swagger_auto_schema(method='put', request_body=AnnouncementSerializer, responses={200: AnnouncementSerializer})
@api_view(['PUT'])
@exception_log_handler
def update_announcement(request, id):
    """ Updates an existing announcement based on its ID. """
    data = UserService.update_announcement(id, request.data)
    return Response(data)

@swagger_auto_schema(method='get', responses={200: AnnouncementSerializer})
@api_view(['GET'])
@exception_log_handler
def get_announcement(request, id):
    """ Retrieves a specific announcement based on its ID. """
    data = UserService.get_announcement(id)
    return Response(data)

@swagger_auto_schema(method='delete', responses={204: 'User deleted successfully', 404: 'User not found'})
@api_view(['DELETE'])
@exception_log_handler
def delete_announcement(request, id):
    """ Deletes an announcement based on its ID. """
    data = UserService.delete_announcement(id)
    return Response(data)

@swagger_auto_schema(method='post', request_body=DiscussionForumSerializer, responses={201: DiscussionForumSerializer})
@api_view(['POST'])
@exception_log_handler
def create_discussion_forum(request):
    """ Handles the creation of a new discussion forum. """
    data = UserService.create_discussion_forum(request.data)
    return Response(data)

@swagger_auto_schema(method='put', request_body=DiscussionForumSerializer, responses={200: DiscussionForumSerializer})
@api_view(['PUT'])
@exception_log_handler
def update_discussion_forum(request, id):
    """  Updates an existing discussion forum based on its ID"""
    data = UserService.update_discussion_forum(id, request.data)
    return Response(data)

@swagger_auto_schema(method='get', responses={200: DiscussionForumSerializer})
@api_view(['GET'])
@exception_log_handler
def get_discussion_forum(request, course_id):
    """   Fetches a specific discussion forum question based on its  """
    data = UserService.get_discussion_forum(course_id)
    return Response(data)

@swagger_auto_schema(method='delete', responses={204: 'User deleted successfully', 404: 'User not found'})
@api_view(['DELETE'])
@exception_log_handler
def delete_discussion_forum(request, id):
    """ Removes a discussion forum based on its ID."""
    data = UserService.delete_discussion_forum(id)
    return Response(data)


@swagger_auto_schema(method='post', request_body=EmployeeConcernSerializer, responses={201: EmployeeConcernSerializer})
@api_view(['POST'])
@exception_log_handler
def create_employee_concern(request):
    """ Manages the creation of an employee concern"""
    data = UserService.create_employee_concern(request.data)
    return Response(data)

@swagger_auto_schema(method='put', request_body=EmployeeConcernSerializer, responses={200: EmployeeConcernSerializer})
@api_view(['PUT'])
@exception_log_handler
def update_employee_concern(request, id):
    """Updates an existing employee concern based on its ID"""
    data = UserService.update_employee_concern(id, request.data)
    return Response(data)

@swagger_auto_schema(method='get', responses={200: EmployeeConcernSerializer})
@api_view(['GET'])
@exception_log_handler
def get_employee_concern(request, id):
    """Retrieves a specific employee concern based on its ID"""
    data = UserService.get_employee_concern(id)
    return Response(data)

@swagger_auto_schema(method='delete', responses={204: 'User deleted successfully', 404: 'User not found'})
@api_view(['DELETE'])
@exception_log_handler
def delete_employee_concern(request, id):
    """ Deletes an employee concern based on its ID"""
    data = UserService.delete_employee_concern(id)
    return Response(data)


@swagger_auto_schema(method='post', request_body=DiscussionForumQuestionSerializer, responses={201: DiscussionForumQuestionSerializer})
@api_view(['POST'])
@exception_log_handler
def create_discussion_forum_question(request):
    """  Handles the creation of a new discussion forum question"""
    data = UserService.create_discussion_forum_question(request.data)
    return Response(data)

@swagger_auto_schema(method='put', request_body=DiscussionForumQuestionSerializer, responses={200: DiscussionForumQuestionSerializer})
@api_view(['PUT'])
@exception_log_handler
def update_discussion_forum_question(request, id):
    """  Updates a discussion forum question based on its ID"""
    data = UserService.update_discussion_forum_question(id, request.data)
    return Response(data)


@swagger_auto_schema(method='get', responses={200: DiscussionForumQuestionSerializer})
@api_view(['GET'])
@exception_log_handler
def get_discussion_forum_question(request, id):
    """ Fetches a specific discussion forum question based on its ID"""
    data = UserService.get_discussion_forum_question(id)
    return Response(data)


@swagger_auto_schema(method='delete', responses={204: 'User deleted successfully', 404: 'User not found'})
@api_view(['DELETE'])
@exception_log_handler
def delete_discussion_forum_question(request, id):
    """ Deletes a discussion forum question based on its ID"""
    data = UserService.delete_discussion_forum_question(id)
    return Response(data)


@swagger_auto_schema(method='post', request_body=DiscussionForumAnswerSerializer, responses={201: DiscussionForumAnswerSerializer})
@api_view(['POST'])
@exception_log_handler
def create_discussion_forum_answer(request):
    """ Manages the creation of a discussion forum answer"""
    data = UserService.create_discussion_forum_answer(request.data)
    return Response(data)


@swagger_auto_schema(method='put', request_body=DiscussionForumAnswerSerializer, responses={200: DiscussionForumAnswerSerializer})
@api_view(['PUT'])
@exception_log_handler
def update_discussion_forum_answer(request, id):
    """ Updates a discussion forum answer based on its ID"""
    data = UserService.update_discussion_forum_answer(id, request.data)
    return Response(data)


@swagger_auto_schema(method='get', responses={200: DiscussionForumAnswerSerializer})
@api_view(['GET'])
@exception_log_handler
def get_discussion_forum_answer(request, id):
    """ Retrieves a specific discussion forum answer based on its ID."""
    data = UserService.get_discussion_forum_answer(id)
    return Response(data)


@swagger_auto_schema(method='delete', responses={204: 'User deleted successfully', 404: 'User not found'})
@api_view(['DELETE'])
@exception_log_handler
def delete_discussion_forum_answer(request, id):
    """Removes a discussion forum answer based on its ID"""
    data = UserService.delete_discussion_forum_answer(id)
    return Response(data)


@swagger_auto_schema(method='get', responses={200: AnnouncementSerializer(many=True)})
@api_view(['GET'])
@exception_log_handler
def get_all_announcements(request):
    """Fetches all announcements available in the system"""
    announcements = UserService.get_all_announcements()
    serializer = AnnouncementSerializer(announcements, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='get', responses={200: DiscussionForumSerializer(many=True)})
@api_view(['GET'])
@exception_log_handler
def get_all_discussion_forums(request):
    """Fetches all announcements available in the system"""
    forums = UserService.get_all_discussion_forums()
    serializer = DiscussionForumSerializer(forums, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='get', responses={200: DiscussionForumAnswerSerializer(many=True)})
@api_view(['GET'])
@exception_log_handler
def get_discussion_forum_answers(request, question_id):
    """Retrieves all discussion forums available"""
    answers = UserService.get_answers_by_question_id(question_id)
    serializer = DiscussionForumAnswerSerializer(answers, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='get', responses={200: EmployeeConcernSerializer(many=True)})
@api_view(['GET'])
@exception_log_handler
def get_all_employee_concerns(request):
    """Fetches all answers for a specific discussion forum question"""
    concerns = UserService.get_all_employee_concerns()
    serializer = EmployeeConcernSerializer(concerns, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='get', responses={200: EmployeeConcernSerializer(many=True)})
@api_view(['GET'])
def get_employee_concerns_by_user(request, user_id):
    """ Fetches employee concerns associated with a specific user"""
    concerns = UserService.get_employee_concerns_by_user_id(user_id)
    serializer = EmployeeConcernSerializer(concerns, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='get', responses={200: UserSerializer(many=True)})
@api_view(['GET'])
def get_all_users(request):
    """Retrieves all users registered in the system"""
    users = UserService.get_all_users()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)