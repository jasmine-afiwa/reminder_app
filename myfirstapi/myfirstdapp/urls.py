from django.urls import path
from .views import HelloWorld

urlpatterns = [
    path('yo/', HelloWorld.as_view(), name='hello_world'),
]