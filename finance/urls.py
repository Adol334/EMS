from django.urls import path
from .import views

#URL patterns for finance app
urlpatterns = [
    #Add income, Add expenses, savings, reports, and advisory pages
    path('income/', views.add_income, name='add_income'),
    path('expense/', views.add_expense, name='add_expense'),
    path('savings/', views.saving, name='saving'),
    path('report/', views.reports, name='report'),  
    path('advisory/', views.advisory, name='advisory'),

    #Delete specific income/expense record by primary key (id)
    path('delete-income/<int:pk>/', views.delete_income, name='delete_income'),
    path('delete-expense/<int:pk>/', views.delete_expense, name='delete_expense'),
]
