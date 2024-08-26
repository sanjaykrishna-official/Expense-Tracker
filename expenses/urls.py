from django.urls import path
from . import views
from .views import login_view, logout_view, signup_view

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('add/', views.expense_add, name='expense_add'),
    path('edit/<int:pk>/', views.expense_edit, name='expense_edit'),
    path('delete/<int:pk>/', views.expense_delete, name='expense_delete'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
]
