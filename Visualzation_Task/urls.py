from django.urls import path
from .views import timeline_view

urlpatterns = [
    path('timeline/', timeline_view, name='timeline'),
]
