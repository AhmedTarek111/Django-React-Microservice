from django.urls import path
from .api import JobRetrieveUpdateDestroyApi,JobListCreateApi
urlpatterns = [
    path('',JobListCreateApi.as_view()),
    path('<int:id>',JobRetrieveUpdateDestroyApi.as_view()),
]
