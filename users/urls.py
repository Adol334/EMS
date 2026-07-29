from django.urls import path
from . import views
#URL patterns for authentication and dashboard routing
urlpatterns = [
    #Login page UR
    path('login/', views.login_view, name='login'),
    #Dashboard page URL (user homepage after login)
    path('dashboard/', views.dashboard, name='dashboard'),
    #Logout functionality URL
    path('logout/', views.logout_view, name='logout'),
]
