from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
import logging
from .models import *

logger = logging.getLogger(__name__)

class ChatConsumer(WebsocketConsumer):
    def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['topic_id']
        self.room_group_name = 'chat_%s' % self.room_name

        # Log available rooms
        logger.info("Available rooms: %s", self.channel_layer.groups)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):

        print('Received message...')

        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['username']
        course_id = text_data_json['course_id']
        topic_id = text_data_json['topic_id']
        chat_group_id = text_data_json['chat_group_id']


         # Create ChatMessage object
        sender_user = PortalUser.objects.get(username=sender)
        print('Creating Object...')
        ChatMessage.objects.create(
            group_id=chat_group_id,
            user=sender_user,
            content=message
        )

        # Get the ChatGroup object and related course
        chat_group = ChatGroup.objects.get(id=chat_group_id)
        course = chat_group.course

        # Fetch all recipient IDs: students enrolled in the course + the course's teacher
        student_ids = list(course.enrollments.all().values_list('student_id', flat=True))
        teacher_id = course.teacher.id
        recipients_ids = student_ids + [teacher_id]

        # Construct notification message data
        notification_message_data = {
            'type': 'notify',  # This should match a handler in Notification Consumer
            'chat_group_name': chat_group.name,
            'message': message,
            'sender': sender,
            'recipients_ids': recipients_ids,
        }

        # Send notification to Notification Consumer
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications_group",  # The Notification Consumer must be listening on this channel/group
            notification_message_data
        )




        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': sender,
                'course_id': course_id,
                'topic_id': topic_id,
                'chat_group_id': chat_group_id,
                'sender_channel_name': self.channel_name,  # Pass sender's channel name
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        # Get the username of the sender
        username = event['username']
        # Get the course ID
        course_id = event['course_id']
        # Get the topic ID
        topic_id = event['topic_id']
        # Get the chat group ID
        chat_group_id = event['chat_group_id']

        


        # Check if the recipient channel name is not the sender's channel name
        if self.channel_name != event['sender_channel_name']:
            # Send message to WebSocket
            self.send(text_data=json.dumps({
                'type': 'chat_message',
                'message': message,
                'username': username,
                'course_id': course_id,
                'topic_id': topic_id,
                'chat_group_id': chat_group_id,
            }))

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("notifications_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notifications_group", self.channel_name)

    async def receive(self, text_data):
        # Handle incoming WebSocket messages from the client
        pass

    async def notification_message(self, event):
        # Send the serialized notification data to the WebSocket
        data = event['data']
        await self.send(text_data=json.dumps(data))


    async def notify(self, event):
        # The event parameter contains the message data sent by group_send
        await self.send(text_data=json.dumps({
            'type': event['type'],
            'chat_group_name': event.get('chat_group_name', ''),
            'message': event.get('message', ''),
            'sender': event.get('sender', ''),
            'recipients_ids': event.get('recipients_ids', [])
        }))