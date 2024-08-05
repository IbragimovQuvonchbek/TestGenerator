from django.urls import path
from .views import download_randomized_docx

urlpatterns = [
    path('download-randomized-docx/', download_randomized_docx, name='download_randomized_docx'),
]
