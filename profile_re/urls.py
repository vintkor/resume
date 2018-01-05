from django.urls import path
from .views import UsersList, UserDetail

urlpatterns = [
    path('', UsersList.as_view(), name='users'),
    path('<int:pk>/', UserDetail.as_view(), name='user'),
]
