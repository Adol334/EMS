from django.urls import path
from .import views

#URL patterns for the jobs app
urlpatterns = [
        #Jobs listing page
        path('jobs/',views.jobs, name='jobs'),
    
]
