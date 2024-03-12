from time import localtime
from django.http import FileResponse, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseNotModified, JsonResponse
from django.views.generic.edit import FormView
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView as AuthLoginView
from django.conf import settings
from django.contrib.auth import authenticate
import logging
from django.urls import path
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import PortalUser
from django.http import JsonResponse
from django.contrib import messages
import json
from django.db.models import Q
import os
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.core.serializers import serialize
from django.utils.safestring import mark_safe


def registration_page(request):
    if request.method == 'POST':
        form = PortalUserCreationForm(request.POST, request.FILES) # Pass the POST data to the form
        if form.is_valid():  # Check if the form data is valid
            try:
                form.save() # Save the user to the database
                return redirect('login')  # Redirect if save is successful
            except Exception as e: 
                return JsonResponse({
                    'success': False, 
                    'message': 'Registration failed. Please contact support.', 
                    'debug_error': str(e) if settings.DEBUG else None 
                }) # Return JSON response if save fails
        else:  # Form is invalid
            return JsonResponse({
                'success': False,  
                'message': 'Form data is invalid.', 
                'errors': form.errors  
            }) # Return JSON response if form is invalid
    else:  # GET request
        form = PortalUserCreationForm()
        return render(request, 'register.html', {'form': form}) # Render the registration form

def home_page(request):
    user = request.user # Get the current user
    notification_types = Notification.objects.values_list('notificationtype', flat=True).distinct() # Get distinct notification types

    print(f'Notification types: {notification_types}') # Print notification types for debugging

    notifications = {} # Create an empty dictionary to store notifications

    # Loop through the notification types
    for notification_type in notification_types:
        latest_notifications = Notification.objects.filter(
            notificationtype=notification_type, # Filter by notification type
            recipients=user # Filter by the current user
        ).order_by('-timestamp')[:5]

        # Serialize the QuerySet into JSON, then load it into Python data structures
        serialized_notifications = json.loads(serialize('json', latest_notifications, fields=('message', 'redirectURL', 'notificationtype','recipients')))
        
        # Extract the relevant fields from the serialized data
        notifications[notification_type] = [{
            'message': n['fields']['message'],
            'redirectURL': n['fields']['redirectURL'],
            'notificationtype': n['fields']['notificationtype'],
            'recipients': n['fields']['recipients'],

        } for n in serialized_notifications]

        # Print serialized data for debugging
        print(serialized_notifications)
    

        
    # Convert the entire notifications dict into a JSON string for the template
    context = {
        'user': user,
        'notifications_json': mark_safe(json.dumps(notifications))  # Ensure it's marked safe for use in the template
    }

    return render(request, 'home.html', context)

@login_required
def user_profile(request, username):
    
    
    
    user = get_object_or_404(PortalUser, username=username) # Get the user object
    is_owner = (request.user == user)  # Check ownership

    
    print(f'User profile requested for {username} by {request.user.username}. Is owner: {is_owner}')


    # Get the latest status update for the user
    latest_status = StatusUpdate.objects.filter(user=user).order_by('-timestamp').first()

    # Get list of courses taught by the user if they are a teacher
    courses_taught = None

    if user.is_teacher(): # Check if the user is a teacher
        courses_taught = user.courses_taught.all() # Get all courses taught by the user
        print(f'Courses taught by {user.username}: {courses_taught}') # Print courses taught for debugging
    else:
        courses_taught = None # Set to None if the user is not a teacher

    courses_enrolled = None # Set to None by default
    # Get all coures enrolled by the user if they are a student
    if user.is_student(): # Check if the user is a student
        courses_enrolled = user.enrollments.all() 
        
        for i in courses_enrolled:
            print(i.course.title) 

    else:
        courses_enrolled = None    

    print(f'Latest status: {latest_status.content if latest_status else "No status update available"}')

    context = {
        'user': user, # User details 
        'is_owner': is_owner , # Check if the current user is the owner of the profile
        'latest_status': latest_status , # Latest status update from the user
        'courses_taught': courses_taught, # Courses taught by the user if they are a teacher
        'courses_enrolled': courses_enrolled # Courses enrolled by the user if they are a student
    }
    return render(request, 'userprofile.html', context)

@login_required
def update_bio_field(request):
    username = request.POST.get('username') # Get the username from the POST data
    print(f'Updating bio for {username}')   # Print the username for debugging
    print(f'Bio content: {request.POST.get("bio")}')  # Print the bio content for debugging


    if request.method == 'POST':
        username = request.POST.get('username') # Get the username from the POST data
        new_bio = request.POST.get('bio') # Get the new bio content from the POST data
        
        user = PortalUser.objects.get(username=username)     
        try: 
            if request.user == user:  # Check if the current user is the owner of the profile  
                user.bio = new_bio
                user.save()
                messages.success(request, 'Bio updated successfully!') 
            else:
                messages.error(request, 'Unauthorized') 
        except Exception as e:
            logging.error(f'Error updating bio for {username}: {e}')
            messages.error(request, 'Error updating bio.')  

    return redirect('userprofile', username=username)  

@login_required
def update_qualifications_field(request): # Update qualifications field
    username = request.POST.get('username') # Get the username from the POST data
    new_qualifications = request.POST.get('qualifications') # Get the new qualifications content from the POST data

    print(f'Qualifications content: {new_qualifications}')
    
    if request.method == 'POST': # Check if the request method is POST
        user = PortalUser.objects.get(username=username)    

        try: 
            if request.user == user:  
                user.qualifications = new_qualifications
                user.save() # Save the user to the database
                messages.success(request, 'Qualifications updated successfully!') 
            else:
                messages.error(request, 'Unauthorized') 
        except Exception as e:
            messages.error(request, 'Error updating qualifications.')  

    return redirect('userprofile', username=username)  


@login_required
def post_status_update(request):
    if request.method == 'POST':
        form = StatusUpdateForm(request.POST)
        if form.is_valid(): # Check if the form data is valid
            update = form.save(commit=False)
            update.user = request.user
            update.save()
            # Create new Notification object
            notification = Notification.objects.create(
                notificationtype="Recent Status Update",
                message=f"{request.user.username} posted a new status update: \n {update.content}",
                redirectURL=f"/profile/{request.user.username}",  # Adjust according to your URL patterns
            )

            all_users = PortalUser.objects.all()    # get all users

            # create a list of all user ids in all_users
            all_user_ids = [user.id for user in all_users]



            notification.recipients.add(*all_users)

            status_poster = request.user.username # get the username of the status poster

            # Serialize notification data
            notification_data = {
                "notificationtype": notification.notificationtype,
                "message": notification.message,
                "redirectURL": notification.redirectURL,
                "timestamp": notification.timestamp.isoformat(),  
                "recipients": all_user_ids,
                "status_poster": status_poster,
            }

            # Send notification to WebSocket
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "notifications_group",
                {
                    "type": "notification.message",
                    "data": notification_data,
                }
            )

            return redirect('post_status_update')
    else:
        form = StatusUpdateForm()

    latest_status = StatusUpdate.objects.filter(user=request.user).order_by('-timestamp').first() # Get the latest status update for the user

    return render(request, 'statusupdate.html', {'form': form, 'status': latest_status})



@login_required
def create_course(request):
    if request.user.user_type != 'teacher':   # Check if the user is a teacher
        return redirect('home')  

    if request.method == 'POST': # Check if the request method is POST
        form = CourseCreationForm(request.POST)

        if form.is_valid():
            course = form.save(commit=False)  # Get the course object
            course.teacher = request.user # Set the teacher of the course to the current user
            course.save()  # Save the course to the database

            messages.success(request, 'Course created successfully!')
            print(f'Course created: {course.title}')




            # Create new Notification object
            notification = Notification.objects.create(
                notificationtype="Courses",
                message=f"{request.user.username} created a new course: {course.title}",
                redirectURL=f"/courses/{course.id}",  # Adjust according to your URL patterns
            )

            enrolled_students = PortalUser.objects.filter(
                enrollments__course__teacher=request.user
            ).distinct()

            notification.recipients.set(enrolled_students) # Set the recipients to the enrolled students

            #  get list of all user ids in enrolled_students
            enrolled_student_ids = [student.id for student in enrolled_students]

            # Serialize notification data
            notification_data = {
                "notificationtype": notification.notificationtype,
                "message": notification.message,
                "redirectURL": notification.redirectURL,
                "timestamp": notification.timestamp.isoformat(),  
                "recipients": enrolled_student_ids,
            }

            # Send notification to WebSocket
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "notifications_group",
                {
                    "type": "notification.message",
                    "data": notification_data,
                }
            )


            return redirect('coursedetails', course_id=course.id)  
        else:
            print(f'Error creating course: {form.errors}')

    # GET request: 
    form = CourseCreationForm() 
    return render(request, 'coursecreation.html', {'form': form})

@login_required
def search_page(request):
    print("Viewing search page")

    query = request.GET.get('q')

    # Handle empty search query
    if not query:
        # Print all students, teachers, and courses for debugging
        print("Printing all students:")
        for student in PortalUser.objects.filter(user_type='student'):
            print(student)

        print("Printing all teachers:")
        for teacher in PortalUser.objects.filter(user_type='teacher'):
            print(teacher)

        print("Printing all courses:")
        for course in Course.objects.all():
            print(course)

        # Return empty search results
        return render(request, 'search.html', {'courses': None, 'teachers': None , 'students': None, 'query': None})

    # Handle non-empty search query
    else:
        # Get search results for courses and teachers
        courses = Course.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        teachers = PortalUser.objects.filter(Q(user_type='teacher') & (Q(username__icontains=query) | Q(real_name__icontains=query)))
        students = PortalUser.objects.filter(Q(user_type='student') & (Q(username__icontains=query) | Q(real_name__icontains=query)))
        
        # Return search results
        return render(request, 'search.html', {'courses': courses, 'teachers': teachers, 'students':students , 'query': query})

def view_course_details(request, course_id):
    course = get_object_or_404(Course, id=course_id) # Get the course object
    if not request.user.is_authenticated:
        return redirect('login')
    # Check if the user is the teacher or is enrolled in the course
    if not course.enrollments.filter(student=request.user).exists() and request.user != course.teacher:
        # If not, return a forbidden response or redirect to a different page
        return HttpResponseForbidden("You are not authorized to view this course details.")

    enrolled_students = course.enrollments.all() # Get all students enrolled in the course
    feedback = Feedback.objects.filter(course=course) # Get all feedback for the course
    context = {
        'course': course, # Course details
        'enrolled_students': enrolled_students, # Enrolled students
        'is_enrolled_in': course.enrollments.filter(student=request.user).exists(), # Check if the user is enrolled in the course
        'is_teacher': request.user == course.teacher, # Check if the user is the teacher of the course
        'is_student': request.user.is_student(), # Check if the user is a student
        'topics': course.topics.all(),# Get all topics for the course
        'feedback': feedback, # Feedback for the course
    }

    return render(request, 'coursedetails.html', context)

@login_required
def enrollmentpage(request):
    search_term = request.GET.get('search', '').strip()
    # Get all courses
    courses = Course.objects.filter(
        Q(title__icontains=search_term) | 
        Q(teacher__real_name__icontains=search_term) |
        Q(description__icontains=search_term)
    )

    
    courses = courses.order_by('-created_at')  # Or any other default ordering

    enrollments = Enrollment.objects.filter(student=request.user) # Get all enrollments for the current user

    enrollments_json = json.dumps([
        {'courseId': enrollment.course.id} for enrollment in enrollments
    ])

    context = {
        'courses': courses,  # All courses
        'enrollments_json': enrollments_json, # Enrollments as JSON
        'search_term': search_term,  # Search term
    }
    return render(request, 'enrollment.html', context)


@login_required
def enroll(request, course_id):
    print('Enrolling in course')
    course = get_object_or_404(Course, id=course_id) # Get the course object

    if not Enrollment.objects.filter(student=request.user, course=course).exists(): # Check if the user is already enrolled in the course
        # Create enrollment
        Enrollment.objects.create(student=request.user, course=course) # Create a new enrollment for the user
        messages.success(request, "Successfully enrolled in the course!") # Display success message

        # Create a notification for the teacher
        notification = Notification.objects.create(
            notificationtype="Course Enrollment",
            message=f"A new student has enrolled in your course: {course.title}",
            redirectURL=f"/courses/{course.id}/",
        )

        # Assuming the Notification model has a recipients ManyToMany field for PortalUser
        notification.recipients.add(course.teacher)

        # Prepare notification data for WebSocket
        notification_data = {
            "notificationtype": notification.notificationtype,
            "message": notification.message,
            "redirectURL": notification.redirectURL,
            "timestamp": notification.timestamp.isoformat(),
            "recipients": [course.teacher.id],  # Assuming the teacher is the recipient
        }

        # Send notification to WebSocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications_group",
            {
                "type": "notification.message",
                "data": notification_data,
            }
        )

    else:
        messages.warning(request, "You are already enrolled in this course.")

    return redirect('coursedetails', course_id=course.id)
    
@login_required
def remove_enrollment(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id) # Get the enrollment object

    # Authorization: Ensure the current user is the course teacher
    if request.user != enrollment.course.teacher:
        messages.error(request, "You are not authorized to remove enrollments for this course.")
        return redirect('coursedetails', course_id=enrollment.course.id)

    student_id = enrollment.student.id  # Capture the student's ID before deletion
    course_title = enrollment.course.title  # Capture the course title for the message

    # Deletion and Success Message
    enrollment.delete()
    messages.success(request, "Student enrollment removed successfully.")

    # Create and send notification to the removed student
    notification = Notification.objects.create(
        notificationtype="Removed Enrollment",
        message=f"You have been removed from the course: {course_title}.",
        # Assuming Notification model doesn't need redirectURL for this case
    )

    # Set the recipient to the removed student
    notification.recipients.add(student_id)

    # Prepare and send WebSocket message
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notifications_group",
        {
            "type": "notification.message",
            "data": {
                "notificationtype": notification.notificationtype,
                "message": notification.message,
                "recipients": [student_id],  # Send to the removed student
            }
        }
    )

    return redirect('coursedetails', course_id=enrollment.course.id)

@login_required
def create_topic(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        topic_form = TopicCreationForm(request.POST)

        if topic_form.is_valid():
            topic = topic_form.save(commit=False)
            topic.course = course
            topic.save()

            # Assuming you have a mechanism to create chat groups
            chat_group_name = topic.name
            chat_group = ChatGroup.objects.create(
                name=chat_group_name,
                course=course,
                topic=topic
            )

            # Fetch all students enrolled in the course
            enrolled_students = course.enrollments.all().values_list('student', flat=True)

            # Create a notification for the new topic
            notification = Notification.objects.create(
                notificationtype="New Topic",
                message=f"New topic added to the course: {course.title}. Topic: {topic.name}.",
                redirectURL=f"/courses/{course.id}/",  # Adjust URL as needed
            )

            # Assuming Notification model supports multiple recipients
            notification.recipients.set(enrolled_students)

            # Prepare and send WebSocket message
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "notifications_group",
                {
                    "type": "notification.message",
                    "data": {
                        "notificationtype": notification.notificationtype,
                        "message": notification.message,
                        "redirectURL": notification.redirectURL,
                        "recipients": list(enrolled_students),  # Convert QuerySet to list
                    }
                }
            )

            return redirect('coursedetails', course_id=course_id)
        else:
            print(f'Topic form errors: {topic_form.errors}')

    else:
        topic_form = TopicCreationForm()

    context = {
        'course': course,
        'topic_form': topic_form,
    }
    return render(request, 'topiccreation.html', context)
  
@login_required
def delete_topic(request, course_id, topic_id):
    course = get_object_or_404(Course, id=course_id) # Ensure course exists
    topic = get_object_or_404(Topic, id=topic_id, course=course)  # Ensure topic belongs to the course

    if request.user != course.teacher:
        messages.error(request, "You are not authorized to delete this topic.") # Display error message
        return redirect('coursedetails', course_id=course_id) # Redirect to course details page

    topic.delete() # Delete the topic
    messages.success(request, "Topic deleted successfully!") # Display success message
    return redirect('coursedetails', course_id=course_id) # Redirect to course details page


def save_file_with_structure(uploaded_file, course, topic):
    # Get the base media root directory from settings
    media_root = settings.MEDIA_ROOT

    # Construct the desired file path
    target_dir = os.path.join(media_root, 'Course_Material', f'Course{course.id}', f'Topic{topic.id}')
    target_path = os.path.join(target_dir, uploaded_file.name) # Assuming the file name is unique

    # Ensure directories exist
    os.makedirs(target_dir, exist_ok=True) 

    # Save the file 
    with open(target_path, 'wb+') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)

    return target_path  

@login_required
def upload_file(request, course_id, topic_id):
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'message': 'User not authenticated'}, status=403) # Return 403 Forbidden if user is not authenticated

    course = get_object_or_404(Course, id=course_id) # Ensure course exists
    topic = get_object_or_404(Topic, id=topic_id, course=course) # Ensure topic belongs to the course

    if request.user != course.teacher:
        return JsonResponse({'success': False, 'message': 'You are not authorized to upload files for this course'}, status=403) # Return 403 Forbidden if user is not authorized

    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['file'] # Get the uploaded file
            file_name = uploaded_file.name # Get the file name

            # Assuming save_file_with_structure is a function that saves the file and returns the path
            saved_file_path = save_file_with_structure(uploaded_file, course, topic)

            course_material = CourseMaterial(
                course=course, # Set the course
                topic=topic, # Set the topic
                title=file_name, # Set the file title
                file=saved_file_path # Set the file path
            )
            course_material.save()

            # Fetch all students enrolled in the course
            enrolled_students = course.enrollments.all().values_list('student', flat=True)

            # Create and send notification
            notification = Notification.objects.create(
                notificationtype="New Material",
                message=f"New material added to the course: {course.title}. Material: {file_name}.",
                redirectURL=f"/courses/{course.id}/",  # Adjust URL as needed
            )

            # Assuming Notification model supports multiple recipients
            notification.recipients.set(enrolled_students)

            # Prepare and send WebSocket message
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "notifications_group",
                {
                    "type": "notification.message",
                    "data": {
                        "notificationtype": notification.notificationtype,
                        "message": notification.message,
                        "redirectURL": notification.redirectURL,
                        "recipients": list(enrolled_students),  # Convert QuerySet to list
                    }
                }
            )
            # Return JSON response with success message and file details
            return JsonResponse({
                'success': True,
                'message': "File uploaded successfully!",
                'file_name': file_name,
                'file_url': course_material.file.url,
                'topic_id': topic.id, 
                'material_id': course_material.id,
                'course_id': course.id
            })

        except Exception as e:
            print(f"Error uploading file: {e}")
            return JsonResponse({'success': False, 'message': "Error uploading file."}, status=500)

    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)  
    
@login_required
def delete_file(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        topic_id = request.POST.get('topic_id')
        material_id = request.POST.get('material_id')

        try:
            # Get the CourseMaterial object
            course_material = CourseMaterial.objects.get(id=material_id, topic__id=topic_id)
        except CourseMaterial.DoesNotExist: # Handle the case where the material does not exist
            messages.error(request, 'Course material does not exist.')
            return redirect('coursedetails', course_id=course_id)

        # Ensure that the user deleting the file is authorized to do so
        if request.user != course_material.course.teacher:
            messages.error(request, 'You are not authorized to delete this file.')
            return redirect('coursedetails', course_id=course_id)

        if course_material.file:
            try:
                # Construct the file path
                file_path = os.path.join(settings.MEDIA_ROOT, str(course_material.file)) 
                
                # Check if the file exists before attempting deletion
                if os.path.exists(file_path):
                    # Delete the file from storage
                    os.remove(file_path)
                    
                    # Delete the database record
                    course_material.delete()
                    
                    messages.success(request, 'File deleted successfully.')
                else:
                    messages.error(request, 'File not found.')
            except Exception as e:
                messages.error(request, f'Error deleting file: {e}')
        else:
            messages.error(request, 'No file associated with the material.')

        return redirect('coursedetails', course_id=course_id)

    return redirect('home')

@login_required
def download_material(request, material_id):
    print("Downloading material")
    material = get_object_or_404(CourseMaterial, id=material_id) # Ensure the material exists
    
    print("debugging code:")
    # Print file name and path for debugging
    print ('File name:', material.title)
    print ('File path:', material.file.path)

    return FileResponse(open(material.file.path, 'rb'), as_attachment=True) # Return the file as an attachment

# Chat views
def chat_page(request, course_id, topic_id):
    try:
        # Retrieve the course and topic objects or return 404 if not found
        course = get_object_or_404(Course, id=course_id)
        topic = get_object_or_404(Topic, id=topic_id)
        
        # Retrieve existing messages for the chat group
        messages = ChatMessage.objects.filter(group__course=course, group__topic=topic)

        # Serialize the messages as JSON
        serialized_messages = json.dumps([{'content': msg.content, 'user': msg.user.username} for msg in messages])

        # Create a chat group for the course and topic if it doesn't exist
        chat_group, created = ChatGroup.objects.get_or_create(course=course, topic=topic)
        
        # Return the chat page with the serialized messages
        return render(request, 'chat.html', {'course': course, 'topic': topic, 'chat_group': chat_group, 'serialized_messages': serialized_messages})

    except (Course.DoesNotExist, Topic.DoesNotExist):
        # Return 404 response if course or topic does not exist
        return HttpResponseNotFound("Course or topic not found")
    
# Feedback views
@login_required  
def feedback(request):
    # Get all courses the user is enrolled in
    enrolled_courses = request.user.enrollments.all().select_related('course')

    # Check if the user is enrolled in at least one course
    if enrolled_courses:
        courses = [(course.course.id, course.course.title) for course in enrolled_courses]

        # Print all course titles for debugging
        print("Courses enrolled in:")
        for course in courses:
            print(course[1])

        return render(request, 'feedback.html', {'courses': courses})
    else:
        return redirect('home')
 
@login_required
def submit_feedback(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        rating = request.POST.get('rating')
        review = request.POST.get('review')
        course = get_object_or_404(Course, id=course_id)

        # Create Feedback object and save it
        feedback = Feedback.objects.create(
            student=request.user,
            course=course,
            rating=rating,
            review=review
        )

        # Create and send notification to the course teacher
        notification = Notification.objects.create(
            notificationtype="Feedback",
            message=f"New feedback received for the course: {course.title}. Student: {request.user.get_full_name() or request.user.username}, Rating: {rating}, Review: {review}.",
            redirectURL=f"/courses/{course.id}/",  # Adjust URL as needed
        )

        # Set the recipient to the course teacher
        notification.recipients.add(course.teacher.id)

        # Prepare and send WebSocket message
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications_group",
            {
                "type": "notification.message",
                "data": {
                    "notificationtype": notification.notificationtype,
                    "message": notification.message,
                    "redirectURL": notification.redirectURL,
                    "recipients": [course.teacher.id],  # Send to the course teacher
                }
            }
        )

        # Redirect to home page after submitting feedback
        return redirect('home')
    else:
        return redirect('home')