from django.urls import path
from .views import indexPageView, aboutusPageView

urlpatterns = [
    path("", indexPageView, name="landingpage"),
    path("about/", aboutusPageView, name="aboutus")   
]   