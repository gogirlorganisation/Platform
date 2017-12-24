from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done

app_name='accounts'
urlpatterns = [

    # Profile
    url(r'^profile/$', views.view_profile, name ='profile'),

    # Edit Profile Details
    url(r'^settings/edit/$', views.edit_profile, name ='edit_profile'),

    # Change Password
    url(r'^settings/edit/change_password$', views.change_password, name ='change_password'),

    # Login
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),

    # Logout
    url(r'^logout/$', logout,  {'next_page': '/'}, name='logout'),

    # Register
    url(r'^register/$', views.register, name='register'),

    # Curriculum 1
    url(r'^course-1/$', views.course_1, name='course1'),

    # Curriculum 2
    url(r'^course-2/$', views.course_2, name='course2'),

    # Curriculum 3
    url(r'^course-3/$', views.course_3, name='course3'),

    # Curriculum 4
    url(r'^course-4/$', views.course_4, name='course4'),

    # Curriculum 5
    url(r'^course-5/$', views.course_5, name='course5'),

    # Curriculum 6
    url(r'^course-6/$', views.course_6, name='course6'),

    # Curriculum 7
    url(r'^course-7/$', views.course_7, name='course7'),

    # Curriculum 8
    url(r'^course-8/$', views.course_8, name='course8'),

    # Curriculum 9
    url(r'^course-9/$', views.course_9, name='course9'),



]