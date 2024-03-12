from django.contrib.auth.models import AbstractUser # Implements a fully featured User model 
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
    user = models.ForeignKey(PortalUser, on_delete=models.CASCADE, related_name='status_updates') # The user who posted the status update
    content = models.TextField() # The content of the status update
    timestamp = models.DateTimeField(auto_now_add=True) # The time the status update was posted


# Define the Course model to store information about courses
class Course(models.Model):
    title = models.CharField(max_length=255) # The title of the course
    description = models.TextField() # The description of the course
    subject = models.CharField(max_length=255, default='General') # The subject of the course
    teacher = models.ForeignKey(PortalUser, on_delete=models.CASCADE, related_name='courses_taught') # The teacher who teaches the course
    created_at = models.DateTimeField(auto_now_add=True) # The time the course was created


# Define the Topic model to store information about topics within a course
class Topic(models.Model):
    name = models.CharField(max_length=255) # The name of the topic
    description = models.TextField(default='No description available') # The description of the topic
    topic_number = models.IntegerField(default=0) # The number of the topic in the course
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='topics') # The course the topic belongs to


# Define the CourseMaterial model to store course materials in a topic
class CourseMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials') # The course the material belongs to
    title = models.CharField(max_length=255) # The title of the material
    file = models.FileField(upload_to='course_materials/') # The file of the material
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, related_name='materials')  # The topic the material belongs to
    date_uploaded = models.DateTimeField(auto_now_add=True) # The time the material was uploaded


# Define the Enrollment model to store information about students enrolled in a course
class Enrollment(models.Model):
    student = models.ForeignKey(PortalUser, on_delete=models.CASCADE, **{"related_name": "enrollments"},null=True, blank=True) # The student enrolled in the course
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='enrollments') # The course the student is enrolled in
    date_enrolled = models.DateTimeField(default=timezone.now)  # The time the student was enrolled in the course



# Define the ChatGroup and ChatMessage models to store chat messages
class ChatGroup(models.Model):
    name = models.CharField(max_length=255) # The name of the chat group
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='chat_groups') # The course the chat group belongs to
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='chat_groups') # The topic the chat group belongs to
    created_at = models.DateTimeField(auto_now_add=True) # The time the chat group was created

# Define the ChatMessage model to store chat messages
class ChatMessage(models.Model):
    group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE, related_name='messages') # The chat group the message belongs to
    user = models.ForeignKey(PortalUser, on_delete=models.CASCADE, related_name='messages') # The user who sent the message
    content = models.TextField() # The content of the message
    timestamp = models.DateTimeField(auto_now_add=True) # The time the message was sent


# Define the Feedback model to store feedback from students to teachers
class Feedback(models.Model):
    student = models.ForeignKey(PortalUser, on_delete=models.CASCADE, related_name='feedback_given') # The student who gave the feedback
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='feedback_received') # The course the feedback is for
    rating = models.IntegerField() # The rating given by the student
    review = models.TextField(blank=True, null=True)  # The review given by the student (optional) 


# Define the Notification model to store notifications for users
class Notification(models.Model):
    notificationtype = models.CharField(max_length=255) # The type of the notification
    message = models.CharField(max_length=255) # The message of the notification
    recipients = models.ManyToManyField(PortalUser, related_name='notifications') # The recipients of the notification
    redirectURL = models.CharField(max_length=255, blank=True, null=True) # The URL to redirect the user to
    timestamp = models.DateTimeField(auto_now_add=True) # The time the notification was created

    def __str__(self):
        return self.message
