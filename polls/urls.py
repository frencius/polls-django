from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/get/question', views.question_view, name='question'),
]