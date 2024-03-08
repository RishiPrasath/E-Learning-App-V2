 
from django.urls import path, re_path
from el import consumers 

websocket_urlpatterns = [
    path('ws/chat/<int:course_id>/<int:topic_id>/', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/notifications/$', consumers.NotificationConsumer.as_asgi()),
]