
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('task/<int:id>', views.tasks),
    path('project/', views.projectHtml),
    path('tasks/', views.taskHtml),
    path('createTasks/', views.createTASK),
    path('createProject/', views.createProject),
    path('processFormProject/', views.processFormProject),
    path('processForm/', views.processForm, )


]