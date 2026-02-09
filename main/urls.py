from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path("", views.index, name='Home'),
    path("my-courses", views.my_courses, name='MyCourses'),
    path("registration", views.registration, name='Registration'),
    path("login", views.login, name='Login'),
    path("creator-registration", views.creator_registration, name='CreatorRegistration'),
    path("math-foundation-course", views.math_foundation_course, name='Math Foundation Course'),
    path("math-foundation-class", views.math_foundation_class, name='Math Foundation Course'),
]
