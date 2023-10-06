from django.urls import path
from . import views

urlpatterns = [
    path('', views.students, name = 'students'),
    path('detail/<str:id>', views.students_detail, name = 'students_detail'),
    path('create/', views.students_create, name = 'students_create'),
    path('delete/<str:id>', views.students_delete, name = 'students_delete'),
]