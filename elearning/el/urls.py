from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Authentication
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('register/', registration_page, name='register'),

    # User Profiles
    path('home/', home_page, name='home'),
    path('profile/<str:username>/', user_profile, name='userprofile'),
    path('profile/update/bio/', update_bio_field, name='update_bio'),
    path('profile/update/qualifications/', update_qualifications_field, name='update_qualifications'),

    # Status Updates
    path('status/update/', post_status_update, name='post_status_update'),

    
    
  
    path('search/', search_page, name='search_page'),
 

    # Courses
    path('courses/<int:course_id>/', view_course_details, name='coursedetails'),
    path('courses/<int:course_id>/enroll/', enroll, name='enroll'),
    path('courses/create/', create_course, name='create_course'), 
    path('courses/<int:enrollment_id>/remove_enrollment/', remove_enrollment, name='remove_enrollment'),
    path('courses/enrollment/', enrollmentpage, name='enrollment'), # Enrollment page 
    



    #Add Topic
    path('courses/<int:course_id>/add_topic/', create_topic, name='create_topic'),
    # Delete Topic
    path('courses/<int:course_id>/topics/<int:topic_id>/delete/', delete_topic, name='delete_topic'), 

    # CourseMaterial
    path('courses/<int:course_id>/topics/<int:topic_id>/upload/', upload_file, name='upload_file'),
    path('delete_file/', delete_file, name='delete_file'),
    path('download_material/<int:material_id>/', download_material, name='download_material'),

    # Chat

    # Chat URLs
    path('chatpage/<int:course_id>/<int:topic_id>/', chat_page, name='chat_page'),
    

    # Feedback URLs

    path('feedback/', feedback, name='feedback'),
    path('submit_feedback/', submit_feedback, name='submit_feedback'),



]