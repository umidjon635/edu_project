from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/<int:course_id>/', views.register, name='register'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('register/<int:course_id>/', views.register_course, name='register_course'),
]

