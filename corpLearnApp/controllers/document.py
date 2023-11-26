from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

from drf_yasg.utils import swagger_auto_schema

from corpLearnApp.controllers.admin_decorator.admin_only import admin_only
from corpLearnApp.models import Course, TrainingDocument
from corpLearnApp.repositories import CourseRepository, TrainingDocumentRepository
from corpLearnApp.serializers import ModuleSerializer
from corpLearnApp.serializers.training_document import TrainingDocumentSerializer
from corpLearnApp.serializers.upload_document import UploadDocumentSerializer
from corpLearnApp.services import CourseService, UserService
from corpLearnApp.services.document import DocumentService
from corpLearnApp.controllers.controller_excpetion_log_handler.exception_log_handler import exception_log_handler

@swagger_auto_schema(method='post', request_body=TrainingDocumentSerializer, responses={201: TrainingDocumentSerializer})
@api_view(['POST'])
@exception_log_handler
@admin_only
def create_training_document(request):
    """ Creates a new training document in the system. Requires admin privileges. """
    data = DocumentService.create_document(request.data)
    return Response(data, status=status.HTTP_201_CREATED)

@swagger_auto_schema(method='put', request_body=TrainingDocumentSerializer, responses={200: TrainingDocumentSerializer})
@api_view(['PUT'])
@exception_log_handler
@admin_only
def update_training_document(request, id):
    """ Updates an existing training document identified by 'id'. Requires admin privileges. """
    data = DocumentService.update_document(id, request.data)
    return Response(data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='get', responses={200: TrainingDocumentSerializer})
@api_view(['GET'])
@exception_log_handler
def get_training_document(request, id):
    """ Retrieves a specific training document based on its 'id'. """
    data = DocumentService.get_document(id)
    return Response(data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='delete', responses={204: 'Document deleted successfully', 404: 'Document not found'})
@api_view(['DELETE'])
@exception_log_handler
@admin_only
def delete_training_document(request, id):
    """ Deletes a training document identified by 'id'. Requires admin privileges. """
    DocumentService.delete_document(id)
    return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='get', responses={200: ModuleSerializer(many=True)})
@api_view(['GET'])
def get_modules_by_course(request, course_id):
    """ Retrieves all modules associated with a specific course identified by 'course_id'. """
    modules = DocumentService.get_modules_by_course_id(course_id)
    serializer = ModuleSerializer(modules, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='get', responses={200: ModuleSerializer(many=True)})
@api_view(['GET'])
def get_modules_by_document(request, document_id):
    """ Retrieves all modules associated with a specific document identified by 'document_id'. """
    modules = DocumentService.get_modules_by_document_id(document_id)
    serializer = ModuleSerializer(modules, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=ModuleSerializer, responses={201: ModuleSerializer})
@api_view(['POST'])
@exception_log_handler
@admin_only
def create_module(request):
    """ Creates a new module in the system. Requires admin privileges. """
    data = DocumentService.create_module(request.data)
    return Response(data)

@swagger_auto_schema(method='put', request_body=ModuleSerializer, responses={200: ModuleSerializer})
@api_view(['PUT'])
@admin_only
@exception_log_handler
def update_module(request, id):
    """ Updates an existing module identified by 'id'. Requires admin privileges. """
    data = DocumentService.update_module(id, request.data)
    return Response(data)

@swagger_auto_schema(method='get', responses={200: ModuleSerializer})
@api_view(['GET'])
@admin_only
@exception_log_handler
def get_module(request, id):
    """ Retrieves a specific module based on its 'id'. Requires admin privileges. """
    data = DocumentService.get_module(id)
    return Response(data)

@swagger_auto_schema(method='delete', responses={204: 'User deleted successfully', 404: 'User not found'})
@api_view(['DELETE'])
@exception_log_handler
@admin_only
def delete_module(request, id):
    """ Deletes a module identified by 'id'. Requires admin privileges. """
    data = DocumentService.delete_module(id)
    return Response(data)

@swagger_auto_schema( method='post', request_body=UploadDocumentSerializer, responses={201: UploadDocumentSerializer})
@api_view(['POST'])
@exception_log_handler
@admin_only
def upload_document(request):
    """ Handles the uploading of a document and associating it with a course and module. Requires admin privileges. """
    file = request.FILES['file']
    course_id = request.data['course_id']
    content = request.data['content']
    training_document = DocumentService.save_training_document(file, f"{file.name}")
    training_document = TrainingDocumentRepository(TrainingDocument).get_training_document(id=training_document.data['id'])
    course = CourseRepository(Course).get_course(code=course_id)
    module = {
        'course': course,
        'content': content,
        'training_document': training_document
    }
    module = DocumentService.create_module(module)
    return Response({
        'training_document': TrainingDocumentSerializer(training_document),
        'module': module
    }, status=status.HTTP_201_CREATED)


@swagger_auto_schema( method='get', operation_description="Downloads a training document file associated with a specific module.")
@api_view(['GET'])
@exception_log_handler
def download_training_document(request, module_id):
    """ Allows downloading of a training document associated with a module identified by 'module_id'. """
    file_content, file_name = DocumentService.get_saved_training_document(module_id)
    response = HttpResponse(file_content, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response