from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class PortalUser(AbstractUser):
    STUDENT = 'student'
    TEACHER = 'teacher'
    USER_TYPE_CHOICES = [
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    real_name = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(blank=True)
    qualifications = models.TextField(blank=True)

    # Add custom related_name for groups and user_permissions fields
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="portal_users",
        related_query_name="portal_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="portal_users",
        related_query_name="portal_user",
    )

    def __str__(self):
        return self.username


# Define the Course model to store information about courses offered
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    subject = models.CharField(max_length=255, default='General')
    teacher = models.ForeignKey(PortalUser, on_delete=models.CASCADE, related_name='courses_taught')

# Define the Enrollment model to track student enrollment in courses
class Enrollment(models.Model):
    student = models.ForeignKey(PortalUser, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    date_enrolled = models.DateTimeField(default=timezone.now)

# Define the CourseMaterial model to store course materials
class CourseMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='course_materials/')
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, related_name='materials')
    date_uploaded = models.DateTimeField(auto_now_add=True)

# Define the Topic model to store information about topics within a course
class Topic(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='No description available')
    topic_number = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='topics')

# Define the Feedback model to collect feedback from students on courses
class Feedback(models.Model):
    student = models.ForeignKey(PortalUser, on_delete=models.CASCADE, related_name='feedback_given')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='feedback_received')
    rating = models.IntegerField()
    review = models.TextField()

# Define the StatusUpdate model to allow users to post status updates
class StatusUpdate(models.Model):
    user = models.ForeignKey(PortalUser, on_delete=models.CASCADE, related_name='status_updates')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# Define the ChatGroup model
class ChatGroup(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(PortalUser, related_name='chat_groups', blank=True)
    creator = models.ForeignKey(PortalUser, on_delete=models.CASCADE, related_name='chat_groups_created')

# Model for chat messages
class ChatMessage(models.Model):
    group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(PortalUser, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
