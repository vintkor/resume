from django.urls import path
from .views import (
    ProjectDetailView,
    ProjectListView,
    TaskView,
    ModuleView,
    ProjectView,
    ClientView,
)

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project'),
    path('task/<int:pk>/', TaskView.as_view(), name='task-desc'),
    path('module/<int:pk>/', ModuleView.as_view(), name='module-desc'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project-desc'),
    path('client/<int:pk>/', ClientView.as_view(), name='client-desc'),
]
