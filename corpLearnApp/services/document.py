from corpLearnApp.models import TrainingDocument, Module
from corpLearnApp.repositories import ModuleRepository
from corpLearnApp.repositories.training_document import TrainingDocumentRepository
from corpLearnApp.serializers import ModuleSerializer
from corpLearnApp.serializers.training_document import TrainingDocumentSerializer
from django.core.files.storage import default_storage
import os

from corpLearnApp.services.service_exception_log_handler.exception_log_handler import exception_log_handler


class DocumentService:
    @staticmethod
    @exception_log_handler
    def create_document(data):
        """ Creates a new training document in the system. """
        repository = TrainingDocumentRepository(TrainingDocument)
        document = repository.create_training_document(**data)
        return TrainingDocumentSerializer(document).data

    @staticmethod
    @exception_log_handler
    def update_document(id, data):
        """ Updates an existing training document identified by 'id'. """
        repository = TrainingDocumentRepository(TrainingDocument)
        document = repository.update_training_document(id, **data)
        return TrainingDocumentSerializer(document).data

    @staticmethod
    @exception_log_handler
    def get_document(id):
        """ Retrieves a specific training document based on its 'id'. """
        repository = TrainingDocumentRepository(TrainingDocument)
        document = repository.get_training_document(id)
        return TrainingDocumentSerializer(document).data

    @staticmethod
    @exception_log_handler
    def delete_document(id):
        """ Deletes a training document identified by 'id'. """
        repository = TrainingDocumentRepository(TrainingDocument)
        repository.delete_training_document(id)
        return {'message': 'Document deleted successfully'}

    @staticmethod
    @exception_log_handler
    def get_modules_by_course_id(course_id):
        """ Retrieves all modules associated with a specific course identified by 'course_id'. """
        repo = ModuleRepository(Module)
        return repo.get_module_by_course_id(course_id)

    @staticmethod
    @exception_log_handler
    def get_modules_by_document_id(document_id):
        """ Retrieves all modules associated with a specific document identified by 'document_id'. """
        repo = ModuleRepository(Module)
        return repo.get_module_by_document_id(document_id)

    @staticmethod
    @exception_log_handler
    def create_module(data):
        """ Creates a new module in the system. """
        repository = ModuleRepository(Module)
        module = repository.create_module(**data)
        return ModuleSerializer(module).data

    @staticmethod
    @exception_log_handler
    def update_module(id, data):
        """ Updates an existing module identified by 'id'. """
        repository = ModuleRepository(Module)
        module = repository.update_module(id, **data)
        return ModuleSerializer(module).data

    @staticmethod
    @exception_log_handler
    def get_module(id):
        """ Retrieves a specific module based on its 'id'. """
        repository = ModuleRepository(Module)
        module = repository.get_module(id)
        return ModuleSerializer(module).data

    @staticmethod
    @exception_log_handler
    def delete_module(id):
        """ Deletes a module identified by 'id'. """
        repository = ModuleRepository(Module)
        repository.delete_module(id)
        return {'message': 'Module deleted successfully'}

    @staticmethod
    @exception_log_handler
    def save_training_document(file, file_name):
        """ Saves a training document file and updates the document's path in the system. """
        file_path = os.path.join('training_documents', file_name)
        document_data = {'document_path': file_path}
        document = DocumentService.create_document(document_data)
        file_path = os.path.join('training_documents',  f"{document['id']}_{file_name}")
        path = default_storage.save(file_path, file)
        repository = TrainingDocumentRepository(TrainingDocument)
        training_document=  repository.update_training_document (document['id'], document_path=path)
        return TrainingDocumentSerializer(training_document)

    @staticmethod
    @exception_log_handler
    def get_saved_training_document(module_id):
        """ Retrieves the file content and name of a training document associated with a specific module. """
        module = DocumentService.get_module(id=module_id)
        training_document = DocumentService.get_document(id=module['training_document'])
        document_path = training_document['document_path']
        if default_storage.exists(document_path):
            with default_storage.open(document_path, 'rb') as document_file:
                file_content = document_file.read()
                file_name = document_path.split('/')[-1]
                return file_content, file_name
        else:
            raise FileNotFoundError("The file does not exist.")



