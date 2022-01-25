from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.post_list, name='post_list'),
]