from django.urls import path
from .views import dreamJobView

urlpatterns = [
    path("", dreamJobView, name="dream_job")
] 