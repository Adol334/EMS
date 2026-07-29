from django.contrib import admin
from django.urls import path, include
from users import views as user_views

"""

URL configuration for ems_project project.
"""
#URL patterns for the application
urlpatterns = [
    #Django admin panel
    path('admin/', admin.site.urls),


    #Default homepage redirects to login view
    path('', user_views.login_view, name='login'),

    #Include URLs from the users, finance, and jobs apps
    path('', include('users.urls')),
    path('', include('finance.urls')),
    path('', include('jobs.urls')),

]