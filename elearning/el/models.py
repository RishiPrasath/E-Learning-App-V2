from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class PortalUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    user_type = models.CharField(max_length=7, choices=USER_TYPE_CHOICES, default='student')
    email = models.EmailField(_('email address'), unique=True)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    real_name = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(blank=True,null=True)
    qualifications = models.TextField(blank=True ,null=True)

    class Meta:
        verbose_name = 'Portal User'
        verbose_name_plural = 'Portal Users'
        # Specify related_name for groups and user_permissions to resolve conflict
        permissions = [
            # Define any custom permissions for your PortalUser here
        ]


    def is_teacher(self):
        return self.user_type == 'teacher'
    
    def is_student(self):
        return self.user_type == 'student'

    def is_enrolled_in(self, course):
        return self.enrollments.filter(course=course).exists()


    def __str__(self):
        return self.username


# Stores status updates of PortalUsers
class StatusUpdate(models.Model):
    user = models.ForeignKey(PortalUser, on_delete=models.CASCADE, related_name='status_updates')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    subject = models.CharField(max_length=255, default='General')
    teacher = models.ForeignKey(PortalUser, on_delete=models.CASCADE, related_name='courses_taught')
    created_at = models.DateTimeField(auto_now_add=True)


# Define the Topic model to store information about topics within a course
class Topic(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='No description available')
    topic_number = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='topics')


# Define the CourseMaterial model to store course materials in a topic
class CourseMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='course_materials/')
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, related_name='materials')
    date_uploaded = models.DateTimeField(auto_now_add=True)



class Enrollment(models.Model):
    student = models.ForeignKey(PortalUser, on_delete=models.CASCADE, **{"related_name": "enrollments"},null=True, blank=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='enrollments')
    date_enrolled = models.DateTimeField(default=timezone.now)  # Assuming you have a Course model




class ChatGroup(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='chat_groups')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='chat_groups')
    created_at = models.DateTimeField(auto_now_add=True)


class ChatMessage(models.Model):
    group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(PortalUser, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



class Feedback(models.Model):
    student = models.ForeignKey(PortalUser, on_delete=models.CASCADE, related_name='feedback_given')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='feedback_received')
    rating = models.IntegerField()
    review = models.TextField(blank=True, null=True) # Optional review



class Notification(models.Model):
    notificationtype = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    recipients = models.ManyToManyField(PortalUser, related_name='notifications')
    redirectURL = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
