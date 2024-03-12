from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from el.models import Course, Topic, CourseMaterial
import shutil
import tempfile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.core.files.base import ContentFile

User = get_user_model()

class CourseManagementTests(TestCase):
    
    def setUp(self):
        # Temporarily override MEDIA_ROOT
        self.temp_media_root = tempfile.mkdtemp(dir=settings.BASE_DIR)
        settings.MEDIA_ROOT = self.temp_media_root

        # Create a teacher and a student user
        self.teacher_user = User.objects.create_user(username='teacher', email='teacher@example.com', password='123', user_type='teacher')
        self.student_user = User.objects.create_user(username='student', email='student@example.com', password='123', user_type='student')
        
        # Log in as the teacher user
        self.client.login(username='teacher', password='123')
        
        # Create a course and a topic under the teacher
        self.course = Course.objects.create(title="Test Course", description="Test Description", subject="Test Subject", teacher=self.teacher_user)
        self.topic = Topic.objects.create(name="Test Topic", description="Test Topic Description", course=self.course)

        # Create a course material
        self.material_file = SimpleUploadedFile("test_file.txt", b"this is a test file")
        self.material = CourseMaterial.objects.create(course=self.course, topic=self.topic, title='Test Material', file=self.material_file)

    def test_delete_material_by_teacher(self):
        self.assertEqual(CourseMaterial.objects.count(), 1)  # Ensure the material exists before deletion
        response = self.client.post(reverse('delete_file'), {'course_id': self.course.id, 'topic_id': self.topic.id, 'material_id': self.material.id})
        self.assertEqual(response.status_code, 302)  # Redirect expected after successful deletion
        self.assertEqual(CourseMaterial.objects.count(), 0)  # Verify the material has been deleted

    def tearDown(self):
        # Cleanup the temporary MEDIA_ROOT directory
        shutil.rmtree(self.temp_media_root, ignore_errors=True)
        super().tearDown()
