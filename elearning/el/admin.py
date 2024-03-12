from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(PortalUser)
admin.site.register(StatusUpdate)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Topic)
admin.site.register(CourseMaterial)
admin.site.register(ChatGroup)
admin.site.register(ChatMessage)
admin.site.register(Feedback)
admin.site.register(Notification)

