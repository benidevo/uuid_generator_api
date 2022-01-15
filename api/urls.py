from django.urls import path
from .views import GenerateUUIDView

urlpatterns = [
    path('', GenerateUUIDView.as_view(), name='generate-uuid'),
]
