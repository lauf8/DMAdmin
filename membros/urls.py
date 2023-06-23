from django.urls import path
from .views import read_excel_view_castelo

urlpatterns = [
    path('read-excel/', read_excel_view_castelo, name='read_excel'),
]