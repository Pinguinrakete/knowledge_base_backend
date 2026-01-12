from django.urls import path
from .views import DataSingleView


urlpatterns = [
    path('data/', DataSingleView.as_view(), name='data'),
]