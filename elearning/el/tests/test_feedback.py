from django.test import TestCase
from django.urls import reverse
from el.models import PortalUser, Course, Feedback
from django.contrib.auth import get_user_model

class TestSubmittingFeedback(TestCase):
    def setUp(self):
        # Create a test student and teacher with unique email addresses
        self.student = get_user_model().objects.create_user(username='student', password='testpass123', email='student@test.com')
        self.teacher = get_user_model().objects.create_user(username='teacher', password='testpass123', email='teacher@test.com')

        # Create a test course taught by the teacher
        self.course = Course.objects.create(title='Test Course', description='Test Description', teacher=self.teacher)

        # Simulate enrolling the student in the course
        self.course.enrollments.create(student=self.student)

    def test_student_submits_feedback(self):
        self.client.login(username='student', password='testpass123')
        url = reverse('submit_feedback')
        response = self.client.post(url, {'course_id': self.course.id, 'rating': 5, 'review': 'Great course!'})

        # Check that the feedback was successfully submitted
        self.assertEqual(response.status_code, 302)  # Assuming redirection to a success page or the course detail page
        self.assertEqual(Feedback.objects.count(), 1)
        feedback = Feedback.objects.first()
        self.assertEqual(feedback.student, self.student)
        self.assertEqual(feedback.course, self.course)
        self.assertEqual(feedback.rating, 5)
        self.assertEqual(feedback.review, 'Great course!')


class TestViewingFeedback(TestCase):
    def setUp(self):
        # Assuming your user model has an 'is_teacher' field or method that correctly identifies the user as a teacher.
        self.teacher = get_user_model().objects.create_user(
            username='teacher', email='teacher@example.com', password='testpass123', user_type='teacher')
        self.student = get_user_model().objects.create_user(
            username='student', email='student@example.com', password='testpass123', user_type='student')
        self.course = Course.objects.create(
            title='Test Course', description='Test Description', teacher=self.teacher)

        # Enroll the student in the course
        self.course.enrollments.create(student=self.student)

        # Create feedback from the student
        Feedback.objects.create(
            student=self.student, course=self.course, rating=5, review='Great course!')

    def test_teacher_views_feedback(self):
        self.client.login(username='teacher', password='testpass123')
        response = self.client.get(reverse('coursedetails', args=[self.course.id]))

        # Check that the teacher can view the feedback on the course details page
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Great course!')
        self.assertContains(response, 'Rating: 5')
        self.assertContains(response, 'By: student')