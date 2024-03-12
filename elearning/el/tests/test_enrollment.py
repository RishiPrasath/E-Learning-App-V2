from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from el.models import Course, Enrollment

User = get_user_model()

class EnrollmentTests(TestCase):

    def setUp(self):
        # Create users
        self.teacher_user = User.objects.create_user(username='teacher', email='teacher@example.com', password='123', user_type='teacher')
        self.student_user_1 = User.objects.create_user(username='student1', email='student1@example.com', password='123', user_type='student')
        self.student_user_2 = User.objects.create_user(username='student2', email='student2@example.com', password='123', user_type='student')
        
        # Create a course by the teacher
        self.course = Course.objects.create(title="Test Course", description="Test Description", subject="Test Subject", teacher=self.teacher_user)

    def test_students_enrollment_and_access(self):
        # Students enroll in the course
        self.client.login(username='student1', password='123')
        self.client.get(reverse('enroll', kwargs={'course_id': self.course.id}))
        self.client.logout()

        self.client.login(username='student2', password='123')
        self.client.get(reverse('enroll', kwargs={'course_id': self.course.id}))
        self.client.logout()

        # Ensure teacher sees both students in the enrollment list
        self.client.login(username='teacher', password='123')
        response = self.client.get(reverse('coursedetails', kwargs={'course_id': self.course.id}))
        self.assertContains(response, 'student1')
        self.assertContains(response, 'student2')

        # Ensure both students can access the course
        self.client.login(username='student1', password='123')
        response = self.client.get(reverse('coursedetails', kwargs={'course_id': self.course.id}))
        self.assertEqual(response.status_code, 200)

        self.client.login(username='student2', password='123')
        response = self.client.get(reverse('coursedetails', kwargs={'course_id': self.course.id}))
        self.assertEqual(response.status_code, 200)

        # Remove one student from enrollment
        enrollment = Enrollment.objects.get(student=self.student_user_1, course=self.course)
        enrollment.delete()

        # Ensure the removed student can't access the course details anymore
        self.client.login(username='student1', password='123')
        response = self.client.get(reverse('coursedetails', kwargs={'course_id': self.course.id}))
        self.assertNotEqual(response.status_code, 200)  # Assuming there's a redirect or a permission denied response

        # Cleanup
        self.client.logout()

    def tearDown(self):
        User.objects.all().delete()
        Course.objects.all().delete()
        Enrollment.objects.all().delete()
