from django.test import TestCase
from corpLearnApp.models import TrainingDocument, Course, Module, User
from corpLearnApp.services.document import DocumentService
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import os

class DocumentServiceTestCase(TestCase):

    def setUp(self):
        self.admin_user = User.objects.create_user(email='admin@example.com', name='Admin User', password='admin@123')
        self.course = Course.objects.create(code='ENPM613', time_to_complete=10, admin=self.admin_user)
        self.document_path = 'path/to/document/1'
        self.training_document = TrainingDocument.objects.create(document_path=self.document_path)
        self.module_data = {
            'course': self.course,
            'content': 'Module Content',
            'training_document': self.training_document
        }
        self.module = Module.objects.create(**self.module_data)

        self.file_name = 'test_document.txt'
        self.file_content = ContentFile(b"Dummy file content.")
        self.file_path = os.path.join('training_documents', self.file_name)

    def test_update_document(self):
        new_data = {'document_path': 'new/path/to/document'}
        DocumentService.update_document(self.training_document.id, new_data)
        updated_document = TrainingDocument.objects.get(id=self.training_document.id)
        self.assertEqual(updated_document.document_path, new_data['document_path'])

    def test_get_document(self):
        result = DocumentService.get_document(self.training_document.id)
        self.assertEqual(result['document_path'], self.training_document.document_path)

    def test_delete_document(self):
        DocumentService.delete_document(self.training_document.id)
        with self.assertRaises(TrainingDocument.DoesNotExist):
            TrainingDocument.objects.get(id=self.training_document.id)

    def test_get_modules_by_course_id(self):
        modules = DocumentService.get_modules_by_course_id(self.course.code)
        self.assertIn(self.module, modules)

    def test_get_modules_by_document_id(self):
        modules = DocumentService.get_modules_by_document_id(self.training_document.id)
        self.assertIn(self.module, modules)

    def test_create_module(self):
        module = DocumentService.create_module(self.module_data)
        new_module = Module.objects.get(id=module['id'])
        self.assertEqual(module['content'], new_module.content)

    def test_update_module(self):
        updated_data = {'content': 'Updated Module Content'}
        DocumentService.update_module(self.module.id, updated_data)
        updated_module = Module.objects.get(id=self.module.id)
        self.assertEqual(updated_module.content, updated_data['content'])

    def test_get_module(self):
        module = DocumentService.get_module(self.module.id)
        self.assertEqual(module['content'], self.module.content)

    def test_delete_module(self):
        DocumentService.delete_module(self.module.id)
        with self.assertRaises(Module.DoesNotExist):
            Module.objects.get(id=self.module.id)

    def test_save_training_document(self):
        serializer = DocumentService.save_training_document(self.file_content, self.file_name)
        document_id = serializer.data['id']
        training_document = TrainingDocument.objects.get(id=document_id)
        self.assertTrue(default_storage.exists(training_document.document_path))
        with default_storage.open(training_document.document_path) as file:
            self.assertEqual(file.read(), b"Dummy file content.")
        default_storage.delete(training_document.document_path)
        training_document.delete()

    def test_get_saved_training_document(self):
        default_storage.save(self.training_document.document_path, ContentFile(self.file_content.read()))
        file_content, file_name = DocumentService.get_saved_training_document(self.module.id)
        self.assertEqual(file_name, os.path.basename(self.training_document.document_path))
        if default_storage.exists(self.training_document.document_path):
            default_storage.delete(self.training_document.document_path)

    def tearDown(self):
        if default_storage.exists(self.file_path):
            default_storage.delete(self.file_path)

