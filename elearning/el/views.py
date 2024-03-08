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



def registration_page(request):
    if request.method == 'POST':
        form = PortalUserCreationForm(request.POST, request.FILES)
        if form.is_valid(): 
            try:
                form.save()
                return redirect('login')  # Redirect if save is successful
            except Exception as e: 
                return JsonResponse({
                    'success': False, 
                    'message': 'Registration failed. Please contact support.', 
                    'debug_error': str(e) if settings.DEBUG else None 
                })
        else:  # Form is invalid
            return JsonResponse({
                'success': False,  
                'message': 'Form data is invalid.', 
                'errors': form.errors  
            })
    else:  # GET request
        form = PortalUserCreationForm()
        return render(request, 'register.html', {'form': form})

def home_page(request):

    # get current user object
    user = request.user
    context = {
        'user': user
    }

    return render(request, 'home.html', context)

@login_required
def user_profile(request, username):
    
    logging.debug(f'User profile requested for {username}')
    
    user = get_object_or_404(PortalUser, username=username)
    is_owner = (request.user == user)  # Check ownership

    logging.debug(f'User profile requested for {username} by {request.user.username}. Is owner: {is_owner}')
    print(f'User profile requested for {username} by {request.user.username}. Is owner: {is_owner}')


    # Get the latest status update for the user
    latest_status = StatusUpdate.objects.filter(user=user).order_by('-timestamp').first()

    # Get list of courses taught by the user if they are a teacher
    courses_taught = None

    if user.is_teacher():
        courses_taught = user.courses_taught.all()
        print(f'Courses taught by {user.username}: {courses_taught}')
    else:
        courses_taught = None

    courses_enrolled = None
    # Get all coures enrolled by the user if they are a student
    if user.is_student():
        courses_enrolled = user.enrollments.all()
        print(f'Courses enrolled by {user.username}: {courses_enrolled}')
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
    username = request.POST.get('username')
    print(f'Updating bio for {username}')
    print(f'Bio content: {request.POST.get("bio")}')


    if request.method == 'POST':
        username = request.POST.get('username')
        new_bio = request.POST.get('bio')
        
        user = PortalUser.objects.get(username=username)  
        try: 
            if request.user == user:  
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
def update_qualifications_field(request):
    username = request.POST.get('username')
    new_qualifications = request.POST.get('qualifications')

    print(f'Qualifications content: {new_qualifications}')
    
    if request.method == 'POST':
        user = PortalUser.objects.get(username=username) 

        try: 
            if request.user == user:  
                user.qualifications = new_qualifications
                user.save()
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
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.save()

            notification = Notification.objects.create(
                notificationtype="Recent Status Update",
                message=f"{request.user.username} posted a new status update: \n {update.content}",
                redirectURL=f"/profile/{request.user.username}",  # Adjust according to your URL patterns
            )

            all_users = PortalUser.objects.all()

            # create a list of all user ids in all_users
            all_user_ids = [user.id for user in all_users]



            notification.recipients.add(*all_users)

            status_poster = request.user.username

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

    latest_status = StatusUpdate.objects.filter(user=request.user).order_by('-timestamp').first()

    return render(request, 'statusupdate.html', {'form': form, 'status': latest_status})



@login_required
def create_course(request):
    if request.user.user_type != 'teacher':  
        return redirect('home')  

    if request.method == 'POST':
        form = CourseCreationForm(request.POST)

        if form.is_valid():
            course = form.save(commit=False)  # Get the course object
            course.teacher = request.user
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

            notification.recipients.set(enrolled_students)

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
        return render(request, 'search.html', {'courses': None, 'teachers': None})

    # Handle non-empty search query
    else:
        # Get search results for courses and teachers
        courses = Course.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        teachers = PortalUser.objects.filter(Q(user_type='teacher') & (Q(username__icontains=query) | Q(real_name__icontains=query)))

        # Return search results
        return render(request, 'search.html', {'courses': courses, 'teachers': teachers, 'query': query})

@login_required
def view_course_details(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    enrolled_students = course.enrollments.all()  # Get all enrollments for the course
    
    # print all course materials
    for topic in course.topics.all():
        for material in topic.materials.all():
            print(material.title, material.file.url)


    context = {
        'course': course,
        'enrolled_students': enrolled_students,  # Add to context
        'is_enrolled_in': request.user.is_authenticated and course.enrollments.filter(student=request.user).exists(), 
        'is_teacher': request.user.is_authenticated and request.user == course.teacher, 
        'is_student': request.user.is_authenticated and request.user.is_student(),
        'topics': course.topics.all(),
    }


    return render(request, 'coursedetails.html', context)

@login_required
def enrollmentpage(request):
    search_term = request.GET.get('search', '').strip()

    courses = Course.objects.filter(
        Q(title__icontains=search_term) | 
        Q(teacher__real_name__icontains=search_term) |
        Q(description__icontains=search_term)
    )

    # Since sorting is removed, you can order by default here
    courses = courses.order_by('-created_at')  # Or any other default ordering

    enrollments = Enrollment.objects.filter(student=request.user)

    enrollments_json = json.dumps([
        {'courseId': enrollment.course.id} for enrollment in enrollments
    ])

    context = {
        'courses': courses, 
        'enrollments_json': enrollments_json,
        'search_term': search_term, 
    }
    return render(request, 'enrollment.html', context)


@login_required
def enroll(request, course_id):
    print('Enrolling in course')
    course = get_object_or_404(Course, id=course_id)

    if not Enrollment.objects.filter(student=request.user, course=course).exists():
        # Create enrollment
        Enrollment.objects.create(student=request.user, course=course)
        messages.success(request, "Successfully enrolled in the course!")

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
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)

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
    course = get_object_or_404(Course, id=course_id)
    topic = get_object_or_404(Topic, id=topic_id, course=course)  # Ensure topic belongs to the course

    if request.user != course.teacher:
        messages.error(request, "You are not authorized to delete this topic.")
        return redirect('coursedetails', course_id=course_id)

    topic.delete()
    messages.success(request, "Topic deleted successfully!")
    return redirect('coursedetails', course_id=course_id)


def save_file_with_structure(uploaded_file, course, topic):
    # Get the base media root directory from settings
    media_root = settings.MEDIA_ROOT

    # Construct the desired file path
    target_dir = os.path.join(media_root, 'Course_Material', f'Course{course.id}', f'Topic{topic.id}')
    target_path = os.path.join(target_dir, uploaded_file.name)

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
        return JsonResponse({'success': False, 'message': 'User not authenticated'}, status=403)

    course = get_object_or_404(Course, id=course_id)
    topic = get_object_or_404(Topic, id=topic_id, course=course)

    if request.user != course.teacher:
        return JsonResponse({'success': False, 'message': 'You are not authorized to upload files for this course'}, status=403)

    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['file']
            file_name = uploaded_file.name

            # Assuming save_file_with_structure is a function that saves the file and returns the path
            saved_file_path = save_file_with_structure(uploaded_file, course, topic)

            course_material = CourseMaterial(
                course=course,
                topic=topic,
                title=file_name,
                file=saved_file_path
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
        
        print("debugging code:")
        print('course_id:', course_id)
        print('topic_id:', topic_id)
        print('material_id:', material_id)

        try:
            course_material = CourseMaterial.objects.get(id=material_id, topic__id=topic_id)
        except CourseMaterial.DoesNotExist:
            messages.error(request, 'Course material does not exist.')
            return redirect('coursedetails', course_id=course_id)

        if course_material.file:
            # Use MEDIA_ROOT setting instead of hardcoding
            media_root = settings.MEDIA_ROOT
            file_relative_path = os.path.relpath(course_material.file.name, media_root)
            file_path = os.path.join(media_root, file_relative_path)

           
            try:
                # Delete the file and the database record
                course_material.file.delete(save=False)  # Deletes the file from storage
                course_material.delete()  # Deletes the database record
                messages.success(request, 'File deleted successfully.')
            except Exception as e:
                messages.error(request, f'Error deleting file: {e}')
        else:
            messages.error(request, 'No file associated with the material.')

        return redirect('coursedetails', course_id=course_id)

    return redirect('home')

@login_required
def download_material(request, material_id):
    print("Downloading material")
    material = get_object_or_404(CourseMaterial, id=material_id)
    
    print("debugging code:")
    # Print file name and path for debugging
    print ('File name:', material.title)
    print ('File path:', material.file.path)

    return FileResponse(open(material.file.path, 'rb'), as_attachment=True)






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
@login_required  # Assuming you have a decorator to ensure the user is a student
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