from django.urls import path
from .views import criar_reuniao_castelo

urlpatterns = [
    path('criar', criar_reuniao_castelo, name='criar_reuniao'),
]