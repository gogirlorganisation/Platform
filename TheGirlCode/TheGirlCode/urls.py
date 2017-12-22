from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    #Admin
    url(r'^admin/', admin.site.urls),

    #Home Page
    url(r'^$', views.home , name ='home'),

    #Home Page
    url(r'^aboutus/$', views.about_us , name ='about_us'),

    # Accounts
    url(r'^account/', include('accounts.urls')),



]
