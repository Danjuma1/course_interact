from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student_main/', views.student_main, name='student_main'),
    path('<int:course_id>/student_detail/', views.student_detail, name='student_detail'),
    path('lecturer_main/', views.lecturer_main, name='lecturer_main'),
    path('<int:course_id>/lecturer_detail/', views.lecturer_detail, name='lecturer_detail'),
    path('<int:course_id>/add_notification/', views.add_notification, name='add_notification'),
]